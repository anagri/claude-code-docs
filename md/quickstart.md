url: https://docs.anthropic.com/en/docs/claude-code/quickstart

---

This quickstart guide will have you using AI-powered coding assistance in just a few minutes. By the end, you’ll understand how to use Claude Code for common development tasks.

## Before you begin

Make sure you have:

  * A terminal or command prompt open
  * A code project to work with
  * A [Claude.ai](https://claude.ai) \(recommended\) or [Anthropic Console](https://console.anthropic.com/) account

## Step 1: Install Claude Code

### NPM Install

If you have [Node.js 18 or newer installed](https://nodejs.org/en/download/):
[code]
    npm install -g @anthropic-ai/claude-code

[/code]

### Native Install

Alternatively, try our new native install, now in beta.

**macOS, Linux, WSL:**
[code]
    curl -fsSL claude.ai/install.sh | bash

[/code]

**Windows PowerShell:**
[code]
    irm https://claude.ai/install.ps1 | iex

[/code]

## Step 2: Log in to your account

Claude Code requires an account to use. When you start an interactive session with the `claude` command, you’ll need to log in:
[code]
    claude
    # You'll be prompted to log in on first use

[/code]
[code]
    /login
    # Follow the prompts to log in with your account

[/code]

You can log in using either account type:

  * [Claude.ai](https://claude.ai) \(subscription plans - recommended\)
  * [Anthropic Console](https://console.anthropic.com/) \(API access with pre-paid credits\)

Once logged in, your credentials are stored and you won’t need to log in again.

When you first authenticate Claude Code with your Anthropic Console account, a workspace called “Claude Code” is automatically created for you. This workspace provides centralized cost tracking and management for all Claude Code usage in your organization.

You can have both account types under the same email address. If you need to log in again or switch accounts, use the `/login` command within Claude Code.

## Step 3: Start your first session

Open your terminal in any project directory and start Claude Code:
[code]
    cd /path/to/your/project
    claude

[/code]

You’ll see the Claude Code prompt inside a new interactive session:
[code]
    ✻ Welcome to Claude Code!

    ...

    > Try "create a util logging.py that..."

[/code]

After logging in \(Step 2\), your credentials are stored on your system. Learn more in [Credential Management](/en/docs/claude-code/iam#credential-management).

## Step 4: Ask your first question

Let’s start with understanding your codebase. Try one of these commands:
[code]
    > what does this project do?

[/code]

Claude will analyze your files and provide a summary. You can also ask more specific questions:
[code]
    > what technologies does this project use?

[/code]
[code]
    > where is the main entry point?

[/code]
[code]
    > explain the folder structure

[/code]

You can also ask Claude about its own capabilities:
[code]
    > what can Claude Code do?

[/code]
[code]
    > how do I use slash commands in Claude Code?

[/code]
[code]
    > can Claude Code work with Docker?

[/code]

Claude Code reads your files as needed - you don’t have to manually add context. Claude also has access to its own documentation and can answer questions about its features and capabilities.

## Step 5: Make your first code change

Now let’s make Claude Code do some actual coding. Try a simple task:
[code]
    > add a hello world function to the main file

[/code]

Claude Code will:

  1. Find the appropriate file
  2. Show you the proposed changes
  3. Ask for your approval
  4. Make the edit

Claude Code always asks for permission before modifying files. You can approve individual changes or enable “Accept all” mode for a session.

## Step 6: Use Git with Claude Code

Claude Code makes Git operations conversational:
[code]
    > what files have I changed?

[/code]
[code]
    > commit my changes with a descriptive message

[/code]

You can also prompt for more complex Git operations:
[code]
    > create a new branch called feature/quickstart

[/code]
[code]
    > show me the last 5 commits

[/code]
[code]
    > help me resolve merge conflicts

[/code]

## Step 7: Fix a bug or add a feature

Claude is proficient at debugging and feature implementation.

Describe what you want in natural language:
[code]
    > add input validation to the user registration form

[/code]

Or fix existing issues:
[code]
    > there's a bug where users can submit empty forms - fix it

[/code]

Claude Code will:

  * Locate the relevant code
  * Understand the context
  * Implement a solution
  * Run tests if available

## Step 8: Test out other common workflows

There are a number of ways to work with Claude:

**Refactor code**
[code]
    > refactor the authentication module to use async/await instead of callbacks

[/code]

**Write tests**
[code]
    > write unit tests for the calculator functions

[/code]

**Update documentation**
[code]
    > update the README with installation instructions

[/code]

**Code review**
[code]
    > review my changes and suggest improvements

[/code]

**Remember** : Claude Code is your AI pair programmer. Talk to it like you would a helpful colleague - describe what you want to achieve, and it will help you get there.

## Essential commands

Here are the most important commands for daily use:

Command| What it does| Example
---|---|---
`claude`| Start interactive mode| `claude`
`claude "task"`| Run a one-time task| `claude "fix the build error"`
`claude -p "query"`| Run one-off query, then exit| `claude -p "explain this function"`
`claude -c`| Continue most recent conversation| `claude -c`
`claude -r`| Resume a previous conversation| `claude -r`
`claude commit`| Create a Git commit| `claude commit`
`/clear`| Clear conversation history| `> /clear`
`/help`| Show available commands| `> /help`
`exit` or Ctrl+C| Exit Claude Code| `> exit`

See the [CLI reference](/en/docs/claude-code/cli-reference) for a complete list of commands.

## Pro tips for beginners

Be specific with your requests

Instead of: “fix the bug”

Try: “fix the login bug where users see a blank screen after entering wrong credentials”

Use step-by-step instructions

Break complex tasks into steps:
[code]
    > 1. create a new database table for user profiles

[/code]
[code]
    > 2. create an API endpoint to get and update user profiles

[/code]
[code]
    > 3. build a webpage that allows users to see and edit their information

[/code]

Let Claude explore first

Before making changes, let Claude understand your code:
[code]
    > analyze the database schema

[/code]
[code]
    > build a dashboard showing products that are most frequently returned by our UK customers

[/code]

Save time with shortcuts

  * Use Tab for command completion
  * Press ↑ for command history
  * Type `/` to see all slash commands

## What’s next?

Now that you’ve learned the basics, explore more advanced features:

## [Common workflowsStep-by-step guides for common tasks](/en/docs/claude-code/common-workflows)## [CLI referenceMaster all commands and options](/en/docs/claude-code/cli-reference)## [ConfigurationCustomize Claude Code for your workflow](/en/docs/claude-code/settings)

## Getting help

  * **In Claude Code** : Type `/help` or ask “how do I…”
  * **Documentation** : You’re here\! Browse other guides
  * **Community** : Join our [Discord](https://www.anthropic.com/discord) for tips and support

Was this page helpful?

YesNo

[Overview](/en/docs/claude-code/overview)[Common workflows](/en/docs/claude-code/common-workflows)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
