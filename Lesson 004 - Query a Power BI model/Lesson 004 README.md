# Lesson 004 - Query a Power BI model

**Objective:** Create an MCP server that connects to Power BI REST APIs to query workspaces, datasets, and run DAX queries.

**Outcome:** Build a server with 4 tools that can discover Power BI workspaces, list datasets, get model definitions, and execute DAX queries.

**Video:** [How to create a Power BI MCP server to chat with data (004 - Learn MCP servers for data & analytics)](https://www.youtube.com/watch?v=bZYzZZF1AEc)

### Steps

1. Follow along in the video and create a basic server that can list the Power BI workspaces.
2. Use the Power BI documentation to try the APIs.
3. Use VS Code to be able to set environment variables to store your token. You can get a token:
   - From the "Try it" REST API examples (for personal, educational use).
   - By setting up app registration (complex).
   - By using other methods of authentication not covered in this series (because it is a complex and sensitive topic).
   - For Claude Desktop, you will need to use other methods to store the token, like:
      - Hard-coded in the constant (**security risk - not recommended**).
      - Using libraries like `keyring`.
      - Setting an environment variable on your computer.
4. Run and test your server.
5. Extend the server with the other tools as described in the course.
6. Run the Power BI server from the provided code: [powerbi_server.py](powerbi_server.py)
7. The server provides four tools:
   - `list_workspaces` - Find your Power BI workspaces
   - `list_datasets` - Show datasets in a workspace
   - `get_model_definition` - Get dataset schema information
   - `execute_dax_query` - Run DAX queries against datasets
8. Test with prompts like:
   - "show my Power BI workspaces"
   - "list datasets in workspace X"
   - "run this DAX query: EVALUATE VALUES('Date'[Year])"
9. Experiment with modifying, extending, and restricting the functionality. Please use responsibly.


### Key takeaways

- Plan your tools before you make them. Use wireframes and diagrams to understand the steps and dependencies. 
- Ensure that a tool always has sufficient context to be able to give the best results. Don't rely on manual user input for context because that is unreliable and unlikely to happen often.
- Using APIs can be complex, and involves handling:
   - Authentication.
   - Request formatting and content.
   - Finding / using the appropriate endpoints.
   - Handling and formatting the response.
- You might need to use the Power BI APIs for some things and Fabric APIs for others. You can use Fabric APIs with Fabric items without having a Fabric capacity.
- VS Code has special options to save your tokens securely when you are testing an MCP server. 
- Ensure that you have good error handling to understand when you get no results, bad results, or incorrect results.
- Pay attention to how you return the outputs. Don't try to return "everything" and just select the stuff that you need. Don't try to create "the one tool to rule them all". It's just like data modelling.
- Do your due diligence and research the appropriate authentication methods to use for the APIs. There are many options, now, and some options are more suitable than others for different scenarios. I can't advise you on this in the scope of this series.
