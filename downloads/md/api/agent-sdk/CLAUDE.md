# Directory: agent-sdk

## Overview
This directory contains comprehensive documentation for the Claude Agent SDK, covering both TypeScript and Python implementations, configuration options, and advanced features for building production-ready AI agents.

## Files in This Directory

### **cost-tracking.md**
- Detailed guidance on tracking token usage and costs across SDK interactions
- Explains message-level usage reporting and how messages with the same ID share identical usage data
- Best practice: charge once per step (unique message ID) rather than per individual message
- Provides implementation examples including CostTracker and BillingAggregator classes
- Covers edge cases like output token discrepancies and cache token tracking
- Usage fields reference: input_tokens, output_tokens, cache tokens, service_tier, and total_cost_usd

### **custom-tools.md**
- Guide for extending Claude Code capabilities through in-process MCP servers
- Creating tools using `createSdkMcpServer` and `tool` helper functions with Zod schema validation
- Tool naming convention: `mcp__{server_name}__{tool_name}` (e.g., `mcp__my-custom-tools__get_weather`)
- Important: Custom MCP tools require streaming input mode (async generator/iterable for prompt parameter)
- Includes error handling patterns and example tools (database queries, API gateway, calculator)
- Type safety with Zod schemas for runtime validation and TypeScript type inference

### **mcp.md**
- Model Context Protocol (MCP) server configuration and usage in the SDK
- Three transport types: stdio (external processes via stdin/stdout), HTTP/SSE (remote servers), and SDK (in-process)
- Configuration via `.mcp.json` at project root or programmatically in SDK options
- Resource management: servers can expose resources that Claude can list and read
- Authentication patterns including environment variable substitution and OAuth2 status
- Error handling for connection failures and server status monitoring

### **modifying-system-prompts.md**
Four methods for customizing Claude's behavior: CLAUDE.md files (project-level persistent instructions loaded via `settingSources: ['project']`), output styles (saved configurations as markdown files in `.claude/output-styles`), system prompt with append (using `claude_code` preset with additional instructions), and fully custom prompts. CLAUDE.md files are NOT automatically loaded by the `claude_code` preset - you must explicitly set `settingSources` to load them. Each approach serves different use cases from persistent project guidelines to session-specific customization.

### **overview.md**
- Introduction to the Claude Agent SDK (formerly Claude Code SDK) with installation instructions
- Three SDK options: TypeScript, Python, and streaming vs single mode guidance
- Key benefits: context management, rich tool ecosystem, advanced permissions, production essentials, optimized Claude integration
- Authentication via ANTHROPIC_API_KEY, Amazon Bedrock, or Google Vertex AI
- Full Claude Code feature support: subagents, hooks, slash commands, and CLAUDE.md memory
- Important: CLAUDE.md files require explicit `settingSources: ['project']` configuration to load

### **permissions.md**
- Four complementary permission control methods: Permission Modes (global settings: default, plan, acceptEdits, bypassPermissions), canUseTool callback (runtime handler for uncovered cases), Hooks (fine-grained control over every tool execution), and Permission rules in settings.json (declarative allow/deny with bash command parsing)
- Permission flow: PreToolUse Hook → Ask Rules → Deny Rules → Permission Mode Check → Allow Rules → canUseTool Callback → PostToolUse Hook
- Mode-specific behaviors: acceptEdits auto-approves file edits, bypassPermissions skips all checks (use with caution)
- Permission modes can be set initially or changed dynamically during streaming sessions via `setPermissionMode()`
- Best practice: layer defenses by combining modes, rules, hooks, and callbacks for critical applications

### **python.md**
- Complete Python SDK reference with two interaction patterns: `query()` function (creates new session each time, simpler) and `ClaudeSDKClient` class (maintains conversation across exchanges, supports interrupts, hooks, and custom tools)
- Comprehensive type documentation: ClaudeAgentOptions with 40+ configuration fields, message types (UserMessage, AssistantMessage, SystemMessage, ResultMessage), content blocks, and hook types
- Tool creation: `@tool` decorator for defining MCP tools with type safety, `create_sdk_mcp_server()` for bundling tools
- Context manager support: `async with ClaudeSDKClient() as client` for automatic connection management
- Complete tool input/output schemas for all built-in tools (Task, Bash, Edit, Read, Write, Glob, Grep, etc.)
- SettingSource control: defaults to no filesystem settings unless explicitly configured

### **sessions.md**
- Session management for maintaining conversation state across multiple interactions
- Capturing session IDs from initial system init message for later resumption
- Resuming sessions via `resume` option with session ID to continue previous conversations
- Forking sessions: `forkSession: true` creates new branch from resume point, preserving original session
- Use cases for forking: exploring different approaches, testing changes, maintaining separate conversation paths
- Session behavior comparison table: same ID vs new ID, history appending vs branching

### **slash-commands.md**
- Built-in slash commands: `/compact` (reduces conversation history while preserving context), `/clear` (starts fresh conversation)
- Discovering available commands via system init message's `slash_commands` field
- Creating custom commands as markdown files in `.claude/commands/` (project) or `~/.claude/commands/` (personal)
- Advanced features: arguments with placeholders ($1, $2), bash command execution (!`command`), file references (@filename)
- YAML frontmatter options: allowed-tools, description, model, argument-hint
- Organization with subdirectories for namespacing and practical examples (code-review, test runner commands)

### **streaming-vs-single-mode.md**
Two input modes: Streaming Input Mode (default & recommended) providing persistent interactive sessions with image uploads, queued messages, full tool integration, hooks support, real-time feedback, and context persistence; Single Message Input for one-shot queries without images, hooks, or dynamic queueing. Streaming mode is preferred for production applications as it enables rich, interactive experiences with the agent operating as a long-lived process handling interruptions, permission requests, and session management.

### **subagents.md**
- Specialized AIs orchestrated by main agent for context management and parallelization
- Two definition methods: programmatically via `agents` parameter (recommended for SDK) or filesystem-based (`.claude/agents/*.md`)
- AgentDefinition fields: description (when to use), prompt (system instructions), tools (optional restrictions), model (optional override)
- Benefits: separate context prevents overload, concurrent execution speeds up workflows, specialized instructions per agent, tool restrictions reduce risks
- Common tool combinations: read-only (Read, Grep, Glob), test execution (Bash, Read, Grep), code modification (Read, Edit, MultiEdit, Write)
- Programmatic agents override filesystem-based agents with same name

### **todo-tracking.md**
- Built-in todo functionality for organizing complex workflows and displaying progress
- Todo lifecycle: created as pending → activated to in_progress → completed → removed when all done
- Automatically used for: complex multi-step tasks (3+ actions), user-provided task lists, non-trivial operations, explicit requests
- Monitoring via TodoWrite tool messages in the message stream
- Examples include TodoTracker class for real-time progress display with status icons and completion tracking
- Todo structure: content (imperative form), status (pending/in_progress/completed), activeForm (present continuous form)

### **typescript.md**
- Complete TypeScript SDK reference: `query()` function (primary interface returning async generator), `tool()` for creating MCP tools with Zod schemas, `createSdkMcpServer()` for bundling tools
- Options type with 40+ configuration fields including systemPrompt, agents, allowedTools, hooks, permissionMode, settingSources
- Query interface extends AsyncGenerator with `interrupt()` and `setPermissionMode()` methods for dynamic control
- Message types: SDKAssistantMessage, SDKUserMessage, SDKResultMessage, SDKSystemMessage, SDKPartialAssistantMessage, SDKCompactBoundaryMessage
- Comprehensive hook system with 8 events (PreToolUse, PostToolUse, Notification, UserPromptSubmit, SessionStart, SessionEnd, Stop, SubagentStop, PreCompact)
- Complete tool input/output type definitions for all 15+ built-in tools with detailed interfaces
- SettingSource defaults to empty array (no filesystem settings) unless explicitly configured
