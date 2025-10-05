# Claude Code Common Workflows Summary

## Understanding New Codebases
- Get quick codebase overview
- Find relevant code for specific features

## Bug Fixing
- Share error messages with Claude
- Get fix recommendations and apply them
- Reproduce and trace issues

## Code Refactoring
- Identify legacy/deprecated code
- Get modernization recommendations
- Apply changes safely with verification

## Specialized Subagents
- View available subagents with `/agents`
- Automatic delegation to appropriate subagents
- Create custom project-specific subagents

## Plan Mode
- Safe code analysis with read-only operations
- Multi-step implementation planning
- Interactive development and code exploration
- Switch modes with Shift+Tab or `--permission-mode plan`

## Testing
- Identify untested code
- Generate test scaffolding and meaningful test cases
- Run and verify tests

## Pull Requests
- Summarize changes
- Generate PR descriptions with context
- Add testing details and review information

## Documentation
- Find undocumented code
- Generate JSDoc/docstring comments
- Review against project standards

## Working with Images
- Drag/drop or paste images for analysis
- Analyze UI elements, screenshots, errors
- Generate code from visual mockups

## File References
- Use `@` syntax to reference files and directories
- Reference MCP resources with `@server:resource`
- Include multiple files in single message

## Extended Thinking
- Complex architectural decisions
- Deep reasoning for challenging problems
- Use "think" prompts for various depths of analysis

## Conversation Management
- Resume with `--continue` (most recent) or `--resume` (picker)
- Non-interactive continuation with `--print`
- Full context and tool state preservation

## Git Worktrees
- Run parallel Claude sessions with isolation
- Create separate working directories for different tasks
- Manage multiple branches simultaneously

## Unix-style Utility Usage
- Add Claude to build scripts as linter/reviewer
- Pipe data in/out with structured formatting
- Control output format (text/json/stream-json)

## Custom Slash Commands
- Create project-specific commands in `.claude/commands/`
- Personal commands in `~/.claude/commands/`
- Use `$ARGUMENTS` placeholder for flexible commands

## Self-Documentation
- Ask Claude about its own capabilities
- Get documentation-based answers about features
- Latest documentation access regardless of version
