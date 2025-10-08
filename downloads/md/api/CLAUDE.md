# Directory: api

## Overview
This directory contains comprehensive API reference documentation for Claude's APIs, including the Messages API, Admin API, Usage & Cost APIs, and the Agent SDK for building production-ready AI agents.

## Files in This Directory

### **admin-api.md**
Single-endpoint API reference for retrieving organization information via GET `/v1/organizations/me`. Returns organization ID, name, and type. Requires Admin API key authentication. Note: Admin API is unavailable for individual accounts.

### **administration-api.md**
Comprehensive guide to the Admin API for programmatic organization management. Covers user management, workspace administration, API key lifecycle, invitation handling, and usage reporting. Requires special Admin API key (sk-ant-admin...) accessible only to organization admins. Includes organization roles (user, claude_code_user, developer, billing, admin), workspace permissions, and automated workflows for onboarding/offboarding. Explains workspace concepts including the Default Workspace and automatic role inheritance patterns.

### **beta-headers.md**
Documentation for accessing experimental API features using the `anthropic-beta` header. Supports multiple beta features via comma-separated values. Beta feature naming follows `feature-name-YYYY-MM-DD` convention. Features may have breaking changes, different rate limits, or be removed without notice. Includes SDK usage examples with `betas` parameter.

### **canceling-message-batches.md**
- API endpoint: POST `/v1/messages/batches/{message_batch_id}/cancel`
- Cancels in-progress message batches to stop processing queued requests
- Only batches in `in_progress` state can be canceled
- Transitions batch to `canceling` then `canceled` status
- Requests already processing will complete; unprocessed requests won't be charged

### **claude-code-analytics-api.md**
Programmatic access to daily Claude Code usage metrics via `/v1/organizations/usage_report/claude_code` endpoint. Provides per-user productivity analytics including sessions, lines of code (added/removed), commits, PRs, tool acceptance rates (Edit, MultiEdit, Write, NotebookEdit), and model-level token usage with estimated costs. Supports cursor-based pagination for large datasets. Data available with 1-hour delay. Requires Admin API key. Only tracks 1st party Claude API usage (not Bedrock/Vertex AI).

### **claude-on-amazon-bedrock.md**
- Configuration guide for using Claude via Amazon Bedrock
- Supports Python and TypeScript SDKs with AWS credentials
- Region-specific model access and availability
- Cross-region inference for enhanced reliability
- Streaming support and guardrails integration
- Model IDs, pricing, and feature compatibility

### **claude-on-vertex-ai.md**
- Configuration guide for using Claude on Google Cloud Vertex AI
- Supports Python and TypeScript SDKs with GCP credentials
- Region-specific model availability and inference endpoints
- Streaming support and context caching
- Model IDs, pricing, and feature compatibility
- Project-based authentication and setup

### **client-sdks.md**
Official SDK documentation for 7 languages: Python, TypeScript, Java, Go, C#, Ruby, and PHP. Each includes installation instructions, authentication patterns, model string constants/enums, and basic usage examples. Covers Claude 4.x, 3.7, 3.5, and 3 model families with aliases (e.g., claude-sonnet-4-5 → claude-sonnet-4-5-20250929). All SDKs provide a beta namespace for accessing experimental features via `betas` parameter.

### **creating-message-batches.md**
- API endpoint: POST `/v1/messages/batches`
- Create async batch processing jobs with up to 100K requests
- 50% discount compared to standard API
- 24-hour processing window with result persistence
- Custom IDs for request tracking
- JSONL request format with validation requirements

### **deleting-message-batches.md**
- API endpoint: DELETE `/v1/messages/batches/{message_batch_id}`
- Permanently deletes message batch and all associated data
- Cannot be undone - use with caution
- Returns deleted batch object as confirmation
- Batch must exist to delete (404 if not found)

### **errors.md**
Comprehensive error handling guide covering HTTP error codes (400-529), error object structure with `type` and `message` fields, and request size limits (32MB standard, 256MB batch, 500MB files). Documents rate limit errors (429), overloaded errors (529), and unique `request_id` for debugging. Recommends streaming API or Message Batches for long-running requests (>10 minutes) and explains TCP socket keep-alive for network resilience.

### **files-content.md**
- API endpoint: GET `/v1/organizations/files/{file_id}/content`
- Download binary file content as application/octet-stream
- Returns raw file bytes for files uploaded via Files API
- Requires file_id from file creation or listing
- Content-Type header indicates binary format

### **files-create.md**
- API endpoint: POST `/v1/organizations/files`
- Upload files up to 500 MB via multipart/form-data
- Supports PDF, text, images, and code files
- Returns file metadata with unique file_id
- Purpose field determines file usage context
- Files are organization-scoped, not workspace-scoped

### **files-delete.md**
- API endpoint: DELETE `/v1/organizations/files/{file_id}`
- Permanently deletes files and all metadata
- Cannot be undone - use with caution
- Returns deleted file object as confirmation
- File must exist to delete (404 if not found)

### **files-list.md**
- API endpoint: GET `/v1/organizations/files`
- List all organization files with pagination
- Filter by purpose, type, and workspace
- Returns file metadata including size, type, created_at
- Supports limit and page parameters
- Default limit: 20 files per page

### **files-metadata.md**
- API endpoint: GET `/v1/organizations/files/{file_id}`
- Retrieve file metadata without downloading content
- Returns filename, size, MIME type, purpose, timestamps
- Useful for validation before content download
- File must exist (404 if not found)

### **getting-help.md**
- Brief guide on accessing support resources
- Links to documentation, API reference, and community forums
- Contact information for technical support
- Troubleshooting tips and best practices

### **getting-started.md**
Identical to overview.md - covers API access via Console, authentication using x-api-key header, JSON content-type requirements, and request size limits (32MB standard, 256MB batch, 500MB files). Includes response headers (request-id, anthropic-organization-id) and basic cURL/SDK examples for Messages API.

### **handling-stop-reasons.md**
Comprehensive guide to interpreting `stop_reason` values in Messages API responses. Covers seven stop reasons: `end_turn` (natural completion), `max_tokens` (token limit reached), `stop_sequence` (custom sequence matched), `tool_use` (model needs tool execution), `pause_turn` (long response paused for resumption), `refusal` (policy violation), and `model_context_window_exceeded` (input too large). Includes best practices for each scenario, empty response handling, continuation patterns for paused turns, and error recovery strategies.

### **ip-addresses.md**
- Documentation about Anthropic API IP address ranges
- Information for allowlist/firewall configuration
- May include egress IPs for server tool callbacks
- Important for network security and access control

### **listing-message-batches.md**
- API endpoint: GET `/v1/messages/batches`
- List all message batches with pagination
- Filter by status and time range
- Returns batch metadata including processing state
- Supports before_id and after_id cursors
- Default limit: 20 batches per page

### **messages-batch-examples.md**
- Practical examples of Message Batches API usage
- JSONL request format samples
- Batch creation and result retrieval workflows
- Error handling patterns for batch processing
- Cost calculation and optimization tips

### **messages-count-tokens.md**
- API endpoint: POST `/v1/messages/count_tokens`
- Preview token usage before making actual API requests
- Returns input_tokens count for given messages/system prompt
- Useful for cost estimation and max_tokens planning
- Supports same parameters as Messages API
- Helps avoid exceeding token limits

### **messages-examples.md**
Practical examples demonstrating Messages API usage patterns: basic request/response, multi-turn conversations (stateless API requiring full history), prefilling Claude's responses for constrained outputs (e.g., multiple choice), and vision capabilities supporting base64-encoded or URL-referenced images (JPEG, PNG, GIF, WebP). Includes references to tool use and computer use guides. All examples provided in Shell, Python, and TypeScript.

### **messages-streaming.md**
Comprehensive streaming guide using server-sent events (SSE). Documents event flow: message_start → content_block_start → content_block_delta (text_delta, input_json_delta, thinking_delta) → content_block_stop → message_delta → message_stop. Includes ping events, error handling, signature verification for thinking blocks, and examples for basic streaming, tool use, extended thinking, and web search. SDK helpers provided for Python/TypeScript. Supports error recovery by resuming from partial responses.

### **messages.md**
Complete Messages API reference for POST `/v1/messages`. Documents all request parameters: model, messages (alternating user/assistant turns), max_tokens, system prompts, temperature, streaming, tools, tool_choice, stop_sequences, thinking configuration, metadata, service_tier, context_management, MCP servers, and container settings. Response includes message ID, role, content blocks (text, thinking, tool_use, server_tool_use, MCP tool results), stop_reason, usage statistics, and container information. Maximum 100K messages per request, 32MB size limit.

### **migrating-from-text-completions-to-messages.md**
- Migration guide from legacy Text Completions API to Messages API
- Key differences in request/response format
- Mapping between old and new parameters
- Code examples showing before/after patterns
- Best practices for smooth migration

### **models-list.md**
- API endpoint: GET `/v1/models`
- List all available Claude models
- Returns model IDs, display names, and release dates
- Useful for discovering model versions
- Pagination support for large model lists

### **models.md**
API reference for GET `/v1/models/{model_id}`. Retrieves model metadata including unique ID (e.g., claude-sonnet-4-20250514), display_name (e.g., "Claude Sonnet 4"), created_at timestamp (RFC 3339), and type field (always "model"). Supports model ID aliases. Returns 404 for invalid model IDs.

### **openai-sdk.md**
OpenAI SDK compatibility layer for testing and comparison purposes. Requires changing base URL to `https://api.anthropic.com/v1/`, using Claude API key, and Claude model names. Not recommended for production - native Claude API provides full feature access (PDF processing, citations, extended thinking, prompt caching). Intended for capability testing, not long-term use. Includes quick start examples for Python and TypeScript.

### **overview.md**
Identical to getting-started.md - entry point documentation covering Console access, API key authentication via x-api-key header, JSON content-type requirements, request size limits by endpoint type, response headers for debugging, and basic usage examples in cURL/Python/TypeScript for the Messages API.

### **prompt-tools-generate.md**
- API endpoint for AI-powered prompt generation
- Creates optimized prompts from natural language descriptions
- Supports various prompt types and use cases
- Returns structured prompt with examples
- Helps streamline prompt engineering workflow

### **prompt-tools-improve.md**
- API endpoint for enhancing existing prompts
- Analyzes and suggests improvements to prompts
- Optimizes for clarity, specificity, and effectiveness
- Returns improved prompt with explanations
- Useful for iterative prompt refinement

### **prompt-tools-templatize.md**
- API endpoint for converting prompts into reusable templates
- Identifies variable components in prompts
- Creates parameterized templates with placeholders
- Returns template structure and variable definitions
- Enables scalable prompt management

### **rate-limits.md**
Comprehensive rate limiting documentation covering spend limits (monthly caps by tier) and rate limits (RPM, ITPM, OTPM per model). Four usage tiers requiring credit purchases ($5, $40, $200, $400) with tier-specific limits. Token bucket algorithm for continuous replenishment. Message Batches API has separate limits (50 RPM, 100K batch requests in queue). Long context requests (>200K tokens) have dedicated limits for 1M context window. Response headers expose current limits and remaining capacity. Workspace-level limits available for resource allocation.

### **retrieving-message-batch-results.md**
- API endpoint: GET `/v1/messages/batches/{message_batch_id}/results`
- Download batch processing results as JSONL
- Each line contains request result with custom_id
- Results available after batch reaches ended status
- Supports streaming download for large result sets
- Results retained for 24 hours after completion

### **retrieving-message-batches.md**
- API endpoint: GET `/v1/messages/batches/{message_batch_id}`
- Get detailed batch status and metadata
- Returns processing state, request counts, progress
- Shows created_at, expires_at, ended_at timestamps
- Useful for monitoring batch progress
- Includes results_url when processing completes

### **service-tiers.md**
- Documentation on API service tier options
- Standard Tier (default): Best-effort service with standard pricing
- Priority Tier: Enhanced reliability with committed spend
- Rate limit differences between tiers
- Pricing and billing implications
- How to request Priority Tier access

### **supported-regions.md**
- Geographic availability of Claude API services
- Regional data residency information
- Latency considerations by region
- Partner platform regional availability
- Compliance and regulatory requirements per region

### **usage-cost-api.md**
Admin API providing programmatic access to usage/cost data via two endpoints: Usage API (`/v1/organizations/usage_report/messages`) tracks token consumption with grouping by model/workspace/service_tier/context_window and time bucket granularity (1m/1h/1d); Cost API (`/v1/organizations/cost_report`) provides USD cost breakdowns (daily only) by workspace/description. Both support pagination and filtering. Enables cost reconciliation, rate limit optimization, performance monitoring, and advanced analytics. Partner integrations available (Datadog, Grafana, Honeycomb). Requires Admin API key. Data available within 5 minutes, supports 1-minute polling.

### **versioning.md**
API versioning policy preserving existing inputs/outputs while allowing additions (optional inputs, new output fields, new enum variants). Current versions: `2023-06-01` (latest - improved SSE streaming with incremental completions, named events, removed legacy fields) and `2023-01-01` (initial release, deprecated). Recommends using latest version. Version specified via `anthropic-version` header.

## Subdirectories

### **admin-api/**
Comprehensive Admin API reference for organization management including users, workspaces, API keys, invitations, and usage reporting
- apikeys/get-api-key.md: Retrieve specific API key details by ID
- apikeys/list-api-keys.md: List all API keys with filtering by status, workspace, creator
- apikeys/update-api-key.md: Update API key name or status (active, inactive, archived)
- claude-code/get-claude-code-usage-report.md: Daily Claude Code metrics with sessions, commits, PRs, token usage, model breakdown
- invites/create-invite.md: Create organization invitations with role assignments
- invites/delete-invite.md: Delete pending invitations before acceptance
- invites/get-invite.md: Retrieve invitation details and status by ID
- invites/list-invites.md: List all organization invitations with pagination
- organization/get-me.md: Retrieve authenticated organization's ID, name, and type
- usage-cost/get-cost-report.md: Cost reports grouped by workspace, model with time-bucket granularity
- usage-cost/get-messages-usage-report.md: Token usage statistics with filtering by API keys, workspaces, models, service tiers
- users/get-user.md: Retrieve detailed user information by ID
- users/list-users.md: List all organization users with pagination and email filtering
- users/remove-user.md: Delete user from organization
- users/update-user.md: Update user's organization role
- workspace_members/create-workspace-member.md: Add member to workspace with role assignment
- workspace_members/delete-workspace-member.md: Remove member from workspace
- workspace_members/get-workspace-member.md: Retrieve workspace member details and role
- workspace_members/list-workspace-members.md: List all workspace members with pagination
- workspace_members/update-workspace-member.md: Modify workspace member role (workspace_user, workspace_developer, workspace_admin, workspace_billing)
- workspaces/archive-workspace.md: Archive workspace by ID (sets archived_at timestamp)
- workspaces/create-workspace.md: Create new workspace with name (1-40 characters)
- workspaces/get-workspace.md: Retrieve workspace details by ID
- workspaces/list-workspaces.md: List all workspaces with pagination and optional archived workspaces
- workspaces/update-workspace.md: Update workspace name

### **agent-sdk/**
Claude Agent SDK documentation covering TypeScript and Python implementations for production AI agents
- cost-tracking.md: Token usage tracking, per-step cost calculation, BillingAggregator patterns, cache token handling
- custom-tools.md: Creating MCP tools with createSdkMcpServer, Zod schema validation, tool naming conventions (mcp__{server}__{tool})
- mcp.md: Model Context Protocol server configuration (stdio, HTTP/SSE, SDK transports), .mcp.json config, resource management, OAuth2 auth
- modifying-system-prompts.md: Four customization methods - CLAUDE.md files, output styles, system prompt append, fully custom prompts
- overview.md: SDK introduction, installation (TypeScript/Python), authentication options (API key, Bedrock, Vertex AI), key benefits
- permissions.md: Four permission control methods (modes, canUseTool, hooks, rules), permission flow, acceptEdits/bypassPermissions modes
- python.md: Complete Python reference - query() function, ClaudeSDKClient class, @tool decorator, type documentation, context managers
- sessions.md: Session management, capturing session IDs, resuming with session ID, forking sessions for branching conversations
- slash-commands.md: Built-in commands (/compact, /clear), custom commands in .claude/commands/, YAML frontmatter, arguments/bash/file refs
- streaming-vs-single-mode.md: Streaming (default, persistent sessions, hooks, images) vs Single Message (one-shot queries without context)
- subagents.md: Specialized AI orchestration, programmatic vs filesystem definition, tool restrictions, context separation, parallelization
- todo-tracking.md: Built-in todo functionality, lifecycle (pending→in_progress→completed), TodoWrite monitoring, TodoTracker examples
- typescript.md: Complete TypeScript reference - query() async generator, tool() with Zod, hooks system, message types, settingSources
