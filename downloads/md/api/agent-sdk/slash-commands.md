url: https://docs.claude.com/en/api/agent-sdk/slash-commands

---

Slash commands provide a way to control Claude Code sessions with special commands that start with `/`. These commands can be sent through the SDK to perform actions like clearing conversation history, compacting messages, or getting help.

## Discovering Available Slash Commands

The Claude Agent SDK provides information about available slash commands in the system initialization message. Access this information when your session starts:

TypeScript

Python

Copy
[code]
    import { query } from "@anthropic-ai/claude-agent-sdk";

    for await (const message of query({
      prompt: "Hello Claude",
      options: { maxTurns: 1 }
    })) {
      if (message.type === "system" && message.subtype === "init") {
        console.log("Available slash commands:", message.slash_commands);
        // Example output: ["/compact", "/clear", "/help"]
      }
    }

[/code]

## Sending Slash Commands

Send slash commands by including them in your prompt string, just like regular text:

TypeScript

Python

Copy
[code]
    import { query } from "@anthropic-ai/claude-agent-sdk";

    // Send a slash command
    for await (const message of query({
      prompt: "/compact",
      options: { maxTurns: 1 }
    })) {
      if (message.type === "result") {
        console.log("Command executed:", message.result);
      }
    }

[/code]

## Common Slash Commands

### /compact- Compact Conversation History

The `/compact` command reduces the size of your conversation history by summarizing older messages while preserving important context:

TypeScript

Python

Copy
[code]
    import { query } from "@anthropic-ai/claude-agent-sdk";

    for await (const message of query({
      prompt: "/compact",
      options: { maxTurns: 1 }
    })) {
      if (message.type === "system" && message.subtype === "compact_boundary") {
        console.log("Compaction completed");
        console.log("Pre-compaction tokens:", message.compact_metadata.pre_tokens);
        console.log("Trigger:", message.compact_metadata.trigger);
      }
    }

[/code]

### /clear- Clear Conversation

The `/clear` command starts a fresh conversation by clearing all previous history:

TypeScript

Python

Copy
[code]
    import { query } from "@anthropic-ai/claude-agent-sdk";

    // Clear conversation and start fresh
    for await (const message of query({
      prompt: "/clear",
      options: { maxTurns: 1 }
    })) {
      if (message.type === "system" && message.subtype === "init") {
        console.log("Conversation cleared, new session started");
        console.log("Session ID:", message.session_id);
      }
    }

[/code]

## Creating Custom Slash Commands

In addition to using built-in slash commands, you can create your own custom commands that are available through the SDK. Custom commands are defined as markdown files in specific directories, similar to how subagents are configured.

### File Locations

Custom slash commands are stored in designated directories based on their scope:

  * **Project commands** : `.claude/commands/` \- Available only in the current project
  * **Personal commands** : `~/.claude/commands/` \- Available across all your projects

### File Format

Each custom command is a markdown file where:

  * The filename \(without `.md` extension\) becomes the command name
  * The file content defines what the command does
  * Optional YAML frontmatter provides configuration

#### Basic Example

Create `.claude/commands/refactor.md`:

Copy
[code]
    Refactor the selected code to improve readability and maintainability.
    Focus on clean code principles and best practices.

[/code]

This creates the `/refactor` command that you can use through the SDK.

#### With Frontmatter

Create `.claude/commands/security-check.md`:

Copy
[code]
    ---
    allowed-tools: Read, Grep, Glob
    description: Run security vulnerability scan
    model: claude-3-5-sonnet-20241022
    ---

    Analyze the codebase for security vulnerabilities including:
    - SQL injection risks
    - XSS vulnerabilities
    - Exposed credentials
    - Insecure configurations

[/code]

### Using Custom Commands in the SDK

Once defined in the filesystem, custom commands are automatically available through the SDK:

TypeScript

Python

Copy
[code]
    import { query } from "@anthropic-ai/claude-agent-sdk";

    // Use a custom command
    for await (const message of query({
      prompt: "/refactor src/auth/login.ts",
      options: { maxTurns: 3 }
    })) {
      if (message.type === "assistant") {
        console.log("Refactoring suggestions:", message.message);
      }
    }

    // Custom commands appear in the slash_commands list
    for await (const message of query({
      prompt: "Hello",
      options: { maxTurns: 1 }
    })) {
      if (message.type === "system" && message.subtype === "init") {
        // Will include both built-in and custom commands
        console.log("Available commands:", message.slash_commands);
        // Example: ["/compact", "/clear", "/help", "/refactor", "/security-check"]
      }
    }

[/code]

### Advanced Features

#### Arguments and Placeholders

Custom commands support dynamic arguments using placeholders: Create `.claude/commands/fix-issue.md`:

Copy
[code]
    ---
    argument-hint: [issue-number] [priority]
    description: Fix a GitHub issue
    ---

    Fix issue #$1 with priority $2.
    Check the issue description and implement the necessary changes.

[/code]

Use in SDK:

TypeScript

Python

Copy
[code]
    import { query } from "@anthropic-ai/claude-agent-sdk";

    // Pass arguments to custom command
    for await (const message of query({
      prompt: "/fix-issue 123 high",
      options: { maxTurns: 5 }
    })) {
      // Command will process with $1="123" and $2="high"
      if (message.type === "result") {
        console.log("Issue fixed:", message.result);
      }
    }

[/code]

#### Bash Command Execution

Custom commands can execute bash commands and include their output: Create `.claude/commands/git-commit.md`:

Copy
[code]
    ---
    allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
    description: Create a git commit
    ---

    ## Context

    - Current status: !`git status`
    - Current diff: !`git diff HEAD`

    ## Task

    Create a git commit with appropriate message based on the changes.

[/code]

#### File References

Include file contents using the `@` prefix: Create `.claude/commands/review-config.md`:

Copy
[code]
    ---
    description: Review configuration files
    ---

    Review the following configuration files for issues:
    - Package config: @package.json
    - TypeScript config: @tsconfig.json
    - Environment config: @.env

    Check for security issues, outdated dependencies, and misconfigurations.

[/code]

### Organization with Namespacing

Organize commands in subdirectories for better structure:

Copy
[code]
    .claude/commands/
    ├── frontend/
    │   ├── component.md      # Creates /component (project:frontend)
    │   └── style-check.md     # Creates /style-check (project:frontend)
    ├── backend/
    │   ├── api-test.md        # Creates /api-test (project:backend)
    │   └── db-migrate.md      # Creates /db-migrate (project:backend)
    └── review.md              # Creates /review (project)

[/code]

The subdirectory appears in the command description but doesn’t affect the command name itself.

### Practical Examples

#### Code Review Command

Create `.claude/commands/code-review.md`:

Copy
[code]
    ---
    allowed-tools: Read, Grep, Glob, Bash(git diff:*)
    description: Comprehensive code review
    ---

    ## Changed Files
    !`git diff --name-only HEAD~1`

    ## Detailed Changes
    !`git diff HEAD~1`

    ## Review Checklist

    Review the above changes for:
    1. Code quality and readability
    2. Security vulnerabilities
    3. Performance implications
    4. Test coverage
    5. Documentation completeness

    Provide specific, actionable feedback organized by priority.

[/code]

#### Test Runner Command

Create `.claude/commands/test.md`:

Copy
[code]
    ---
    allowed-tools: Bash, Read, Edit
    argument-hint: [test-pattern]
    description: Run tests with optional pattern
    ---

    Run tests matching pattern: $ARGUMENTS

    1. Detect the test framework (Jest, pytest, etc.)
    2. Run tests with the provided pattern
    3. If tests fail, analyze and fix them
    4. Re-run to verify fixes

[/code]

Use these commands through the SDK:

TypeScript

Python

Copy
[code]
    import { query } from "@anthropic-ai/claude-agent-sdk";

    // Run code review
    for await (const message of query({
      prompt: "/code-review",
      options: { maxTurns: 3 }
    })) {
      // Process review feedback
    }

    // Run specific tests
    for await (const message of query({
      prompt: "/test auth",
      options: { maxTurns: 5 }
    })) {
      // Handle test results
    }

[/code]

## See Also

  * [Slash Commands](/en/docs/claude-code/slash-commands) \- Complete slash command documentation
  * [Subagents in the SDK](/en/api/agent-sdk/subagents) \- Similar filesystem-based configuration for subagents
  * [TypeScript SDK reference](/en/docs/claude-code/typescript-sdk-reference) \- Complete API documentation
  * [SDK overview](/en/api/agent-sdk/overview) \- General SDK concepts
  * [CLI reference](/en/docs/claude-code/cli-reference) \- Command-line interface

Was this page helpful?

YesNo

[Subagents in the SDK](/en/api/agent-sdk/subagents)[Tracking Costs and Usage](/en/api/agent-sdk/cost-tracking)
