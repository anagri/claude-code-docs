# Directory: agents-and-tools

## Overview
This directory covers Claude's agent capabilities and tool ecosystem, including Google Sheets integration, Model Context Protocol (MCP) implementation, and remote server connections for extending Claude's functionality.

## Files in This Directory

### **claude-for-sheets.md**
Documents the Claude for Sheets Google Workspace extension that enables prompt engineering at scale and office automation. The extension supports two main functions: `CLAUDE()` for basic prompts and `CLAUDEMESSAGES()` for multi-turn conversations with prefilled responses. Installation requires an API key configured per sheet at Extensions > Claude for Sheets > Settings. Function parameters include model selection (always second parameter), optional API parameters (max_tokens, temperature, system, stop_sequences, api_key) passed as argument-value pairs. The extension excels at testing prompts across evaluation suites in parallel, survey analysis, and online data processing. Includes links to interactive prompt engineering tutorial and workbook templates. Troubleshooting covers NAME errors (enable extension in document), ERROR/DEFERRED/THROTTLED cells (manual recalculation), and API key entry issues (wait/refresh/reinstall).

### **mcp-connector.md**
Explains the MCP connector feature (beta) that enables connecting to remote MCP servers directly from the Messages API without a separate MCP client. Requires beta header `anthropic-beta: mcp-client-2025-04-04`. Key features include direct API integration, tool calling support, OAuth Bearer token authentication, and multiple server connections. Currently only supports tool calls from the MCP specification (not prompts or resources), requires publicly exposed HTTP servers (Streamable HTTP or SSE transports), and is not available on Amazon Bedrock or Google Vertex. Configuration includes `mcp_servers` array with fields: type (only "url" supported), url (must be https://), name (unique identifier), optional tool_configuration (enabled, allowed_tools), and optional authorization_token for OAuth. Responses include two new content block types: `mcp_tool_use` (with id, name, server_name, input) and `mcp_tool_result` (with tool_use_id, is_error, content). OAuth token acquisition is handled by API consumers using the MCP inspector for testing purposes.

### **mcp.md**
Provides high-level introduction to Model Context Protocol (MCP) as an open protocol standardizing how applications provide context to LLMs. Compares MCP to USB-C as a standardized connection for AI applications to data sources and tools. Links to external MCP documentation at modelcontextprotocol.io for building servers and clients. Lists MCP integration across Anthropic products: Messages API (MCP connector), Claude Code (server management and client usage), Claude.ai (team connectors), and Claude Desktop (local server configuration).

### **remote-mcp-servers.md**
Lists third-party remote MCP servers deployable via the Anthropic MCP connector API, categorized by function. Development & Testing Tools include Hugging Face (Hub and Gradio access) and Jam (debugging with recordings). Project Management & Documentation includes Asana, Atlassian (Jira/Confluence), Intercom, Linear, Box, Fireflies (meeting transcripts), and Monday. Databases & Data Management includes Daloopa (financial data) and HubSpot (CRM). Payments & Commerce includes PayPal, Plaid (banking data), Square, and Stripe. Design & Media includes Cloudinary, invideo, and Canva. Infrastructure & DevOps includes Cloudflare, Netlify, Stytch (authentication), and Vercel. Automation & Integration includes Workato and Zapier (8,000+ apps). Each entry provides server URL and brief description. Includes disclaimer that servers are third-party services not owned or endorsed by Anthropic, with security and trust considerations for users.

## Subdirectories

### **tool-use/**
Comprehensive documentation for Claude's tool use capabilities including client-side and server-side tools
- bash-tool.md: Bash tool for executing shell commands in persistent sessions with state maintenance
- code-execution-tool.md: Sandboxed code execution environment with bash and file manipulation tools
- computer-use-tool.md: Desktop environment interaction via screenshots and mouse/keyboard control
- fine-grained-tool-streaming.md: Streaming tool parameters without buffering for reduced latency
- implement-tool-use.md: Implementation guide covering tool definition, JSON Schema, tool choice parameters, and best practices
- memory-tool.md: File-based memory storage for cross-conversation information persistence
- overview.md: Foundational overview distinguishing client tools vs server tools and tool use workflow
- text-editor-tool.md: Text file viewing and modification for code debugging and refactoring
- token-efficient-tool-use.md: Token reduction feature for Sonnet 3.7 saving up to 70% output tokens
- web-fetch-tool.md: Web page and PDF content retrieval with domain filtering and citations
- web-search-tool.md: Real-time web search with automatic citations and organization-level controls
