# Lesson 002 - Your First MCP Server

**Objective:** Create an MCP server that can communicate with a host application.

**Outcome:** Create an MCP server in Python that will say "Hello World".

**Video:** [Create your first MCP server! (002 - Learn MCP servers for data & analytics)](https://www.youtube.com/watch?v=Iy1-_hoU8IY)


### Steps

1. Understand what imports are required.
2. Initialize the server.
3. List the tools:
    - Understand tool names
    - Understand descriptions
    - Understand the input schema
4. Set up tool calling.
5. Understand how `FastMCP` is more concise than `mcp`.
6. Set up the config and test the server in VS Code and Claude Desktop.


### Key takeaways

- A server can be as simple as a single Python script.
    - More advanced servers will be projects of multiple files.
- A server has several common components:
    - (Optional) Docstring for documenting the script / file / server.
    - Imports for necessary libraries
    - Server instance
    - Tool registry
        - Listing tools
        - Calling tools
    - Each tool must have:
        - A name.
        - Any arguments and their explicit types.
        - Output types.
        - (Optional) Description, which is necessary for the LLM to "find" the tool effectively .
    - Runner (to run the server)
- Suggestions for code hygeine:
    - Format your code.
    - Use error handling.
    - Organize it into "code regions"
- In Python, the `FastMCP` library takes care of the basic boilerplate.
    - This helps make your code more concise.
    - It is good to try a few times with the `mcp` library first to understand it.