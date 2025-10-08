url: https://docs.claude.com/en/api/agent-sdk/typescript

---

## Installation

Copy
[code]
    npm install @anthropic-ai/claude-agent-sdk

[/code]

## Functions

### query\(\)

The primary function for interacting with Claude Code. Creates an async generator that streams messages as they arrive.

Copy
[code]
    function query({
      prompt,
      options
    }: {
      prompt: string | AsyncIterable<SDKUserMessage>;
      options?: Options;
    }): Query

[/code]

#### Parameters

Parameter| Type| Description
---|---|---
`prompt`| `string | AsyncIterable<``SDKUserMessage``>`| The input prompt as a string or async iterable for streaming mode
`options`| `Options`| Optional configuration object \(see Options type below\)

#### Returns

Returns a `Query` object that extends `AsyncGenerator<``SDKMessage``, void>` with additional methods.

### tool\(\)

Creates a type-safe MCP tool definition for use with SDK MCP servers.

Copy
[code]
    function tool<Schema extends ZodRawShape>(
      name: string,
      description: string,
      inputSchema: Schema,
      handler: (args: z.infer<ZodObject<Schema>>, extra: unknown) => Promise<CallToolResult>
    ): SdkMcpToolDefinition<Schema>

[/code]

#### Parameters

Parameter| Type| Description
---|---|---
`name`| `string`| The name of the tool
`description`| `string`| A description of what the tool does
`inputSchema`| `Schema extends ZodRawShape`| Zod schema defining the tool’s input parameters
`handler`| `(args, extra) => Promise<``CallToolResult``>`| Async function that executes the tool logic

### createSdkMcpServer\(\)

Creates an MCP server instance that runs in the same process as your application.

Copy
[code]
    function createSdkMcpServer(options: {
      name: string;
      version?: string;
      tools?: Array<SdkMcpToolDefinition<any>>;
    }): McpSdkServerConfigWithInstance

[/code]

#### Parameters

Parameter| Type| Description
---|---|---
`options.name`| `string`| The name of the MCP server
`options.version`| `string`| Optional version string
`options.tools`| `Array<SdkMcpToolDefinition>`| Array of tool definitions created with `tool()`

## Types

### Options

Configuration object for the `query()` function. Property| Type| Default| Description
---|---|---|---
`abortController`| `AbortController`| `new AbortController()`| Controller for cancelling operations
`additionalDirectories`| `string[]`| `[]`| Additional directories Claude can access
`agents`| `Record<string, [`AgentDefinition`](#agentdefinition)>`| `undefined`| Programmatically define subagents
`allowedTools`| `string[]`| All tools| List of allowed tool names
`canUseTool`| `CanUseTool`| `undefined`| Custom permission function for tool usage
`continue`| `boolean`| `false`| Continue the most recent conversation
`cwd`| `string`| `process.cwd()`| Current working directory
`disallowedTools`| `string[]`| `[]`| List of disallowed tool names
`env`| `Dict<string>`| `process.env`| Environment variables
`executable`| `'bun' | 'deno' | 'node'`| Auto-detected| JavaScript runtime to use
`executableArgs`| `string[]`| `[]`| Arguments to pass to the executable
`extraArgs`| `Record<string, string | null>`| `{}`| Additional arguments
`fallbackModel`| `string`| `undefined`| Model to use if primary fails
`forkSession`| `boolean`| `false`| When resuming with `resume`, fork to a new session ID instead of continuing the original session
`hooks`| `Partial<Record<``HookEvent``, ``HookCallbackMatcher``[]>>`| `{}`| Hook callbacks for events
`includePartialMessages`| `boolean`| `false`| Include partial message events
`maxThinkingTokens`| `number`| `undefined`| Maximum tokens for thinking process
`maxTurns`| `number`| `undefined`| Maximum conversation turns
`mcpServers`| `Record<string, [`McpServerConfig`](#mcpserverconfig)>`| `{}`| MCP server configurations
`model`| `string`| Default from CLI| Claude model to use
`pathToClaudeCodeExecutable`| `string`| Auto-detected| Path to Claude Code executable
`permissionMode`| `PermissionMode`| `'default'`| Permission mode for the session
`permissionPromptToolName`| `string`| `undefined`| MCP tool name for permission prompts
`resume`| `string`| `undefined`| Session ID to resume
`settingSources`| `SettingSource``[]`| `[]` \(no settings\)| Control which filesystem settings to load. When omitted, no settings are loaded. **Note:** Must include `'project'` to load CLAUDE.md files
`stderr`| `(data: string) => void`| `undefined`| Callback for stderr output
`strictMcpConfig`| `boolean`| `false`| Enforce strict MCP validation
`systemPrompt`| `string | { type: 'preset'; preset: 'claude_code'; append?: string }`| `undefined` \(empty prompt\)| System prompt configuration. Pass a string for custom prompt, or `{ type: 'preset', preset: 'claude_code' }` to use Claude Code’s system prompt. When using the preset object form, add `append` to extend the system prompt with additional instructions

### Query

Interface returned by the `query()` function.

Copy
[code]
    interface Query extends AsyncGenerator<SDKMessage, void> {
      interrupt(): Promise<void>;
      setPermissionMode(mode: PermissionMode): Promise<void>;
    }

[/code]

#### Methods

Method| Description
---|---
`interrupt()`| Interrupts the query \(only available in streaming input mode\)
`setPermissionMode()`| Changes the permission mode \(only available in streaming input mode\)

### AgentDefinition

Configuration for a subagent defined programmatically.

Copy
[code]
    type AgentDefinition = {
      description: string;
      tools?: string[];
      prompt: string;
      model?: 'sonnet' | 'opus' | 'haiku' | 'inherit';
    }

[/code]

Field| Required| Description
---|---|---
`description`| Yes| Natural language description of when to use this agent
`tools`| No| Array of allowed tool names. If omitted, inherits all tools
`prompt`| Yes| The agent’s system prompt
`model`| No| Model override for this agent. If omitted, uses the main model

### SettingSource

Controls which filesystem-based configuration sources the SDK loads settings from.

Copy
[code]
    type SettingSource = 'user' | 'project' | 'local';

[/code]

Value| Description| Location
---|---|---
`'user'`| Global user settings| `~/.claude/settings.json`
`'project'`| Shared project settings \(version controlled\)| `.claude/settings.json`
`'local'`| Local project settings \(gitignored\)| `.claude/settings.local.json`

#### Default behavior

When `settingSources` is **omitted** or **undefined** , the SDK does **not** load any filesystem settings. This provides isolation for SDK applications.

#### Why use settingSources?

**Load all filesystem settings \(legacy behavior\):**

Copy
[code]
    // Load all settings like SDK v0.0.x did
    const result = query({
      prompt: "Analyze this code",
      options: {
        settingSources: ['user', 'project', 'local']  // Load all settings
      }
    });

[/code]

**Load only specific setting sources:**

Copy
[code]
    // Load only project settings, ignore user and local
    const result = query({
      prompt: "Run CI checks",
      options: {
        settingSources: ['project']  // Only .claude/settings.json
      }
    });

[/code]

**Testing and CI environments:**

Copy
[code]
    // Ensure consistent behavior in CI by excluding local settings
    const result = query({
      prompt: "Run tests",
      options: {
        settingSources: ['project'],  // Only team-shared settings
        permissionMode: 'bypassPermissions'
      }
    });

[/code]

**SDK-only applications:**

Copy
[code]
    // Define everything programmatically (default behavior)
    // No filesystem dependencies - settingSources defaults to []
    const result = query({
      prompt: "Review this PR",
      options: {
        // settingSources: [] is the default, no need to specify
        agents: { /* ... */ },
        mcpServers: { /* ... */ },
        allowedTools: ['Read', 'Grep', 'Glob']
      }
    });

[/code]

**Loading CLAUDE.md project instructions:**

Copy
[code]
    // Load project settings to include CLAUDE.md files
    const result = query({
      prompt: "Add a new feature following project conventions",
      options: {
        systemPrompt: {
          type: 'preset',
          preset: 'claude_code'  // Required to use CLAUDE.md
        },
        settingSources: ['project'],  // Loads CLAUDE.md from project directory
        allowedTools: ['Read', 'Write', 'Edit']
      }
    });

[/code]

#### Settings precedence

When multiple sources are loaded, settings are merged with this precedence \(highest to lowest\):

  1. Local settings \(`.claude/settings.local.json`\)
  2. Project settings \(`.claude/settings.json`\)
  3. User settings \(`~/.claude/settings.json`\)

Programmatic options \(like `agents`, `allowedTools`\) always override filesystem settings.

### PermissionMode

Copy
[code]
    type PermissionMode =
      | 'default'           // Standard permission behavior
      | 'acceptEdits'       // Auto-accept file edits
      | 'bypassPermissions' // Bypass all permission checks
      | 'plan'              // Planning mode - no execution

[/code]

### CanUseTool

Custom permission function type for controlling tool usage.

Copy
[code]
    type CanUseTool = (
      toolName: string,
      input: ToolInput,
      options: {
        signal: AbortSignal;
        suggestions?: PermissionUpdate[];
      }
    ) => Promise<PermissionResult>;

[/code]

### PermissionResult

Result of a permission check.

Copy
[code]
    type PermissionResult =
      | {
          behavior: 'allow';
          updatedInput: ToolInput;
          updatedPermissions?: PermissionUpdate[];
        }
      | {
          behavior: 'deny';
          message: string;
          interrupt?: boolean;
        }

[/code]

### McpServerConfig

Configuration for MCP servers.

Copy
[code]
    type McpServerConfig =
      | McpStdioServerConfig
      | McpSSEServerConfig
      | McpHttpServerConfig
      | McpSdkServerConfigWithInstance;

[/code]

#### McpStdioServerConfig

Copy
[code]
    type McpStdioServerConfig = {
      type?: 'stdio';
      command: string;
      args?: string[];
      env?: Record<string, string>;
    }

[/code]

#### McpSSEServerConfig

Copy
[code]
    type McpSSEServerConfig = {
      type: 'sse';
      url: string;
      headers?: Record<string, string>;
    }

[/code]

#### McpHttpServerConfig

Copy
[code]
    type McpHttpServerConfig = {
      type: 'http';
      url: string;
      headers?: Record<string, string>;
    }

[/code]

#### McpSdkServerConfigWithInstance

Copy
[code]
    type McpSdkServerConfigWithInstance = {
      type: 'sdk';
      name: string;
      instance: McpServer;
    }

[/code]

## Message Types

### SDKMessage

Union type of all possible messages returned by the query.

Copy
[code]
    type SDKMessage =
      | SDKAssistantMessage
      | SDKUserMessage
      | SDKUserMessageReplay
      | SDKResultMessage
      | SDKSystemMessage
      | SDKPartialAssistantMessage
      | SDKCompactBoundaryMessage;

[/code]

### SDKAssistantMessage

Assistant response message.

Copy
[code]
    type SDKAssistantMessage = {
      type: 'assistant';
      uuid: UUID;
      session_id: string;
      message: APIAssistantMessage; // From Anthropic SDK
      parent_tool_use_id: string | null;
    }

[/code]

### SDKUserMessage

User input message.

Copy
[code]
    type SDKUserMessage = {
      type: 'user';
      uuid?: UUID;
      session_id: string;
      message: APIUserMessage; // From Anthropic SDK
      parent_tool_use_id: string | null;
    }

[/code]

### SDKUserMessageReplay

Replayed user message with required UUID.

Copy
[code]
    type SDKUserMessageReplay = {
      type: 'user';
      uuid: UUID;
      session_id: string;
      message: APIUserMessage;
      parent_tool_use_id: string | null;
    }

[/code]

### SDKResultMessage

Final result message.

Copy
[code]
    type SDKResultMessage =
      | {
          type: 'result';
          subtype: 'success';
          uuid: UUID;
          session_id: string;
          duration_ms: number;
          duration_api_ms: number;
          is_error: boolean;
          num_turns: number;
          result: string;
          total_cost_usd: number;
          usage: NonNullableUsage;
          permission_denials: SDKPermissionDenial[];
        }
      | {
          type: 'result';
          subtype: 'error_max_turns' | 'error_during_execution';
          uuid: UUID;
          session_id: string;
          duration_ms: number;
          duration_api_ms: number;
          is_error: boolean;
          num_turns: number;
          total_cost_usd: number;
          usage: NonNullableUsage;
          permission_denials: SDKPermissionDenial[];
        }

[/code]

### SDKSystemMessage

System initialization message.

Copy
[code]
    type SDKSystemMessage = {
      type: 'system';
      subtype: 'init';
      uuid: UUID;
      session_id: string;
      apiKeySource: ApiKeySource;
      cwd: string;
      tools: string[];
      mcp_servers: {
        name: string;
        status: string;
      }[];
      model: string;
      permissionMode: PermissionMode;
      slash_commands: string[];
      output_style: string;
    }

[/code]

### SDKPartialAssistantMessage

Streaming partial message \(only when `includePartialMessages` is true\).

Copy
[code]
    type SDKPartialAssistantMessage = {
      type: 'stream_event';
      event: RawMessageStreamEvent; // From Anthropic SDK
      parent_tool_use_id: string | null;
      uuid: UUID;
      session_id: string;
    }

[/code]

### SDKCompactBoundaryMessage

Message indicating a conversation compaction boundary.

Copy
[code]
    type SDKCompactBoundaryMessage = {
      type: 'system';
      subtype: 'compact_boundary';
      uuid: UUID;
      session_id: string;
      compact_metadata: {
        trigger: 'manual' | 'auto';
        pre_tokens: number;
      };
    }

[/code]

### SDKPermissionDenial

Information about a denied tool use.

Copy
[code]
    type SDKPermissionDenial = {
      tool_name: string;
      tool_use_id: string;
      tool_input: ToolInput;
    }

[/code]

## Hook Types

### HookEvent

Available hook events.

Copy
[code]
    type HookEvent =
      | 'PreToolUse'
      | 'PostToolUse'
      | 'Notification'
      | 'UserPromptSubmit'
      | 'SessionStart'
      | 'SessionEnd'
      | 'Stop'
      | 'SubagentStop'
      | 'PreCompact';

[/code]

### HookCallback

Hook callback function type.

Copy
[code]
    type HookCallback = (
      input: HookInput, // Union of all hook input types
      toolUseID: string | undefined,
      options: { signal: AbortSignal }
    ) => Promise<HookJSONOutput>;

[/code]

### HookCallbackMatcher

Hook configuration with optional matcher.

Copy
[code]
    interface HookCallbackMatcher {
      matcher?: string;
      hooks: HookCallback[];
    }

[/code]

### HookInput

Union type of all hook input types.

Copy
[code]
    type HookInput =
      | PreToolUseHookInput
      | PostToolUseHookInput
      | NotificationHookInput
      | UserPromptSubmitHookInput
      | SessionStartHookInput
      | SessionEndHookInput
      | StopHookInput
      | SubagentStopHookInput
      | PreCompactHookInput;

[/code]

### BaseHookInput

Base interface that all hook input types extend.

Copy
[code]
    type BaseHookInput = {
      session_id: string;
      transcript_path: string;
      cwd: string;
      permission_mode?: string;
    }

[/code]

#### PreToolUseHookInput

Copy
[code]
    type PreToolUseHookInput = BaseHookInput & {
      hook_event_name: 'PreToolUse';
      tool_name: string;
      tool_input: ToolInput;
    }

[/code]

#### PostToolUseHookInput

Copy
[code]
    type PostToolUseHookInput = BaseHookInput & {
      hook_event_name: 'PostToolUse';
      tool_name: string;
      tool_input: ToolInput;
      tool_response: ToolOutput;
    }

[/code]

#### NotificationHookInput

Copy
[code]
    type NotificationHookInput = BaseHookInput & {
      hook_event_name: 'Notification';
      message: string;
      title?: string;
    }

[/code]

#### UserPromptSubmitHookInput

Copy
[code]
    type UserPromptSubmitHookInput = BaseHookInput & {
      hook_event_name: 'UserPromptSubmit';
      prompt: string;
    }

[/code]

#### SessionStartHookInput

Copy
[code]
    type SessionStartHookInput = BaseHookInput & {
      hook_event_name: 'SessionStart';
      source: 'startup' | 'resume' | 'clear' | 'compact';
    }

[/code]

#### SessionEndHookInput

Copy
[code]
    type SessionEndHookInput = BaseHookInput & {
      hook_event_name: 'SessionEnd';
      reason: 'clear' | 'logout' | 'prompt_input_exit' | 'other';
    }

[/code]

#### StopHookInput

Copy
[code]
    type StopHookInput = BaseHookInput & {
      hook_event_name: 'Stop';
      stop_hook_active: boolean;
    }

[/code]

#### SubagentStopHookInput

Copy
[code]
    type SubagentStopHookInput = BaseHookInput & {
      hook_event_name: 'SubagentStop';
      stop_hook_active: boolean;
    }

[/code]

#### PreCompactHookInput

Copy
[code]
    type PreCompactHookInput = BaseHookInput & {
      hook_event_name: 'PreCompact';
      trigger: 'manual' | 'auto';
      custom_instructions: string | null;
    }

[/code]

### HookJSONOutput

Hook return value.

Copy
[code]
    type HookJSONOutput = AsyncHookJSONOutput | SyncHookJSONOutput;

[/code]

#### AsyncHookJSONOutput

Copy
[code]
    type AsyncHookJSONOutput = {
      async: true;
      asyncTimeout?: number;
    }

[/code]

#### SyncHookJSONOutput

Copy
[code]
    type SyncHookJSONOutput = {
      continue?: boolean;
      suppressOutput?: boolean;
      stopReason?: string;
      decision?: 'approve' | 'block';
      systemMessage?: string;
      reason?: string;
      hookSpecificOutput?:
        | {
            hookEventName: 'PreToolUse';
            permissionDecision?: 'allow' | 'deny' | 'ask';
            permissionDecisionReason?: string;
          }
        | {
            hookEventName: 'UserPromptSubmit';
            additionalContext?: string;
          }
        | {
            hookEventName: 'SessionStart';
            additionalContext?: string;
          }
        | {
            hookEventName: 'PostToolUse';
            additionalContext?: string;
          };
    }

[/code]

## Tool Input Types

Documentation of input schemas for all built-in Claude Code tools. These types are exported from `@anthropic-ai/claude-agent-sdk` and can be used for type-safe tool interactions.

### ToolInput

**Note:** This is a documentation-only type for clarity. It represents the union of all tool input types.

Copy
[code]
    type ToolInput =
      | AgentInput
      | BashInput
      | BashOutputInput
      | FileEditInput
      | FileMultiEditInput
      | FileReadInput
      | FileWriteInput
      | GlobInput
      | GrepInput
      | KillShellInput
      | NotebookEditInput
      | WebFetchInput
      | WebSearchInput
      | TodoWriteInput
      | ExitPlanModeInput
      | ListMcpResourcesInput
      | ReadMcpResourceInput;

[/code]

### Task

**Tool name:** `Task`

Copy
[code]
    interface AgentInput {
      /**
       * A short (3-5 word) description of the task
       */
      description: string;
      /**
       * The task for the agent to perform
       */
      prompt: string;
      /**
       * The type of specialized agent to use for this task
       */
      subagent_type: string;
    }

[/code]

Launches a new agent to handle complex, multi-step tasks autonomously.

### Bash

**Tool name:** `Bash`

Copy
[code]
    interface BashInput {
      /**
       * The command to execute
       */
      command: string;
      /**
       * Optional timeout in milliseconds (max 600000)
       */
      timeout?: number;
      /**
       * Clear, concise description of what this command does in 5-10 words
       */
      description?: string;
      /**
       * Set to true to run this command in the background
       */
      run_in_background?: boolean;
    }

[/code]

Executes bash commands in a persistent shell session with optional timeout and background execution.

### BashOutput

**Tool name:** `BashOutput`

Copy
[code]
    interface BashOutputInput {
      /**
       * The ID of the background shell to retrieve output from
       */
      bash_id: string;
      /**
       * Optional regex to filter output lines
       */
      filter?: string;
    }

[/code]

Retrieves output from a running or completed background bash shell.

### Edit

**Tool name:** `Edit`

Copy
[code]
    interface FileEditInput {
      /**
       * The absolute path to the file to modify
       */
      file_path: string;
      /**
       * The text to replace
       */
      old_string: string;
      /**
       * The text to replace it with (must be different from old_string)
       */
      new_string: string;
      /**
       * Replace all occurrences of old_string (default false)
       */
      replace_all?: boolean;
    }

[/code]

Performs exact string replacements in files.

### MultiEdit

**Tool name:** `MultiEdit`

Copy
[code]
    interface FileMultiEditInput {
      /**
       * The absolute path to the file to modify
       */
      file_path: string;
      /**
       * Array of edit operations to perform sequentially
       */
      edits: Array<{
        /**
         * The text to replace
         */
        old_string: string;
        /**
         * The text to replace it with
         */
        new_string: string;
        /**
         * Replace all occurrences (default false)
         */
        replace_all?: boolean;
      }>;
    }

[/code]

Makes multiple edits to a single file in one operation.

### Read

**Tool name:** `Read`

Copy
[code]
    interface FileReadInput {
      /**
       * The absolute path to the file to read
       */
      file_path: string;
      /**
       * The line number to start reading from
       */
      offset?: number;
      /**
       * The number of lines to read
       */
      limit?: number;
    }

[/code]

Reads files from the local filesystem, including text, images, PDFs, and Jupyter notebooks.

### Write

**Tool name:** `Write`

Copy
[code]
    interface FileWriteInput {
      /**
       * The absolute path to the file to write
       */
      file_path: string;
      /**
       * The content to write to the file
       */
      content: string;
    }

[/code]

Writes a file to the local filesystem, overwriting if it exists.

### Glob

**Tool name:** `Glob`

Copy
[code]
    interface GlobInput {
      /**
       * The glob pattern to match files against
       */
      pattern: string;
      /**
       * The directory to search in (defaults to cwd)
       */
      path?: string;
    }

[/code]

Fast file pattern matching that works with any codebase size.

### Grep

**Tool name:** `Grep`

Copy
[code]
    interface GrepInput {
      /**
       * The regular expression pattern to search for
       */
      pattern: string;
      /**
       * File or directory to search in (defaults to cwd)
       */
      path?: string;
      /**
       * Glob pattern to filter files (e.g. "*.js")
       */
      glob?: string;
      /**
       * File type to search (e.g. "js", "py", "rust")
       */
      type?: string;
      /**
       * Output mode: "content", "files_with_matches", or "count"
       */
      output_mode?: 'content' | 'files_with_matches' | 'count';
      /**
       * Case insensitive search
       */
      '-i'?: boolean;
      /**
       * Show line numbers (for content mode)
       */
      '-n'?: boolean;
      /**
       * Lines to show before each match
       */
      '-B'?: number;
      /**
       * Lines to show after each match
       */
      '-A'?: number;
      /**
       * Lines to show before and after each match
       */
      '-C'?: number;
      /**
       * Limit output to first N lines/entries
       */
      head_limit?: number;
      /**
       * Enable multiline mode
       */
      multiline?: boolean;
    }

[/code]

Powerful search tool built on ripgrep with regex support.

### KillBash

**Tool name:** `KillBash`

Copy
[code]
    interface KillShellInput {
      /**
       * The ID of the background shell to kill
       */
      shell_id: string;
    }

[/code]

Kills a running background bash shell by its ID.

### NotebookEdit

**Tool name:** `NotebookEdit`

Copy
[code]
    interface NotebookEditInput {
      /**
       * The absolute path to the Jupyter notebook file
       */
      notebook_path: string;
      /**
       * The ID of the cell to edit
       */
      cell_id?: string;
      /**
       * The new source for the cell
       */
      new_source: string;
      /**
       * The type of the cell (code or markdown)
       */
      cell_type?: 'code' | 'markdown';
      /**
       * The type of edit (replace, insert, delete)
       */
      edit_mode?: 'replace' | 'insert' | 'delete';
    }

[/code]

Edits cells in Jupyter notebook files.

### WebFetch

**Tool name:** `WebFetch`

Copy
[code]
    interface WebFetchInput {
      /**
       * The URL to fetch content from
       */
      url: string;
      /**
       * The prompt to run on the fetched content
       */
      prompt: string;
    }

[/code]

Fetches content from a URL and processes it with an AI model.

### WebSearch

**Tool name:** `WebSearch`

Copy
[code]
    interface WebSearchInput {
      /**
       * The search query to use
       */
      query: string;
      /**
       * Only include results from these domains
       */
      allowed_domains?: string[];
      /**
       * Never include results from these domains
       */
      blocked_domains?: string[];
    }

[/code]

Searches the web and returns formatted results.

### TodoWrite

**Tool name:** `TodoWrite`

Copy
[code]
    interface TodoWriteInput {
      /**
       * The updated todo list
       */
      todos: Array<{
        /**
         * The task description
         */
        content: string;
        /**
         * The task status
         */
        status: 'pending' | 'in_progress' | 'completed';
        /**
         * Active form of the task description
         */
        activeForm: string;
      }>;
    }

[/code]

Creates and manages a structured task list for tracking progress.

### ExitPlanMode

**Tool name:** `ExitPlanMode`

Copy
[code]
    interface ExitPlanModeInput {
      /**
       * The plan to run by the user for approval
       */
      plan: string;
    }

[/code]

Exits planning mode and prompts the user to approve the plan.

### ListMcpResources

**Tool name:** `ListMcpResources`

Copy
[code]
    interface ListMcpResourcesInput {
      /**
       * Optional server name to filter resources by
       */
      server?: string;
    }

[/code]

Lists available MCP resources from connected servers.

### ReadMcpResource

**Tool name:** `ReadMcpResource`

Copy
[code]
    interface ReadMcpResourceInput {
      /**
       * The MCP server name
       */
      server: string;
      /**
       * The resource URI to read
       */
      uri: string;
    }

[/code]

Reads a specific MCP resource from a server.

## Tool Output Types

Documentation of output schemas for all built-in Claude Code tools. These types represent the actual response data returned by each tool.

### ToolOutput

**Note:** This is a documentation-only type for clarity. It represents the union of all tool output types.

Copy
[code]
    type ToolOutput =
      | TaskOutput
      | BashOutput
      | BashOutputToolOutput
      | EditOutput
      | MultiEditOutput
      | ReadOutput
      | WriteOutput
      | GlobOutput
      | GrepOutput
      | KillBashOutput
      | NotebookEditOutput
      | WebFetchOutput
      | WebSearchOutput
      | TodoWriteOutput
      | ExitPlanModeOutput
      | ListMcpResourcesOutput
      | ReadMcpResourceOutput;

[/code]

### Task

**Tool name:** `Task`

Copy
[code]
    interface TaskOutput {
      /**
       * Final result message from the subagent
       */
      result: string;
      /**
       * Token usage statistics
       */
      usage?: {
        input_tokens: number;
        output_tokens: number;
        cache_creation_input_tokens?: number;
        cache_read_input_tokens?: number;
      };
      /**
       * Total cost in USD
       */
      total_cost_usd?: number;
      /**
       * Execution duration in milliseconds
       */
      duration_ms?: number;
    }

[/code]

Returns the final result from the subagent after completing the delegated task.

### Bash

**Tool name:** `Bash`

Copy
[code]
    interface BashOutput {
      /**
       * Combined stdout and stderr output
       */
      output: string;
      /**
       * Exit code of the command
       */
      exitCode: number;
      /**
       * Whether the command was killed due to timeout
       */
      killed?: boolean;
      /**
       * Shell ID for background processes
       */
      shellId?: string;
    }

[/code]

Returns command output with exit status. Background commands return immediately with a shellId.

### BashOutput

**Tool name:** `BashOutput`

Copy
[code]
    interface BashOutputToolOutput {
      /**
       * New output since last check
       */
      output: string;
      /**
       * Current shell status
       */
      status: 'running' | 'completed' | 'failed';
      /**
       * Exit code (when completed)
       */
      exitCode?: number;
    }

[/code]

Returns incremental output from background shells.

### Edit

**Tool name:** `Edit`

Copy
[code]
    interface EditOutput {
      /**
       * Confirmation message
       */
      message: string;
      /**
       * Number of replacements made
       */
      replacements: number;
      /**
       * File path that was edited
       */
      file_path: string;
    }

[/code]

Returns confirmation of successful edits with replacement count.

### MultiEdit

**Tool name:** `MultiEdit`

Copy
[code]
    interface MultiEditOutput {
      /**
       * Success message
       */
      message: string;
      /**
       * Total number of edits applied
       */
      edits_applied: number;
      /**
       * File path that was edited
       */
      file_path: string;
    }

[/code]

Returns confirmation after applying all edits sequentially.

### Read

**Tool name:** `Read`

Copy
[code]
    type ReadOutput =
      | TextFileOutput
      | ImageFileOutput
      | PDFFileOutput
      | NotebookFileOutput;

    interface TextFileOutput {
      /**
       * File contents with line numbers
       */
      content: string;
      /**
       * Total number of lines in file
       */
      total_lines: number;
      /**
       * Lines actually returned
       */
      lines_returned: number;
    }

    interface ImageFileOutput {
      /**
       * Base64 encoded image data
       */
      image: string;
      /**
       * Image MIME type
       */
      mime_type: string;
      /**
       * File size in bytes
       */
      file_size: number;
    }

    interface PDFFileOutput {
      /**
       * Array of page contents
       */
      pages: Array<{
        page_number: number;
        text?: string;
        images?: Array<{
          image: string;
          mime_type: string;
        }>;
      }>;
      /**
       * Total number of pages
       */
      total_pages: number;
    }

    interface NotebookFileOutput {
      /**
       * Jupyter notebook cells
       */
      cells: Array<{
        cell_type: 'code' | 'markdown';
        source: string;
        outputs?: any[];
        execution_count?: number;
      }>;
      /**
       * Notebook metadata
       */
      metadata?: Record<string, any>;
    }

[/code]

Returns file contents in format appropriate to file type.

### Write

**Tool name:** `Write`

Copy
[code]
    interface WriteOutput {
      /**
       * Success message
       */
      message: string;
      /**
       * Number of bytes written
       */
      bytes_written: number;
      /**
       * File path that was written
       */
      file_path: string;
    }

[/code]

Returns confirmation after successfully writing the file.

### Glob

**Tool name:** `Glob`

Copy
[code]
    interface GlobOutput {
      /**
       * Array of matching file paths
       */
      matches: string[];
      /**
       * Number of matches found
       */
      count: number;
      /**
       * Search directory used
       */
      search_path: string;
    }

[/code]

Returns file paths matching the glob pattern, sorted by modification time.

### Grep

**Tool name:** `Grep`

Copy
[code]
    type GrepOutput =
      | GrepContentOutput
      | GrepFilesOutput
      | GrepCountOutput;

    interface GrepContentOutput {
      /**
       * Matching lines with context
       */
      matches: Array<{
        file: string;
        line_number?: number;
        line: string;
        before_context?: string[];
        after_context?: string[];
      }>;
      /**
       * Total number of matches
       */
      total_matches: number;
    }

    interface GrepFilesOutput {
      /**
       * Files containing matches
       */
      files: string[];
      /**
       * Number of files with matches
       */
      count: number;
    }

    interface GrepCountOutput {
      /**
       * Match counts per file
       */
      counts: Array<{
        file: string;
        count: number;
      }>;
      /**
       * Total matches across all files
       */
      total: number;
    }

[/code]

Returns search results in the format specified by output\_mode.

### KillBash

**Tool name:** `KillBash`

Copy
[code]
    interface KillBashOutput {
      /**
       * Success message
       */
      message: string;
      /**
       * ID of the killed shell
       */
      shell_id: string;
    }

[/code]

Returns confirmation after terminating the background shell.

### NotebookEdit

**Tool name:** `NotebookEdit`

Copy
[code]
    interface NotebookEditOutput {
      /**
       * Success message
       */
      message: string;
      /**
       * Type of edit performed
       */
      edit_type: 'replaced' | 'inserted' | 'deleted';
      /**
       * Cell ID that was affected
       */
      cell_id?: string;
      /**
       * Total cells in notebook after edit
       */
      total_cells: number;
    }

[/code]

Returns confirmation after modifying the Jupyter notebook.

### WebFetch

**Tool name:** `WebFetch`

Copy
[code]
    interface WebFetchOutput {
      /**
       * AI model's response to the prompt
       */
      response: string;
      /**
       * URL that was fetched
       */
      url: string;
      /**
       * Final URL after redirects
       */
      final_url?: string;
      /**
       * HTTP status code
       */
      status_code?: number;
    }

[/code]

Returns the AI’s analysis of the fetched web content.

### WebSearch

**Tool name:** `WebSearch`

Copy
[code]
    interface WebSearchOutput {
      /**
       * Search results
       */
      results: Array<{
        title: string;
        url: string;
        snippet: string;
        /**
         * Additional metadata if available
         */
        metadata?: Record<string, any>;
      }>;
      /**
       * Total number of results
       */
      total_results: number;
      /**
       * The query that was searched
       */
      query: string;
    }

[/code]

Returns formatted search results from the web.

### TodoWrite

**Tool name:** `TodoWrite`

Copy
[code]
    interface TodoWriteOutput {
      /**
       * Success message
       */
      message: string;
      /**
       * Current todo statistics
       */
      stats: {
        total: number;
        pending: number;
        in_progress: number;
        completed: number;
      };
    }

[/code]

Returns confirmation with current task statistics.

### ExitPlanMode

**Tool name:** `ExitPlanMode`

Copy
[code]
    interface ExitPlanModeOutput {
      /**
       * Confirmation message
       */
      message: string;
      /**
       * Whether user approved the plan
       */
      approved?: boolean;
    }

[/code]

Returns confirmation after exiting plan mode.

### ListMcpResources

**Tool name:** `ListMcpResources`

Copy
[code]
    interface ListMcpResourcesOutput {
      /**
       * Available resources
       */
      resources: Array<{
        uri: string;
        name: string;
        description?: string;
        mimeType?: string;
        server: string;
      }>;
      /**
       * Total number of resources
       */
      total: number;
    }

[/code]

Returns list of available MCP resources.

### ReadMcpResource

**Tool name:** `ReadMcpResource`

Copy
[code]
    interface ReadMcpResourceOutput {
      /**
       * Resource contents
       */
      contents: Array<{
        uri: string;
        mimeType?: string;
        text?: string;
        blob?: string;
      }>;
      /**
       * Server that provided the resource
       */
      server: string;
    }

[/code]

Returns the contents of the requested MCP resource.

## Permission Types

### PermissionUpdate

Operations for updating permissions.

Copy
[code]
    type PermissionUpdate =
      | {
          type: 'addRules';
          rules: PermissionRuleValue[];
          behavior: PermissionBehavior;
          destination: PermissionUpdateDestination;
        }
      | {
          type: 'replaceRules';
          rules: PermissionRuleValue[];
          behavior: PermissionBehavior;
          destination: PermissionUpdateDestination;
        }
      | {
          type: 'removeRules';
          rules: PermissionRuleValue[];
          behavior: PermissionBehavior;
          destination: PermissionUpdateDestination;
        }
      | {
          type: 'setMode';
          mode: PermissionMode;
          destination: PermissionUpdateDestination;
        }
      | {
          type: 'addDirectories';
          directories: string[];
          destination: PermissionUpdateDestination;
        }
      | {
          type: 'removeDirectories';
          directories: string[];
          destination: PermissionUpdateDestination;
        }

[/code]

### PermissionBehavior

Copy
[code]
    type PermissionBehavior = 'allow' | 'deny' | 'ask';

[/code]

### PermissionUpdateDestination

Copy
[code]
    type PermissionUpdateDestination =
      | 'userSettings'     // Global user settings
      | 'projectSettings'  // Per-directory project settings
      | 'localSettings'    // Gitignored local settings
      | 'session'          // Current session only

[/code]

### PermissionRuleValue

Copy
[code]
    type PermissionRuleValue = {
      toolName: string;
      ruleContent?: string;
    }

[/code]

## Other Types

### ApiKeySource

Copy
[code]
    type ApiKeySource = 'user' | 'project' | 'org' | 'temporary';

[/code]

### ConfigScope

Copy
[code]
    type ConfigScope = 'local' | 'user' | 'project';

[/code]

### NonNullableUsage

A version of `Usage` with all nullable fields made non-nullable.

Copy
[code]
    type NonNullableUsage = {
      [K in keyof Usage]: NonNullable<Usage[K]>;
    }

[/code]

### Usage

Token usage statistics \(from `@anthropic-ai/sdk`\).

Copy
[code]
    type Usage = {
      input_tokens: number | null;
      output_tokens: number | null;
      cache_creation_input_tokens?: number | null;
      cache_read_input_tokens?: number | null;
    }

[/code]

### CallToolResult

MCP tool result type \(from `@modelcontextprotocol/sdk/types.js`\).

Copy
[code]
    type CallToolResult = {
      content: Array<{
        type: 'text' | 'image' | 'resource';
        // Additional fields vary by type
      }>;
      isError?: boolean;
    }

[/code]

### AbortError

Custom error class for abort operations.

Copy
[code]
    class AbortError extends Error {}

[/code]

## See also

  * [SDK overview](/en/api/agent-sdk/overview) \- General SDK concepts
  * [Python SDK reference](/en/api/agent-sdk/python) \- Python SDK documentation
  * [CLI reference](/en/docs/claude-code/cli-reference) \- Command-line interface
  * [Common workflows](/en/docs/claude-code/common-workflows) \- Step-by-step guides

Was this page helpful?

YesNo

[Overview](/en/api/agent-sdk/overview)[Python SDK](/en/api/agent-sdk/python)
