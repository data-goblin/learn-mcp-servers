"""
Minimal Power BI MCP Server for querying and discovery (FastMCP)

Example prompts to test this server:
'How many workspaces do I have access to?'
'What datasets are available in workspace X?'
'How many measures are in the semantic model Y?'
'What is the DAX for measure Z?'
'What is the total sales by product category?'
"""

#region Imports
import json
import re
import requests
import os
import time
import base64
import keyring
from fastmcp import FastMCP
#endregion


#region Configuration
# Create server
mcp = FastMCP("powerbi-server")

# API endpoints
POWERBI_API = "https://api.powerbi.com/v1.0/myorg"
FABRIC_API = "https://api.fabric.microsoft.com/v1"

# Authentication - choose one approach:
# Option 1: Environment variable (default)
TOKEN = os.environ.get("POWERBI_TOKEN", "")

# Option 2: Keyring (recommended for Claude)
# You must first run `keyring set powerbi token` in the terminal.
# TOKEN = keyring.get_password("powerbi", "token")
#endregion


#region Helper Functions
## Simple HTTP request helper
## Returns JSON response or error dict
def make_request(url, method="GET", data=None):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        else:
            response = requests.post(url, headers=headers, json=data)
        
        if response.ok:
            return response.json()
        else:
            return {"error": f"HTTP {response.status_code}: {response.text[:200]}"}
    except Exception as e:
        return {"error": str(e)}


## Wait for a long-running operation to complete
## Polls the operation status until success or failure
def wait_for_operation(location_url, retry_seconds=30):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    while True:
        time.sleep(retry_seconds)
        response = requests.get(location_url, headers=headers)
        
        if response.ok:
            data = response.json()
            status = data.get('status', '')
            
            if status == 'Succeeded':
                # Get the final result
                result_response = requests.get(f"{location_url}/result", headers=headers)
                return result_response.json() if result_response.ok else {"error": "Failed to get result"}
            elif status == 'Failed':
                return {"error": data.get('error', 'Operation failed')}
            # Keep waiting if still running
        else:
            return {"error": f"Failed to check status: {response.status_code}"}


SKIP_PATHS = (
    "definition/cultures/",
    "definition/roles/",
    "definition/perspectives/",
    "definition/expressions.tmdl",
    "definition/dataSources.tmdl",
)
SKIP_PROPERTIES = {"lineageTag", "extendedProperty", "sourceLineageTag", "annotation", "changedProperty", "sourceColumn", "partition"}


def strip_tmdl(content):
    kept = []
    skip_indent = None
    for line in content.splitlines():
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        if skip_indent is not None and (not stripped or indent > skip_indent):
            continue
        skip_indent = None
        if re.split(r"[\s:=]", stripped, maxsplit=1)[0] in SKIP_PROPERTIES:
            skip_indent = indent
            continue
        kept.append(line)
    return "\n".join(kept)
#endregion


#region MCP Tool Functions
@mcp.tool()
def list_workspaces() -> str:
    """
    List all Power BI workspaces you have access to.
    Returns formatted list of workspace names and IDs.
    Examples: 'show my workspaces', 'what Power BI workspaces do I have?', 'list all workspaces'
    """
    result = make_request(f"{POWERBI_API}/groups")
    
    if "error" in result:
        return f"Error: {result['error']}"
    
    workspaces = result.get("value", [])
    if not workspaces:
        return "No workspaces found"
    
    output = f"Found {len(workspaces)} workspaces:\n\n"
    for ws in workspaces:
        output += f"• {ws['name']} (ID: {ws['id']})\n"
    
    return output


@mcp.tool()
def list_datasets(workspace_id: str) -> str:
    """
    List all datasets in a specific workspace.
    Returns formatted list of dataset names and IDs.
    Examples: 'show datasets in workspace X', 'what datasets are available?', 'list all semantic models'
    """
    result = make_request(f"{POWERBI_API}/groups/{workspace_id}/datasets")
    
    if "error" in result:
        return f"Error: {result['error']}"
    
    datasets = result.get("value", [])
    if not datasets:
        return "No datasets found in this workspace"
    
    output = f"Found {len(datasets)} datasets:\n\n"
    for ds in datasets:
        output += f"• {ds['name']} (ID: {ds['id']})\n"
    
    return output


@mcp.tool()
def get_model_definition(workspace_id: str, dataset_id: str) -> str:
    """
    Get the TMDL definition of a semantic model including tables, columns, measures, and relationships.
    Leaves out metadata that DAX queries do not need: lineage tags, annotations, extended properties, partitions, source columns, cultures, roles, perspectives, and data sources.
    Returns the model structure in TMDL format which is necessary to do before evaluating DAX queries.
    Examples: 'show me the data model', 'what tables are in this dataset?', 'get all measures and their DAX'
    """
    # Call Fabric API
    url = f"{FABRIC_API}/workspaces/{workspace_id}/semanticModels/{dataset_id}/getDefinition"
    response = requests.post(url, headers={"Authorization": f"Bearer {TOKEN}"})
    
    # Handle long-running operation
    if response.status_code == 202:
        location = response.headers.get('Location')
        retry_after = int(response.headers.get('Retry-After', 30))
        result = wait_for_operation(location, retry_after)
    elif response.ok:
        result = response.json()
    else:
        return f"Error: HTTP {response.status_code}"
    
    if "error" in result:
        return f"Error: {result['error']}"
    
    # Extract and decode TMDL parts
    parts = result.get("definition", {}).get("parts", [])
    if not parts:
        return "No model definition found"
    
    output = f"Dataset Model Definition (TMDL Format)\n{'='*40}\n\n"
    
    for part in parts:
        path = part.get("path", "")
        payload = part.get("payload", "")
        
        # Skip non-TMDL files
        if not path.endswith('.tmdl') or path.startswith(SKIP_PATHS):
            continue
            
        try:
            # Decode content
            content = base64.b64decode(payload).decode('utf-8')
            
            # Add section header
            output += f"\n{'─'*40}\n"
            output += f"File: {path}\n"
            output += f"{'─'*40}\n"
            output += strip_tmdl(content)
            output += "\n"
            
        except Exception as e:
            output += f"\nError decoding {path}: {str(e)}\n"
    
    return output


@mcp.tool()
def execute_dax_query(workspace_id: str, dataset_id: str, query: str) -> str:
    """
    Execute a DAX query against a Power BI dataset.
    Returns query results as JSON data.
    Examples:
        'tell me the total sales by product category',
        'what is the revenue and profit by year and month?',
        'how many customers are there by country?'
    Example DAX queries:
        "EVALUATE SUMMARIZECOLUMNS('Product'[Category], "@TotalSales", SUM('Sales'[Amount]))", 
        "EVALUATE SUMMARIZECOLUMNS('Date'[Year], 'Date'[Month], "@Revenue", SUM('Sales'[Revenue]), "@Profit", SUM('Sales'[Profit]))", 
        "EVALUATE SUMMARIZECOLUMNS('Customer'[Country], "@CustomerCount", COUNTROWS('Customer'))"
    """
    data = {"queries": [{"query": query}]}
    url = f"{POWERBI_API}/groups/{workspace_id}/datasets/{dataset_id}/executeQueries"
    result = make_request(url, method="POST", data=data)
    
    if "error" in result:
        return f"Error: {result['error']}"
    
    # Just return the actual data
    results = result.get("results", [])
    if results and "tables" in results[0]:
        return json.dumps(results[0]["tables"], indent=2)
    else:
        return "No data returned"
#endregion


#region Main Entry Point
if __name__ == "__main__":
    mcp.run()
#endregion