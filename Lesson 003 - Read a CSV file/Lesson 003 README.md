# Lesson 003 - Read a CSV file

**Objective:** Create an MCP server that can read and analyze CSV files.

**Outcome:** Build a server with a `read_csv` tool that can load CSV files, show their contents, and provide basic information about the data. Add an `aggregate_csv` tool for basic analysis.

**Video:** [Create an MCP server to analyze CSV files (003 - Learn MCP servers for data & analytics)](https://www.youtube.com/watch?v=HVFtf3FpFaY)


### Steps

1. Follow the video to create the server yourself.
2. Adjust and extend the server and experiment with new functionality.
3. Try to find cases where the tools do not work as expected and optimize the tool functionality or description to improve the result.
4. Experiment with cases like when you want an optional parameter / argument (like the group by columns)... what do you do?


### Example Usage

```
User: "Read the file sales_data.csv"
Server: Shows file contents, row count, column names, and sample data
```

### Key Takeaways

- Tools require careful planning and thought about their use.
- You shouldn't just return raw outputs.
   - They will be too many tokens.
   - The LLM will be shit at doing stuff with it.
   - But sometimes a raw output might be the best option.
   - Observe the golden rule: "it depends".
- Ensure you build in robust, informative, helpful error handling so that users know how to tune prompts to get better results.
- Account for things like casing, spaces, and so on in user inputs.
- Test, test, test -- ensure you test tools often and in different clients, models, and scenarios.