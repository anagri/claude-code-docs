# Claude Code Slash Commands: A Hands-On Tutorial

## Introduction

This tutorial is designed for intermediate Claude Code CLI users who want to master slash commands—one of the most powerful customization features in Claude Code. By the end of this guide, you'll be able to create reusable command templates, automate complex workflows, and integrate slash commands with other Claude Code features like sub-agents, hooks, and headless mode.

**What you'll learn:**
- Create custom slash commands with arguments and dynamic content
- Execute bash commands safely within slash commands
- Build cross-feature workflows combining slash commands with sub-agents, hooks, and CI/CD
- Organize commands effectively for team sharing
- Troubleshoot common issues and follow best practices

**Prerequisites:**
- Claude Code CLI installed and configured
- Basic familiarity with Claude Code interactive mode
- Understanding of markdown and YAML frontmatter

## What Are Slash Commands?

Slash commands are shortcuts that execute predefined prompts in Claude Code. They come in two varieties:

**Built-in commands** handle session management, configuration, and debugging:
- `/clear` - Start a fresh conversation
- `/compact` - Reduce conversation history while preserving context
- `/help` - View all available commands
- `/memory` - Edit CLAUDE.md files
- `/model` - Switch AI models

**Custom commands** are markdown files you create containing prompts Claude executes. When you run a custom command, Claude receives the file's content as a prompt and responds accordingly.

Under the hood, custom commands work through the SlashCommand tool. When Claude sees a command in your instructions or you invoke it directly, the tool expands the markdown file into a full prompt. This happens transparently—you just see Claude executing your saved workflow.

## Quick Start (5 minutes)

Let's create your first custom slash command to understand the basics.

### Create a Code Review Command

```bash
# Create the commands directory
mkdir -p .claude/commands

# Create a simple review command
cat > .claude/commands/review.md << 'EOF'
Review this code for:
- Code quality and readability
- Security vulnerabilities
- Performance issues
- Best practices adherence

Provide specific, actionable feedback.
EOF
```

### Use Your Command

```bash
# Start Claude Code
claude

# Use your custom command
> /review @src/auth.js
```

Claude will now analyze the file using your predefined review criteria. The `@` symbol includes the file content in the context automatically.

**What makes this useful:** Instead of retyping review criteria every time, you've created a reusable template that ensures consistent code reviews across your project.

## Built-In Slash Commands Reference

| Category | Command | Purpose |
|----------|---------|---------|
| **Session Management** | `/clear` | Clear conversation history |
| | `/compact [instructions]` | Compact conversation with optional focus |
| | `/rewind` | Restore previous code/conversation state |
| **Configuration** | `/config` | Open Settings interface |
| `/model` | Select or change AI model |
| `/memory` | Edit CLAUDE.md memory files |
| `/permissions` | View or update permissions |
| **Debugging** | `/bug` | Report bugs to Anthropic |
| `/doctor` | Check installation health |
| `/status` | Show version, model, connectivity |
| `/cost` | Display token usage statistics |
| **Utilities** | `/help` | Get usage help |
| `/init` | Initialize project with CLAUDE.md |
| `/agents` | Manage custom AI subagents |
| `/mcp` | Manage MCP server connections |

## Creating Custom Slash Commands

### Anatomy of a Slash Command File

Custom slash commands live in two locations:

**Project commands** (`.claude/commands/`) - Shared with your team via version control:
```bash
.claude/commands/
├── optimize.md          # /optimize command
├── security-check.md    # /security-check command
└── frontend/
    └── component.md     # /component command (shows "project:frontend")
```

**Personal commands** (`~/.claude/commands/`) - Available across all your projects:
```bash
~/.claude/commands/
├── explain.md          # /explain command
└── debug.md           # /debug command
```

**File structure:**
```markdown
---
description: Brief description of the command
argument-hint: [arg1] [arg2] (optional - shown in autocomplete)
model: claude-3-5-haiku-20241022 (optional - override model)
allowed-tools: Bash(git:*), Read, Edit (optional - tool restrictions)
---

Your prompt template goes here.
Use $ARGUMENTS for all arguments or $1, $2 for specific ones.
Use !`command` to execute bash commands.
Use @filename to reference files.
```

### Hands-On Exercise 1: Simple Text Command

**Goal:** Create a command that generates unit tests for any file.

```bash
# Create the command file
cat > .claude/commands/test.md << 'EOF'
---
description: Generate comprehensive unit tests
---

Generate unit tests for this code following these requirements:
1. Cover all public functions and methods
2. Include edge cases and error scenarios
3. Use the project's existing test framework
4. Add descriptive test names and comments
5. Achieve at least 80% code coverage
EOF
```

**Usage:**
```bash
> /test @src/calculator.js
```

**What makes this unique:** This demonstrates the simplest form—a static prompt template. Every invocation uses the same instructions, ensuring consistent test generation across your codebase.

### Hands-On Exercise 2: Arguments and Variables

**Goal:** Create a flexible bug-fix command that accepts issue numbers and priority levels.

```bash
cat > .claude/commands/fix-issue.md << 'EOF'
---
description: Fix a GitHub issue with priority
argument-hint: [issue-number] [priority]
---

Fix GitHub issue #$1 with priority level: $2

Steps:
1. Read the issue description from GitHub
2. Locate the relevant code in our codebase
3. Implement a solution that addresses the root cause
4. Add appropriate tests
5. Create a descriptive commit message

Priority context:
- high: Focus on quick, safe resolution
- medium: Balance thoroughness with speed
- low: Optimize for code quality and refactoring
EOF
```

**Usage:**
```bash
> /fix-issue 123 high
# $1 becomes "123", $2 becomes "high"

> /fix-issue 456 medium
# $1 becomes "456", $2 becomes "medium"
```

**What makes this unique:** Positional arguments ($1, $2) enable command customization at runtime. This single template adapts to different issues and priority levels, making it far more versatile than static commands.

### Hands-On Exercise 3: Bash Execution

**Goal:** Create a git commit command that analyzes current changes.

```bash
cat > .claude/commands/commit.md << 'EOF'
---
description: Create a git commit with analysis
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
---

## Current Git Context

- Status: !`git status`
- Staged changes: !`git diff --cached`
- Unstaged changes: !`git diff`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5`

## Your Task

Based on the changes above:
1. Stage appropriate files with `git add`
2. Create a descriptive commit message following conventional commits
3. Execute the commit
4. Confirm successful commit
EOF
```

**Usage:**
```bash
> /commit
```

**What makes this unique:** The `!` prefix executes bash commands and includes their output in the prompt. The `allowed-tools` frontmatter restricts Claude to only specific git commands, providing a security boundary. This pattern is essential for commands that need live system state.

## Real-World Examples

### Example 1: PR Review with GitHub Integration

```bash
cat > .claude/commands/pr-review.md << 'EOF'
---
description: Comprehensive pull request review
allowed-tools: Bash(gh:*), Read, Grep
argument-hint: [pr-number]
---

## Pull Request Analysis for #$1

### Fetch PR Details
!`gh pr view $1 --json title,body,files`

### Changed Files
!`gh pr diff $1 --name-only`

### Full Diff
!`gh pr diff $1`

### Review Checklist

Analyze the above PR for:

1. **Code Quality**
   - Readability and maintainability
   - Adherence to project conventions
   - DRY principle violations

2. **Security**
   - Input validation
   - SQL injection risks
   - XSS vulnerabilities
   - Exposed credentials

3. **Performance**
   - N+1 queries
   - Unnecessary computations
   - Memory leaks

4. **Testing**
   - Test coverage for new code
   - Edge case handling
   - Error scenarios

5. **Documentation**
   - Code comments where needed
   - Updated README/docs
   - API documentation

Provide actionable feedback organized by priority (critical, important, nice-to-have).
EOF
```

**What makes this unique:** This command integrates with GitHub CLI (gh) to fetch live PR data, then performs structured analysis. It demonstrates how slash commands can bridge Claude Code with external systems, creating powerful automation workflows. The combination of `!` command execution and structured review criteria ensures thorough, consistent PR reviews.

### Example 2: Database Migration Validator

```bash
cat > .claude/commands/validate-migration.md << 'EOF'
---
description: Validate database migration safety
allowed-tools: Bash(ls:*), Read, Grep
argument-hint: [migration-file]
---

## Migration Safety Analysis for $1

### Migration Content
@$1

### Related Models
!`grep -r "class.*Model" app/models/ --include="*.py"`

### Existing Migrations
!`ls -la migrations/ | tail -10`

### Safety Checklist

Analyze this migration for:

1. **Breaking Changes**
   - Column drops without backup
   - Non-nullable columns without defaults
   - Index removals on large tables

2. **Performance Impact**
   - Blocking DDL operations
   - Missing indexes on foreign keys
   - Full table scans required

3. **Rollback Strategy**
   - Reversible operations
   - Data preservation
   - Downtime requirements

4. **Dependencies**
   - Model changes required
   - Application code updates
   - Configuration changes

Provide:
- Risk assessment (low/medium/high)
- Required preparatory steps
- Rollback procedure
- Recommended deployment window
EOF
```
**What makes this unique:** This command performs multi-source analysis—reading the migration file, scanning model definitions, and listing migration history. It demonstrates the power of combining file references (@), bash execution (!), and structured prompts to create domain-specific validation tools.

## Cross-Feature Integration Patterns

### Integration 1: Slash Commands + Sub-Agents

Slash commands can delegate tasks to specialized sub-agents for better context management and expertise.

**Create a security-focused sub-agent:**
```bash
cat > .claude/agents/security-expert.md << 'EOF'
---
description: Security vulnerability analysis expert
tools: Read, Grep, Glob
model: opus
---

You are a senior security engineer specializing in vulnerability detection.
Focus exclusively on security issues including:
- SQL injection, XSS, CSRF
- Authentication/authorization flaws
- Cryptographic weaknesses
- Sensitive data exposure
- Security misconfigurations

Provide CVE references where applicable and rate findings by CVSS score.
EOF
```

**Create a command that uses the sub-agent:**
```bash
cat > .claude/commands/security-audit.md << 'EOF'
---
description: Full security audit using expert sub-agent
---

Use the security-expert subagent to perform a comprehensive security audit.

Scan the following critical areas:
- Authentication system: @src/auth/
- API endpoints: @src/api/
- Database queries: @src/db/
- User input handling: @src/forms/
- Configuration files: @config/

For each area, the security expert should:
1. Identify vulnerabilities
2. Assess severity (critical/high/medium/low)
3. Provide remediation steps
4. Suggest preventive controls

Generate a final security report with prioritized findings.
EOF
```

**Why this pattern is useful:** Sub-agents maintain separate context windows, preventing information overload. The security expert can deeply analyze code without cluttering the main conversation. This pattern is ideal for specialized analysis tasks that benefit from dedicated expertise and focused context.

### Integration 2: Slash Commands + Hooks

Slash commands can trigger hooks for automation, validation, and logging.

**Configure a hook to validate changes:**
```json
// .claude/settings.json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-changes.sh"
          }
        ]
      }
    ]
  }
}
```

**Create the validation hook:**
```bash
cat > .claude/hooks/validate-changes.sh << 'EOF'
#!/bin/bash
# Read hook input from stdin
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path')

# Run linter on modified file
if [[ "$file_path" == *.js ]]; then
  if ! eslint "$file_path" 2>&1; then
    echo "ESLint failed for $file_path" >&2
    exit 2  # Block with error
  fi
fi

exit 0  # Success
EOF
chmod +x .claude/hooks/validate-changes.sh
```

**Create a command that modifies code:**
```bash
cat > .claude/commands/refactor.md << 'EOF'
---
description: Refactor code with automatic validation
allowed-tools: Read, Edit, MultiEdit
---

Refactor $ARGUMENTS to improve:
- Code clarity and readability
- Performance and efficiency
- Maintainability

The PostToolUse hook will automatically validate your changes with ESLint.
If validation fails, you'll need to fix the issues before proceeding.
EOF
```

**Why this pattern is useful:** Hooks provide automatic quality gates. Every file edit triggers linting, ensuring code standards are maintained. This creates a safety net—Claude can't proceed with invalid changes. It's particularly valuable in team environments where consistency is critical.

### Integration 3: Slash Commands + Headless Mode

Slash commands can be used in CI/CD pipelines for automated workflows.

**GitHub Actions workflow:**
```yaml
# .github/workflows/auto-fix.yml
name: Auto-fix Issues

on:
  issues:
    types: [labeled]

jobs:
  auto-fix:
    if: github.event.label.name == 'auto-fix'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Fix Issue
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          issue_number="${{ github.event.issue.number }}"
          claude --print "/fix-issue $issue_number high" \
            --output-format json \
            --permission-mode bypassPermissions \
            --max-turns 10 > result.json

      - name: Create PR
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Parse result and create PR
          result=$(jq -r '.result' result.json)
          branch_name="auto-fix-${{ github.event.issue.number }}"

          git checkout -b "$branch_name"
          git add .
          git commit -m "Auto-fix: Issue #${{ github.event.issue.number }}"
          git push origin "$branch_name"

          gh pr create \
            --title "Auto-fix: Issue #${{ github.event.issue.number }}" \
            --body "$result" \
            --base main
```

**GitLab CI/CD example:**
```yaml
# .gitlab-ci.yml
auto-fix-issues:
  stage: fix
  only:
    - issues
  script:
    - npm install -g @anthropic-ai/claude-code
    - |
      claude --print "/fix-issue ${CI_ISSUE_IID} medium" \
        --output-format json \
        --permission-mode bypassPermissions \
        --max-turns 8 > result.json
    - git checkout -b "fix-${CI_ISSUE_IID}"
    - git add .
    - git commit -m "Auto-fix issue ${CI_ISSUE_IID}"
    - git push origin "fix-${CI_ISSUE_IID}"
  variables:
    ANTHROPIC_API_KEY: $ANTHROPIC_API_KEY
```

**Why this pattern is useful:** Headless mode enables Claude Code to run without human interaction in CI/CD pipelines. Slash commands encapsulate complex workflows that can be triggered automatically. This is powerful for routine maintenance tasks—label an issue "auto-fix" and CI automatically implements a solution and creates a PR. It reduces manual work while maintaining quality through tested command templates.

### Integration 4: Slash Commands + Memory

Commands can modify CLAUDE.md files to capture learned patterns.

**Create a command that learns from feedback:**
```bash
cat > .claude/commands/learn-pattern.md << 'EOF'
---
description: Learn and save a coding pattern
argument-hint: [pattern-name]
---

I'm documenting a new coding pattern: $1

Steps:
1. Ask me to explain the pattern, including:
   - When to use it
   - Implementation details
   - Best practices
   - Common pitfalls

2. After I provide the explanation, append it to CLAUDE.md under a "## Coding Patterns" section with this format:
   ```
   ### $1

   **When to use:** [from my explanation]
   **Implementation:** [from my explanation]
   **Best practices:** [from my explanation]
   **Pitfalls:** [from my explanation]
   ```

3. Confirm the pattern has been saved and will be used in future sessions.

This ensures the pattern is remembered across all future conversations in this project.
EOF
```

**Usage example:**
```bash
> /learn-pattern "Error Boundary Pattern"
Claude: Please explain when to use the Error Boundary Pattern...

> [Your explanation]

Claude: I've added the Error Boundary Pattern to CLAUDE.md.
It will now be available in all future sessions.
```

**Comparison with # shortcut:**
- **# shortcut:** Quick one-liner additions to memory (e.g., `# Always use TypeScript strict mode`)
- **/learn-pattern:** Structured, multi-step conversation that captures detailed patterns with formatting

Both modify CLAUDE.md, but the command provides a workflow for complex knowledge capture.

## Advanced Topics

### File References and @ Syntax

The `@` symbol includes file or directory contents in your command context:

**File reference:**
```bash
> /review @src/auth/login.js
# Includes full file content
```

**Multiple files:**
```bash
> /compare @src/v1/api.js @src/v2/api.js
```

**Directory reference:**
```bash
> /analyze @src/components/
# Includes directory listing, not contents
```

**MCP resource reference:**
```bash
> /analyze @github:repos/myorg/myrepo/issues
# Fetches data from MCP server
```

**Key behaviors:**
- File paths can be relative or absolute
- `@` references automatically add parent CLAUDE.md files to context
- Directory references show structure only (use Read tool for contents)

### Bash Command Integration

Execute bash commands within slash commands using `!` prefix:

**Security considerations:**
```markdown
---
allowed-tools: Bash(git:*), Bash(npm:test)  # Explicitly allow commands
---

Safe: !`git status`
Safe: !`npm test`
Blocked: !`rm -rf /`  # Not in allowed-tools
```

**Limitations:**
- Commands with `:` in arguments may fail parsing
- Use `allowed-tools: Bash` to allow all commands (risky)
- Output included in context (watch for large outputs)

**Best practices:**
- Always specify `allowed-tools` with specific command patterns
- Avoid commands with sensitive output (passwords, keys)
- Test commands manually first

### Namespacing with Subdirectories

Organize commands hierarchically:

```bash
.claude/commands/
├── frontend/
│   ├── component.md     # /component (project:frontend)
│   └── style.md         # /style (project:frontend)
├── backend/
│   ├── api.md           # /api (project:backend)
│   └── db.md            # /db (project:backend)
└── review.md            # /review (project)
```

**How namespacing works:**
- Command name comes from filename only (`component.md` → `/component`)
- Subdirectory appears in description ("project:frontend")
- Subdirectory does NOT affect command invocation

**Impact on /help output:**
```
/component - Generate React component (project:frontend)
/component - Generate Vue component (user)
/api - Create REST API endpoint (project:backend)
```

Multiple commands with the same filename can coexist if they're in different scopes (user vs. project) or different subdirectories.

### Thinking Mode Integration

Slash commands can trigger extended thinking for complex reasoning:

**Keywords that trigger extended thinking:**
- `think`, `think hard`, `think deeply`
- `analyze carefully`, `consider thoroughly`
- `reason about`, `evaluate options`

**Example command:**
```markdown
---
description: Architectural analysis with deep thinking
---

Think deeply about the architecture for $ARGUMENTS.

Consider:
- Scalability implications
- Security trade-offs
- Performance characteristics
- Maintenance complexity
- Cost factors

Provide a well-reasoned recommendation with alternatives.
```

**Configuration:**
- Set `MAX_THINKING_TOKENS` environment variable for extended thinking budget
- Use `Tab` in interactive mode to toggle thinking on/off
- Thinking appears as italic gray text before response

## Configuration Reference

### YAML Frontmatter Fields

| Field | Type | Purpose | Example |
|-------|------|---------|---------|
| `description` | string | Brief command description (shown in /help) | `Generate unit tests` |
| `argument-hint` | string | Argument format shown in autocomplete | `[issue-number] [priority]` |
| `model` | string | Override model for this command | `claude-3-5-haiku-20241022` |
| `allowed-tools` | string | Comma-separated tool permissions | `Bash(git:*), Read, Edit` |
| `disable-model-invocation` | boolean | Prevent SlashCommand tool from calling this | `true` |

### SlashCommand Tool Configuration

**Enable/disable the tool:**
```bash
# Disable all slash command invocations
/permissions
# Add to deny rules: SlashCommand
```

**Disable specific command:**
```markdown
---
disable-model-invocation: true
---
```

**Permission rules:**
```bash
# Allow only specific command
SlashCommand:/commit

# Allow command with any arguments
SlashCommand:/review:*
```

**Character budget:**
- Default: 15,000 characters for command descriptions
- Configure: `SLASH_COMMAND_TOOL_CHAR_BUDGET=25000`
- When exceeded: Subset of commands shown (warning in /context)

## Troubleshooting

**Command not appearing in /help:**
- Verify file location (`.claude/commands/` or `~/.claude/commands/`)
- Check filename extension is `.md`
- Ensure description is present (required for SlashCommand tool)
- Run `/help` to refresh command list

**Arguments not substituting:**
- Verify you're using `$ARGUMENTS`, `$1`, `$2` (not `{arg1}`)
- Check for typos in placeholder syntax
- Test with simple static text first

**Bash commands failing:**
- Add `allowed-tools` frontmatter with specific commands
- Check command syntax (avoid special characters in arguments)
- Test command manually in terminal first
- Review command output for errors

**Permission denied errors:**
- Verify `allowed-tools` includes required tools
- Check `/permissions` for deny rules blocking the tool
- Ensure you're not in plan mode (plan mode blocks execution)

**Command executes but produces unexpected results:**
- Check if CLAUDE.md memory is conflicting with command
- Verify file references (@) are pointing to correct paths
- Test with `--verbose` flag to see full prompt expansion
- Review recent /compact operations (may have lost context)

## Best Practices

**Command design:**
- Start with clear, specific instructions
- Use structured checklists for multi-step processes
- Include examples in complex commands
- Specify output format when needed

**Organization:**
- Use project commands (`.claude/commands/`) for team-shared workflows
- Use personal commands (`~/.claude/commands/`) for individual preferences
- Group related commands in subdirectories
- Name files descriptively (filename becomes command name)

**Security:**
- Always specify `allowed-tools` when using bash execution
- Avoid commands that expose sensitive data (API keys, passwords)
- Test commands in safe environment first
- Review bash output before including in prompts

**Performance:**
- Keep bash command output concise (large outputs consume tokens)
- Use file references (@) instead of pasting content
- Leverage /compact to manage conversation size
- Consider subagents for complex, context-heavy tasks

**Maintenance:**
- Document complex commands with comments
- Version control `.claude/commands/` for team sharing
- Regularly review and update command descriptions
- Remove obsolete commands to reduce clutter

## References

### Source Documentation

All information in this tutorial is directly sourced from official Claude Code documentation:

1. **CLI Documentation**
   - `/docs/claude-code/slash-commands.md` - Built-in and custom slash command reference
   - `/docs/claude-code/common-workflows.md` - Practical workflow examples
   - `/docs/claude-code/cli-reference.md` - Command-line flags and options
   - `/docs/claude-code/interactive-mode.md` - Interactive session shortcuts
   - `/docs/claude-code/memory.md` - CLAUDE.md memory system
   - `/docs/claude-code/hooks.md` - Hook system for automation

2. **Agent SDK Documentation**
   - `/api/agent-sdk/slash-commands.md` - SDK slash command integration
   - `/api/agent-sdk/overview.md` - SDK fundamentals and architecture
   - `/api/agent-sdk/typescript.md` - TypeScript SDK reference

### Quick Reference Table

| Topic | Primary Documentation File |
|-------|---------------------------|
| Built-in commands | `/docs/claude-code/slash-commands.md` |
| Creating custom commands | `/docs/claude-code/slash-commands.md` |
| Arguments and variables | `/docs/claude-code/slash-commands.md` |
| Bash execution | `/docs/claude-code/slash-commands.md` |
| File references | `/docs/claude-code/common-workflows.md` |
| Sub-agents integration | `/docs/claude-code/sub-agents.md` |
| Hooks integration | `/docs/claude-code/hooks.md`, `/docs/claude-code/hooks-guide.md` |
| Headless mode | `/docs/claude-code/headless.md`, `/docs/claude-code/sdk/sdk-headless.md` |
| Memory system | `/docs/claude-code/memory.md` |
| GitHub Actions | `/docs/claude-code/github-actions.md` |
| GitLab CI/CD | `/docs/claude-code/gitlab-ci-cd.md` |
| SlashCommand tool | `/docs/claude-code/slash-commands.md` |
| SDK integration | `/api/agent-sdk/slash-commands.md` |

## Next Steps

Now that you've mastered slash commands, explore these related topics:

**Advanced Claude Code features:**
- [Sub-agents](/docs/claude-code/sub-agents.md) - Specialized AI assistants for complex tasks
- [Hooks](/docs/claude-code/hooks-guide.md) - Automated workflows triggered by events
- [Memory system](/docs/claude-code/memory.md) - Persistent instructions across sessions

**Automation and integration:**
- [GitHub Actions](/docs/claude-code/github-actions.md) - CI/CD integration with Claude Code
- [Headless mode](/docs/claude-code/headless.md) - Non-interactive programmatic usage
- [MCP integration](/docs/claude-code/mcp.md) - Extend with Model Context Protocol

**SDK development:**
- [Agent SDK overview](/api/agent-sdk/overview.md) - Build production AI agents
- [TypeScript SDK](/api/agent-sdk/typescript.md) - Complete API reference
- [Python SDK](/api/agent-sdk/python.md) - Python agent development

**Team collaboration:**
- [Settings](/docs/claude-code/settings.md) - Configuration management
- [Permissions](/docs/claude-code/iam.md) - Access control and security
- [Analytics](/docs/claude-code/analytics.md) - Usage tracking and insights