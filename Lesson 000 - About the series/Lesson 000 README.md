# Lesson 000 - About the Series

**Objective:** Get all the necessary requirements for the course. If you need help, please independently find other resources about installation, set-up, and use of the required software and processes.

**Outcome:** Install the necessary software and libraries and clone the repo on your local computer.

**Video:** [Learn MCP servers for data and analytics! (000 - About the series)](https://www.youtube.com/watch?v=KQFmZiDXk-I)


### Steps

1. Install [VS Code](https://code.visualstudio.com/download).
2. Install [Claude Desktop](https://claude.ai/download).
3. Download and install [Python](http://python.org).
4. Install the required Python libraries by running this command in your terminal:
    ```bash
    pip install -r requirements.txt
    ```
    or
    ```bash
    python -m pip install -r requirements.txt
    ```
    or (on a Mac)
    ```bash
    python3 -m pip install -r requirements.txt
    ```
    - This will install all the necessary dependencies listed in the `requirements.txt` file in the root directory
    - If you're using a virtual environment (recommended), activate it first before running the pip command
5. Install and set up Git
    - Download and install [Git](https://git-scm.com/downloads)
    - Set up user identity (name and email)

```bash
# Set your Git username (replace with your actual name)
git config --global user.name "Your Full Name"

# Set your Git email (replace with your actual email)
git config --global user.email "your.email@example.com"

# Verify your configuration
git config --global user.name
git config --global user.email
```

6. Clone this repository using VS Code
    - Open VS Code
    - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) to open the Command Palette
    - Type "Git: Clone" and select it
    - Enter the repository URL: `https://github.com/[repository-owner]/teach_MCP.git`
    - Choose a folder location on your computer where you want to save the project
    - VS Code will clone the repository and ask if you want to open it - click "Open"
    
    Alternatively, you can clone using the terminal:
    ```bash
    # Navigate to where you want to store the project
    cd C:\Users\YourUsername\Documents
    
    # Clone the repository
    git clone https://github.com/[repository-owner]/teach_MCP.git
    
    # Open the project in VS Code
    code teach_MCP
    ```

7. Open the project in VS Code (if not already open)
    - The project should now be available in VS Code
    - You should see all the lesson folders in the Explorer panel
    - You're ready to start with Lesson 001.
  
8. Perform [first-time setup of GitHub Copilot](https://code.visualstudio.com/docs/copilot/setup). You might want to start a trial for GitHub Copilot, too.

### Key takeaways

    - None; just get the pre-requisites set up.
