# Lesson 001 - Your First MCP Server

**Objective:** Use an MCP host with a local and a remote MCP server.

**Outcome:** Search the Microsoft Docs and run the local server from [Lesson 002](<../Lesson 002 - Your first MCP server>), which just simply returns a variation test text of `hello world`.

**Video:** [How to use MCP servers with VS Code & Claude Desktop (001 - Learn MCP servers for data & analytics)](https://www.youtube.com/watch?v=ovZX1JdnjXY)

### Steps

1. Create the config files. There are several examples:
    - [claude_config.json](claude_config.json) (Lesson 002 example local server only)
    - [.vscode/mcp.json](../.vscode/mcp.json) 

2. Set up configuration of the remote Microsoft Docs server and local server for Claude Desktop.
    - Integrations menu (Remote server endpoint).
    - Settings config JSON file (Local servers and remote).

3. Set up configuration of the servers in VS Code via its config file.

4. Experiment with the MCP servers in both tools and compare / contrast the experiences.

### Key takeaways

- You can use _remote servers_ and _local servers_
    - Remote servers are maintained and run by someone else.
    - Local servers are run on your local computer.

> [!NOTE]
> To use remote servers in Claude Desktop, you need a supported [subscription](https://www.anthropic.com/pricing).
> 

- In Claude Desktop, you can integrate MCP servers in two ways:
    1. [Integrations menu](https://support.anthropic.com/en/articles/11175166-getting-started-with-custom-integrations-using-remote-mcp), required for remote servers. This is also where you manage permissions and review tools, resources, and prompts.
    2. [Claude Desktop configuration JSON file](https://modelcontextprotocol.io/quickstart/user): Settings > Developer > Config.json file. Here you have to add the configuration in a specific format. This is necessary for local servers, but you can also add remote servers here.
    3. [Desktop extensions](https://www.anthropic.com/engineering/desktop-extensions), which streamline the installation process for local servers.

       
- Claude Desktop is different from VS Code (GitHub Copilot) in the following ways:
    1. You have more control over model behavior.
    2. The UI/UX is simpler and more focused on consumption.
    3. You can create "artifacts" including diagrams and interactive visuals.
    4. You don't have "Agent Mode".
    5. You can't call tools with a reference like `/`, `#`, or `@` (yet). You can only implicitly invoke servers and tools by using natural language.
    6. It doesn't support all of the MCP server features.
    7. You have to manually run local servers from a terminal and reboot Claude Desktop after adding the config to make the connection.


- VS Code is different from Claude Desktop in the following ways:
    1. You can choose more models, but only control their behavior with context.
    2. The UI/UX is more complex and 'busy' because it is a developer tool.
    3. You can't create visuals / images in artifacts.
    4. You can choose between different modes, like Ask, Agent, and Edit. Agent mode lets you edit multiple files at once in an open folder.
    5. You can call tools and servers by using `#` to mention them. You don't typically "implicitly" reference MCP servers or their tools within VS Code; this is an intentional design choice to avoid unintentionally invoking a server or tool.
    6. It supports more MCP features.
    7. You can manage MCP servers from the config file, including starting, stopping, running, and more.


- You will likely use VS Code for developer projects and you will likely use Claude for consumption and data analysis (or similar tools). But you might be forced to use VS Code since it's from Microsoft and your organization might not allow you to use Claude Desktop or have an enterprise subscription set up. Considerations for security and licensing apply for both tools.


- Be careful with what MCP servers you trust and use. Bad actors can create malicious and deceptive servers that steal your information or harm you in some way.
