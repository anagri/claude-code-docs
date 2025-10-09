# Claude Code Sub-Agents: A Hands-On Tutorial

> **Target Audience:** Intermediate Claude Code CLI users who want to leverage specialized AI assistants for complex workflows

## Introduction

This tutorial provides a comprehensive, hands-on guide to Claude Code sub-agents - specialized AI assistants that enhance your development workflow through task-specific configurations and separate context windows. By the end of this tutorial, you'll understand:

- What sub-agents are and why they matter
- How to create and configure sub-agents
- Real-world use cases and implementation patterns
- Best practices for production usage

## What Are Sub-Agents?

Sub-agents are pre-configured AI personalities that Claude Code can delegate tasks to. Think of them as specialized team members - each with specific expertise, their own workspace, and tailored permissions.


### Key Characteristics

Each sub-agent has:

1. **Specific Purpose** - A well-defined expertise area (code review, testing, debugging, etc.)
2. **Independent Context** - Its own context window separate from the main conversation
3. **Custom Tools** - Configurable tool access based on its responsibilities
4. **Specialized Prompt** - Custom system prompt guiding its behavior

When Claude Code encounters a task matching a sub-agent's expertise, it can delegate that task to the specialized sub-agent, which works independently and returns results.


## Key Benefits

### Context Preservation

Each sub-agent operates in its own context, preventing pollution of the main conversation and keeping it focused on high-level objectives.

**Example:** A research-assistant sub-agent can explore dozens of files and documentation pages without cluttering the main conversation with all the intermediate search results - only returning the relevant findings.


### Specialized Expertise

Sub-agents can be fine-tuned with detailed instructions for specific domains, leading to higher success rates on designated tasks.

**Example:** A database-migration sub-agent can have detailed knowledge about SQL best practices, rollback strategies, and data integrity checks that would be unnecessary noise in the main agent's instructions.


### Reusability

Once created, sub-agents can be used across different projects and shared with your team for consistent workflows.


### Flexible Permissions

Each sub-agent can have different tool access levels, allowing you to limit powerful tools to specific sub-agent types.

**Example:** A doc-reviewer sub-agent might only have access to Read and Grep tools, ensuring it can analyze but never accidentally modify your documentation files.


## Quick Start (5 minutes)

Let's create your first sub-agent - a simple code reviewer.

### Step 1: Open the Sub-agents Interface

In your Claude Code session, run:

```bash
/agents
```


### Step 2: Select 'Create New Agent'

Choose whether to create a **project-level** or **user-level** sub-agent:

- **Project-level** (`.claude/agents/`) - Available in current project, shared with team
- **User-level** (`~/.claude/agents/`) - Available across all your projects


### Step 3: Define the Sub-agent

**Recommended Approach:** Generate with Claude first, then customize. The interface will:

1. Ask you to describe your sub-agent in detail
2. Let you specify when it should be used
3. Show all available tools for you to select (or leave blank to inherit all)
4. Generate a complete sub-agent definition
5. Allow editing in your preferred editor (press `e`)


### Step 4: Save and Use

Your sub-agent is now available! Claude will use it automatically when appropriate, or you can invoke it explicitly:

```bash
> Use the code-reviewer subagent to check my recent changes
```


## Anatomy of a Sub-Agent File

Sub-agents are stored as Markdown files with YAML frontmatter. Understanding this structure is key to creating effective sub-agents.

### File Location

| Type | Location | Scope | Priority |
|------|----------|-------|----------|
| **Project sub-agents** | `.claude/agents/` | Available in current project | Highest |
| **User sub-agents** | `~/.claude/agents/` | Available across all projects | Lower |

When sub-agent names conflict, project-level sub-agents take precedence over user-level sub-agents.


### File Format

Each sub-agent file has this structure:

```markdown
---
name: your-sub-agent-name
description: Description of when this subagent should be invoked
tools: tool1, tool2, tool3  # Optional - inherits all tools if omitted
model: sonnet  # Optional - specify model alias or 'inherit'
---

Your subagent's system prompt goes here. This can be multiple paragraphs
and should clearly define the subagent's role, capabilities, and approach
to solving problems.

Include specific instructions, best practices, and any constraints
the subagent should follow.
```


### Configuration Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier using lowercase letters and hyphens |
| `description` | Yes | Natural language description of the subagent's purpose |
| `tools` | No | Comma-separated list of specific tools. If omitted, inherits all tools from the main thread |
| `model` | No | Model to use for this subagent. Can be a model alias (`sonnet`, `opus`, `haiku`) or `'inherit'` to use the main conversation's model. If omitted, defaults to the configured subagent model |


### Model Selection

The `model` field allows fine-grained control:

- **Model alias**: Use `sonnet`, `opus`, or `haiku` for specific models
- **`'inherit'`**: Use the same model as the main conversation (useful for consistency)
- **Omitted**: Uses the default model configured for subagents (`sonnet`)

Using `'inherit'` is particularly useful when you want your sub-agents to adapt to the model choice of the main conversation, ensuring consistent capabilities and response style throughout your session.


## Hands-On Exercises

### Exercise 1: Your First Sub-Agent - Simple Logger

Let's create a basic sub-agent that logs bash commands for audit purposes.

**Create the file:** `.claude/agents/bash-logger.md`

```markdown
---
name: bash-logger
description: Use proactively to log all bash commands executed during the session
tools: Bash, Write
model: haiku
---

You are a command logging specialist. Your sole responsibility is to:

1. Execute the requested bash command
2. Log the command and its output to a file called `.command-log.txt`
3. Return the command output to the user

Always append to the log file with timestamps. Format:
```
[YYYY-MM-DD HH:MM:SS] Command: <command>
Output:
<output>
---
```

Never modify files other than the log file.
```

**Test it:**

```bash
> Use the bash-logger subagent to list files in the current directory
```

**Expected behavior:** The sub-agent will execute `ls`, log the command to `.command-log.txt`, and return the output.


### Exercise 2: Tool Restrictions - Read-Only Analyzer

Create a sub-agent that can analyze code but never modify it.

**Create the file:** `.claude/agents/code-analyzer.md`

```markdown
---
name: code-analyzer
description: Static code analysis and architecture review. Use proactively after major changes to analyze code structure without making modifications.
tools: Read, Grep, Glob
model: inherit
---

You are a code architecture analyst. Analyze code structure, identify patterns, and suggest improvements without making changes.

When analyzing:
1. Use Grep to search for patterns
2. Use Glob to find related files
3. Use Read to examine specific files
4. Identify architectural patterns
5. Suggest improvements (but never implement them)

Focus areas:
- Code organization and structure
- Design patterns usage
- Potential coupling issues
- Modularity and separation of concerns
- Code smells and anti-patterns

Present findings in a clear report with:
- Summary of architecture
- Identified patterns
- Recommendations (prioritized)
- Examples from the codebase
```

**Test it:**

```bash
> Use the code-analyzer subagent to review our authentication module
```

**Expected behavior:** The sub-agent will analyze files using only Read, Grep, and Glob - it cannot use Edit or Write tools.


### Exercise 3: Model Selection - Fast Triage Agent

Create a sub-agent that uses Haiku for quick issue triage.

**Create the file:** `.claude/agents/issue-triager.md`

```markdown
---
name: issue-triager
description: Quick triage of bug reports and issues. Use PROACTIVELY when new issues are reported to categorize and prioritize them.
tools: Read, Grep
model: haiku
---

You are a rapid issue triage specialist using the fast Haiku model for efficiency.

For each issue:
1. Read the issue description
2. Search for related code using Grep
3. Categorize: [BUG, FEATURE, ENHANCEMENT, QUESTION]
4. Assign severity: [CRITICAL, HIGH, MEDIUM, LOW]
5. Suggest initial investigation steps

Output format:
```
Category: [category]
Severity: [severity]
Related files: [list]
Investigation steps:
1. [step]
2. [step]
```

Keep analysis concise - this is triage, not deep debugging.
```

**Test it:**

```bash
> Use the issue-triager subagent to analyze the bug report in issue-123.md
```

**Expected behavior:** Fast response using Haiku model for quick categorization.


### Exercise 4: Automatic Delegation - Proactive Test Runner

Create a sub-agent that Claude automatically invokes after code changes.

**Create the file:** `.claude/agents/test-runner.md`

```markdown
---
name: test-runner
description: Use PROACTIVELY to run tests and fix failures. MUST BE USED after any code changes to verify functionality.
tools: Bash, Read, Edit
---

You are a test automation expert. When you see code changes, proactively run the appropriate tests.

Workflow:
1. Detect which files were modified
2. Identify relevant test files
3. Run appropriate test command (npm test, pytest, etc.)
4. If tests fail:
   a. Analyze the failure
   b. Fix the issue
   c. Re-run tests
   d. Repeat until all tests pass
5. Report results

Test commands by framework:
- JavaScript/TypeScript: `npm test` or `yarn test`
- Python: `pytest` or `python -m pytest`
- Go: `go test ./...`
- Rust: `cargo test`

When fixing failures:
- Preserve the original test intent
- Fix implementation, not tests (unless tests are wrong)
- Explain what was broken and how you fixed it

Never skip failing tests - fix them.
```

**Test it:**

```bash
> Modify the calculateTotal function in utils.js to add two numbers instead of multiplying them
```

**Expected behavior:** After making the change, Claude should automatically invoke the test-runner sub-agent to run tests and fix any failures.


## Real-World Use Cases

Here are complete, production-ready sub-agent examples for common development scenarios.

### Use Case 1: Comprehensive Code Reviewer

**File:** `.claude/agents/code-reviewer.md`

```markdown
---
name: code-reviewer
description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
tools: Read, Grep, Glob, Bash
model: inherit
---

You are a senior code reviewer ensuring high standards of code quality and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately

Review checklist:
- Code is simple and readable
- Functions and variables are well-named
- No duplicated code
- Proper error handling
- No exposed secrets or API keys
- Input validation implemented
- Good test coverage
- Performance considerations addressed

Provide feedback organized by priority:
- Critical issues (must fix)
- Warnings (should fix)
- Suggestions (consider improving)

Include specific examples of how to fix issues.
```

**Usage:**

```bash
> Use the code-reviewer subagent to check my recent changes
```


### Use Case 2: Debugging Specialist

**File:** `.claude/agents/debugger.md`

```markdown
---
name: debugger
description: Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues.
tools: Read, Edit, Bash, Grep, Glob
---

You are an expert debugger specializing in root cause analysis.

When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Implement minimal fix
5. Verify solution works

Debugging process:
- Analyze error messages and logs
- Check recent code changes
- Form and test hypotheses
- Add strategic debug logging
- Inspect variable states

For each issue, provide:
- Root cause explanation
- Evidence supporting the diagnosis
- Specific code fix
- Testing approach
- Prevention recommendations

Focus on fixing the underlying issue, not just symptoms.
```

**Usage:**

```bash
> Have the debugger subagent investigate this error: TypeError: Cannot read property 'id' of undefined
```


### Use Case 3: Data Science Specialist

**File:** `.claude/agents/data-scientist.md`

```markdown
---
name: data-scientist
description: Data analysis expert for SQL queries, BigQuery operations, and data insights. Use proactively for data analysis tasks and queries.
tools: Bash, Read, Write
model: sonnet
---

You are a data scientist specializing in SQL and BigQuery analysis.

When invoked:
1. Understand the data analysis requirement
2. Write efficient SQL queries
3. Use BigQuery command line tools (bq) when appropriate
4. Analyze and summarize results
5. Present findings clearly

Key practices:
- Write optimized SQL queries with proper filters
- Use appropriate aggregations and joins
- Include comments explaining complex logic
- Format results for readability
- Provide data-driven recommendations

For each analysis:
- Explain the query approach
- Document any assumptions
- Highlight key findings
- Suggest next steps based on data

Always ensure queries are efficient and cost-effective.
```

**Usage:**

```bash
> Ask the data-scientist subagent to analyze user engagement trends from our analytics database
```


### Use Case 4: Security Auditor

**File:** `.claude/agents/security-auditor.md`

```markdown
---
name: security-auditor
description: Security review specialist. MUST BE USED before deploying code changes to production. Focuses on vulnerabilities, secrets, and security best practices.
tools: Read, Grep, Glob, Bash
model: opus
---

You are a security auditor specializing in application security.

Security checklist:
1. **Secrets Detection**
   - API keys, tokens, passwords
   - Database credentials
   - Private keys and certificates
   - Check .env files and config

2. **Input Validation**
   - SQL injection vulnerabilities
   - XSS attack vectors
   - Command injection risks
   - File upload vulnerabilities

3. **Authentication & Authorization**
   - Proper session management
   - Password hashing (bcrypt, Argon2)
   - JWT token validation
   - Role-based access control

4. **Data Protection**
   - Sensitive data encryption
   - HTTPS enforcement
   - Secure cookie settings
   - CORS configuration

5. **Dependencies**
   - Known vulnerable packages
   - Outdated dependencies
   - License compliance

Output format:
```
SECURITY AUDIT REPORT

CRITICAL FINDINGS: [count]
[list with file:line]

HIGH PRIORITY: [count]
[list with file:line]

MEDIUM PRIORITY: [count]
[list with file:line]

RECOMMENDATIONS:
[prioritized list]
```

Use `grep -r` to search for common vulnerability patterns.
```

**Usage:**

```bash
> Use the security-auditor subagent to review the authentication module before deployment
```


### Use Case 5: Documentation Generator

**File:** `.claude/agents/doc-writer.md`

```markdown
---
name: doc-writer
description: Technical documentation specialist. Use proactively after implementing new features or APIs to generate comprehensive documentation.
tools: Read, Write, Grep, Glob
model: sonnet
---

You are a technical writer specializing in developer documentation.

When documenting code:
1. Read the implementation
2. Understand the public API
3. Identify use cases
4. Write clear, structured documentation

Documentation structure:
```markdown
# [Component/Module Name]

## Overview
[Brief description of purpose]

## Installation
[If applicable]

## Quick Start
[Simplest usage example]

## API Reference
[Detailed method/function documentation]

## Examples
[Common use cases with code]

## Advanced Usage
[Edge cases and advanced patterns]

## Troubleshooting
[Common issues and solutions]
```

Best practices:
- Start with working code examples
- Use consistent terminology
- Include edge cases
- Add troubleshooting sections
- Keep examples runnable

For each function/method document:
- Purpose and behavior
- Parameters with types
- Return value
- Exceptions/errors
- Code example
```

**Usage:**

```bash
> Have the doc-writer subagent create documentation for the new authentication API
```


### Use Case 6: Performance Optimizer

**File:** `.claude/agents/performance-optimizer.md`

```markdown
---
name: performance-optimizer
description: Performance optimization specialist. Use PROACTIVELY when code changes might impact performance. Analyzes bottlenecks and suggests optimizations.
tools: Read, Edit, Bash, Grep, Glob
model: sonnet
---

You are a performance optimization expert focusing on profiling and improvements.

Optimization workflow:
1. **Profile the code**
   - Identify hot paths
   - Measure execution time
   - Find memory bottlenecks

2. **Analyze patterns**
   - N+1 query problems
   - Unnecessary loops
   - Inefficient algorithms
   - Memory leaks

3. **Implement fixes**
   - Cache frequently accessed data
   - Optimize database queries
   - Use efficient data structures
   - Implement lazy loading

4. **Measure impact**
   - Run benchmarks before/after
   - Document performance gains
   - Verify correctness maintained

Tools and techniques:
- Python: cProfile, line_profiler, memory_profiler
- JavaScript: console.time(), Performance API
- Database: EXPLAIN queries, query plans
- Bash: time command for benchmarking

Output format:
```
PERFORMANCE ANALYSIS

Bottlenecks Found: [count]
1. [description] - File: [file:line]
   Impact: [HIGH/MEDIUM/LOW]
   Fix: [description]

2. [...]

Optimizations Applied:
1. [description]
   Before: [metric]
   After: [metric]
   Improvement: [percentage]
```

Always benchmark before and after changes.
```

**Usage:**

```bash
> Use the performance-optimizer subagent to analyze the data processing pipeline
```


## User vs Project Sub-Agents

Understanding the difference between user-level and project-level sub-agents is crucial for effective organization and team collaboration.

### Scoping Differences

| Aspect | User Sub-agents (`~/.claude/agents/`) | Project Sub-agents (`.claude/agents/`) |
|--------|---------------------------------------|---------------------------------------|
| **Scope** | Available across all your projects | Available only in the current project |
| **Sharing** | Personal to you | Shared with team via version control |
| **Priority** | Lower priority when names conflict | Higher priority (overrides user-level) |
| **Use Case** | Personal preferences and workflows | Team-shared standards and processes |


### When to Use User-Level Sub-agents

**Personal productivity tools:**

```bash
# Example: Personal note-taker
~/.claude/agents/my-notes.md
```

**Individual coding preferences:**

```bash
# Example: Your preferred code style enforcer
~/.claude/agents/my-style-checker.md
```

**Cross-project utilities:**

```bash
# Example: Git commit message formatter
~/.claude/agents/commit-formatter.md
```

### When to Use Project-Level Sub-agents

**Team coding standards:**

```bash
# Example: Project-specific code review rules
.claude/agents/project-reviewer.md
```

**Project-specific workflows:**

```bash
# Example: Deployment checklist for this project
.claude/agents/deploy-checker.md
```

**Domain-specific experts:**

```bash
# Example: Healthcare compliance checker for medical app
.claude/agents/hipaa-auditor.md
```

### Version Control Best Practice

Project sub-agents should be checked into version control so your team can benefit from and improve them collaboratively.

```bash
# Add project sub-agents to git
git add .claude/agents/
git commit -m "Add team sub-agents for code review and testing"
```


## CLI Integration

Sub-agents can be defined dynamically using CLI flags for quick testing or automation scripts.

### The --agents Flag

Define sub-agents via JSON without creating files:

```bash
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```


### Priority Hierarchy

CLI-defined sub-agents have **medium priority**:

1. **Highest**: Project-level sub-agents (`.claude/agents/`)
2. **Medium**: CLI-defined sub-agents (`--agents` flag)
3. **Lowest**: User-level sub-agents (`~/.claude/agents/`)


### Use Cases for CLI Sub-agents

**Quick testing:**

```bash
# Test a sub-agent configuration before creating a file
claude --agents '{"tester": {"description": "Test runner", "prompt": "Run tests", "tools": ["Bash"]}}'
```

**Session-specific sub-agents:**

```bash
# One-time sub-agent for a specific task
claude --agents '{"migrator": {"description": "Database migration helper", "prompt": "Help with DB migrations"}}'
```

**Automation scripts:**

```bash
#!/bin/bash
# CI/CD script with custom sub-agent
claude --agents '{
  "ci-checker": {
    "description": "CI/CD validation",
    "prompt": "Verify code passes all CI checks",
    "tools": ["Bash", "Read"]
  }
}' -p "Run CI checks"
```

**Documentation sharing:**

```bash
# Share sub-agent definition in documentation
# Users can copy-paste the --agents JSON
```


### Complete CLI Flag Format

```bash
claude --agents '{
  "agent-name": {
    "description": "string (required) - When to invoke this agent",
    "prompt": "string (required) - System prompt for the agent",
    "tools": ["Tool1", "Tool2"],  // optional array
    "model": "sonnet"  // optional: sonnet, opus, haiku, inherit
  }
}'
```


## Advanced Topics

### Chaining Sub-agents

For complex workflows, you can chain multiple sub-agents:

```bash
> First use the code-analyzer subagent to find performance issues, then use the optimizer subagent to fix them
```

This creates a sequential workflow where:
1. `code-analyzer` identifies issues (read-only)
2. `optimizer` implements fixes (read-write)


### Dynamic Sub-agent Selection

Claude Code intelligently selects sub-agents based on:
- Task description in your request
- The `description` field in sub-agent configurations
- Current context and available tools

**Tips for better automatic selection:**

1. **Use action-oriented descriptions:**
   ```markdown
   description: Use PROACTIVELY to run tests after code changes
   ```

2. **Include trigger keywords:**
   ```markdown
   description: MUST BE USED for security review before deployment
   ```

3. **Be specific about when:**
   ```markdown
   description: Use immediately after writing or modifying code
   ```


### Working with CLAUDE.md

Sub-agents can leverage project-specific context from CLAUDE.md files:

```markdown
# .claude/CLAUDE.md

## Coding Standards
- Use TypeScript strict mode
- Prefer functional programming
- Maximum line length: 80 characters

## Testing Requirements
- All public functions must have tests
- Use Jest for unit tests
- Minimum 80% code coverage
```

Sub-agents automatically see this context, making them project-aware.


### MCP Tools and Sub-agents

Sub-agents can access MCP (Model Context Protocol) tools from configured servers.

**Inheritance behavior:**
- If `tools` field is **omitted**: Sub-agent inherits all MCP tools from main thread
- If `tools` field is **specified**: List individual MCP tools by name

**MCP tool naming:**
```
mcp__{server-name}__{tool-name}
```

Example configuration:

```markdown
---
name: database-expert
description: Database operations specialist
tools: mcp__postgres__execute_query, mcp__postgres__get_schema, Read
---

You are a database expert with access to PostgreSQL tools.
```


### Output Styles Integration

Sub-agents are distinct from output styles:

| Feature | Sub-agents | Output Styles |
|---------|-----------|---------------|
| **Scope** | Task-specific invocation | Main agent loop behavior |
| **Settings** | Model, tools, prompt | System prompt only |
| **Context** | Separate context window | Same context as main |
| **Use Case** | Specialized tasks | Change overall behavior |

You can combine both: use an output style for the main conversation, and sub-agents for specific tasks.


### Performance Considerations

**Context efficiency:**
- Sub-agents preserve main context by working in isolation
- Enables longer overall sessions without hitting context limits

**Latency:**
- Sub-agents start with a clean slate each invocation
- May add latency as they gather required context
- Balance specialization benefits vs. startup overhead


## How Sub-Agents Work (Under the Hood)

Understanding the internal mechanics helps you design better sub-agents.

### From File to Runtime

1. **Discovery Phase**
   - Claude Code scans `.claude/agents/` and `~/.claude/agents/`
   - Parses YAML frontmatter and system prompts
   - Builds internal registry with priority ordering

2. **Invocation Decision**
   - User explicitly requests: "Use the X subagent..."
   - Claude matches task to sub-agent descriptions
   - Priority: Explicit > Automatic > None

3. **Execution**
   - New context window created
   - Sub-agent's system prompt applied
   - Tool access restricted to allowed set
   - Independent conversation with the sub-agent
   - Results returned to main agent

4. **Context Management**
   - Sub-agent context isolated from main
   - Only final results passed back
   - Main conversation continues with results


### AgentDefinition Mapping

When you create a sub-agent file, it maps to an internal `AgentDefinition`:

| File Field | AgentDefinition Field | Type | Required |
|------------|----------------------|------|----------|
| `name` | Key in agents map | string | Yes |
| `description` | `description` | string | Yes |
| System prompt body | `prompt` | string | Yes |
| `tools` | `tools` | string[] | No |
| `model` | `model` | enum | No |


### Tool Execution Flow

When a sub-agent uses a tool:

1. Sub-agent requests tool use (e.g., Read a file)
2. Permission system checks allowed tools for this sub-agent
3. If allowed: Tool executes, results returned to sub-agent
4. If denied: Error returned, sub-agent must adapt
5. Tool results stay in sub-agent context
6. Only final summary goes to main agent


## Configuration Reference

### Complete Frontmatter Options

```yaml
---
# REQUIRED FIELDS
name: agent-name                    # Lowercase, hyphens only
description: When to use this agent # Natural language

# OPTIONAL FIELDS
tools: Tool1, Tool2, Tool3         # Comma-separated, or omit to inherit all
model: sonnet                      # sonnet, opus, haiku, or 'inherit'
---
```


### Model Options

| Value | Behavior |
|-------|----------|
| `sonnet` | Latest Sonnet model (currently 4.5) |
| `opus` | Opus model (currently 4.1) |
| `haiku` | Fast, efficient Haiku model |
| `'inherit'` | Use same model as main conversation |
| Omitted | Default subagent model (sonnet) |


### Available Tools

Complete list of tools that can be specified in the `tools` field:

**File Operations:**
- `Read` - Read files
- `Write` - Create/overwrite files
- `Edit` - Make targeted edits
- `MultiEdit` - Multiple edits atomically
- `NotebookEdit` - Modify Jupyter notebooks

**Search & Discovery:**
- `Glob` - Pattern matching
- `Grep` - Content search
- `Task` - Launch sub-agents

**Execution:**
- `Bash` - Execute commands
- `BashOutput` - Get background command output
- `KillShell` - Terminate background shells

**Web:**
- `WebFetch` - Fetch URLs
- `WebSearch` - Search the web

**Utilities:**
- `SlashCommand` - Run custom slash commands
- `TodoWrite` - Manage task lists

**MCP Tools:**
- Any tool from configured MCP servers (named `mcp__{server}__{tool}`)


### Tool Combinations by Use Case

**Read-only analysis:**
```markdown
tools: Read, Grep, Glob
```

**Test execution:**
```markdown
tools: Bash, Read, Grep
```

**Code modification:**
```markdown
tools: Read, Edit, MultiEdit, Write, Grep, Glob
```

**Web research:**
```markdown
tools: WebSearch, WebFetch, Read, Write
```


## Troubleshooting

### Common Issues

**Issue: Sub-agent not being invoked automatically**

Solution:
- Make description more specific and action-oriented
- Add trigger words: "use PROACTIVELY", "MUST BE USED"
- Try explicit invocation to test functionality
- Check that sub-agent file is in correct location


**Issue: Sub-agent can't access certain tools**

Solution:
- Verify tools are spelled correctly (case-sensitive)
- Check if tools field is comma-separated
- Remember: omitting tools field inherits ALL tools
- MCP tools require server to be connected


**Issue: Sub-agent using wrong model**

Solution:
- Check `model` field in frontmatter
- Verify model alias is correct (sonnet/opus/haiku)
- Use `'inherit'` (with quotes) to match main conversation
- Default is sonnet if field is omitted


**Issue: Conflicts between user and project sub-agents**

Solution:
- Project-level sub-agents ALWAYS take precedence
- Rename one of the conflicting sub-agents
- Use `/agents` command to see which is active
- Check priority: Project > CLI > User


**Issue: Sub-agent context seems limited**

Solution:
- Sub-agents start with clean context each time
- They may need to read files to build context
- Consider including key context in system prompt
- Latency is normal as they gather information


## Best Practices

### 1. Start with Claude-Generated Agents

Use `/agents` to have Claude generate initial sub-agent definitions, then customize them. This gives you:
- Solid foundation following best practices
- Proper structure and formatting
- Starting point for iteration


### 2. Design Focused Sub-agents

Create sub-agents with single, clear responsibilities rather than trying to make one sub-agent do everything.

**Good:**
```markdown
name: test-runner
description: Run tests and fix failures
```

**Bad:**
```markdown
name: code-helper
description: Help with code, tests, docs, deployment, and debugging
```


### 3. Write Detailed Prompts

Include specific instructions, examples, and constraints in system prompts. The more guidance you provide, the better the sub-agent will perform.

**Example of detailed prompt:**

```markdown
---
name: api-tester
description: Test API endpoints
---

You are an API testing specialist.

For each endpoint test:
1. Send HTTP request using curl or httpie
2. Verify status code (200, 201, 404, etc.)
3. Validate response structure matches schema
4. Check for proper error handling
5. Test edge cases (empty input, invalid data)

Response validation:
- JSON structure matches expected schema
- All required fields present
- Data types correct
- No unexpected fields

Report format:
```
ENDPOINT: [method] [url]
STATUS: [✓/✗] Expected [code], got [code]
RESPONSE: [✓/✗] Schema validation
EDGE CASES: [list of tests]
ISSUES: [any problems found]
```
```


### 4. Limit Tool Access

Only grant tools that are necessary for the sub-agent's purpose. This improves security and helps the sub-agent focus on relevant actions.

**Example:**

```markdown
# Documentation reviewer - read-only
tools: Read, Grep, Glob

# Test fixer - can modify tests
tools: Read, Edit, Bash

# Full-stack developer - all tools
tools: # Omit to inherit all
```


### 5. Version Control

Check project sub-agents into version control so your team can benefit from and improve them collaboratively.

```bash
# Standard practice
git add .claude/agents/
git commit -m "Add project sub-agents"
git push
```


### 6. Use Descriptive Names

Choose names that clearly indicate the sub-agent's purpose:

**Good:**
- `code-reviewer`
- `test-runner`
- `security-auditor`
- `performance-optimizer`

**Avoid:**
- `helper`
- `agent1`
- `my-agent`

### 7. Test Incrementally

Test sub-agents with simple tasks before relying on them for complex workflows:

1. Create basic sub-agent
2. Test with explicit invocation
3. Verify tool access works
4. Try automatic invocation
5. Refine description/prompt based on results
6. Add to team workflow

### 8. Document Sub-agent Purpose

Add comments in system prompts to help future maintainers:

```markdown
---
name: deployment-checker
description: Pre-deployment validation
---

# Purpose
# This sub-agent runs a comprehensive pre-deployment checklist
# for our production environment. It ensures all critical
# validations pass before allowing code to ship.

# Created: 2025-01-15
# Owner: DevOps team
# Last updated: 2025-01-20

You are a deployment validation specialist...
```

## References

This tutorial consulted the following source files:

### Core Documentation
1. `docs/claude-code/sub-agents.md` - Main sub-agents documentation
2. `docs/claude-code/common-workflows.md` - Using specialized subagents workflow
3. `docs/claude-code/slash-commands.md` - /agents command
4. `docs/claude-code/cli-reference.md` - --agents flag
5. `docs/claude-code/settings.md` - Tool configurations and subagent settings
6. `docs/claude-code/output-styles.md` - Comparison with output styles
7. `docs/claude-code/model-config.md` - Model selection options
8. `docs/claude-code/memory.md` - CLAUDE.md integration
9. `docs/claude-code/interactive-mode.md` - Using sub-agents interactively

### SDK Documentation
10. `api/agent-sdk/subagents.md` - SDK subagent concepts and benefits
11. `api/agent-sdk/overview.md` - SDK architecture
12. `api/agent-sdk/modifying-system-prompts.md` - System prompt customization
13. `api/agent-sdk/typescript.md` - TypeScript SDK insights
14. `api/agent-sdk/python.md` - Python SDK insights
15. `api/agent-sdk/streaming-vs-single-mode.md` - SDK operational modes

### Quick Reference Table

| Topic | Primary Reference |
|-------|------------------|
| Sub-agent basics | `docs/claude-code/sub-agents.md` |
| File format | `docs/claude-code/sub-agents.md` - File format section |
| Tool configuration | `docs/claude-code/settings.md` - Tools table |
| Model selection | `docs/claude-code/model-config.md` |
| CLI usage | `docs/claude-code/cli-reference.md` - --agents flag |
| Best practices | `docs/claude-code/sub-agents.md` - Best practices |
| SDK integration | `api/agent-sdk/subagents.md` |
| MCP integration | `docs/claude-code/sub-agents.md` - MCP tools |

## Next Steps

Now that you understand sub-agents, explore these related topics:

1. **Custom Slash Commands** - Create reusable prompts for common tasks
   - Reference: `docs/claude-code/slash-commands.md`

2. **CLAUDE.md Memory** - Provide persistent context to sub-agents
   - Reference: `docs/claude-code/memory.md`

3. **Hooks System** - Customize behavior at lifecycle points
   - Reference: `docs/claude-code/hooks-guide.md`

4. **MCP Integration** - Extend sub-agents with custom tools
   - Reference: `docs/claude-code/mcp.md`

5. **Agent SDK** - Build production agents programmatically
   - Reference: `api/agent-sdk/overview.md`

---

**Tutorial completed!** You now have comprehensive knowledge of Claude Code sub-agents, from basic concepts to production-ready implementations. Start by creating simple sub-agents and gradually build more sophisticated ones as you gain experience.
