# Directory: sdk

## Overview
This directory contains migration guides and headless operation documentation for the Claude SDK, covering the transition from Claude Code SDK to Claude Agent SDK and programmatic CLI usage.

## Files in This Directory

### **migration-guide.md**
This guide documents the rebranding and migration process from Claude Code SDK to Claude Agent SDK. The SDK has been renamed to reflect its broader capabilities for building AI agents beyond coding tasks.

**Key changes include:**
- **Package names:** TypeScript/JavaScript package changed from `@anthropic-ai/claude-code` to `@anthropic-ai/claude-agent-sdk`; Python package changed from `claude-code-sdk` to `claude-agent-sdk`
- **Documentation relocation:** SDK docs moved from Claude Code section to API Guide under Agent SDK section
- **Migration steps:** Detailed instructions for both TypeScript/JavaScript and Python projects including package uninstall/install, import updates, and dependency file modifications

**Breaking changes in v0.1.0:**
- **Python type rename:** `ClaudeCodeOptions` renamed to `ClaudeAgentOptions`
- **System prompt no longer default:** SDK uses empty system prompt by default instead of Claude Code's system prompt; must explicitly request the "claude_code" preset to get previous behavior
- **Settings sources not loaded by default:** No longer reads filesystem settings (CLAUDE.md, settings.json, slash commands) automatically; must explicitly specify `settingSources: ['user', 'project', 'local']` for previous behavior

**Rationale:** These changes provide better isolation and explicit configuration for SDK applications, ensuring predictable behavior independent of local filesystem configurations. This is especially important for CI/CD environments, deployed applications, testing, and multi-tenant systems.

### **sdk-headless.md**
This guide covers running Claude Code programmatically from command-line scripts and automation tools without interactive UI using the `--print` (or `-p`) flag.

**Configuration options:**
- **Output formats:** text (default), json (structured data with metadata), stream-json (streams each message as received)
- **Input formats:** text (default via argument or stdin), stream-json (jsonl format for multi-turn conversations)
- **Key flags:** `--print` (non-interactive), `--output-format`, `--resume` (by session ID), `--continue` (most recent), `--allowedTools`, `--disallowedTools`, `--mcp-config`, `--append-system-prompt`, `--permission-prompt-tool`

**Multi-turn conversations:** Supports resuming specific sessions by ID or continuing the most recent conversation, enabling context preservation across multiple programmatic calls.

**Use case examples:**
- **SRE incident response bot:** Automated incident diagnosis with monitoring tool integration
- **Automated security review:** Pull request vulnerability scanning and compliance checking
- **Multi-turn legal assistant:** Session-based contract review with persistent context

**Best practices:**
- Use JSON output format for programmatic parsing with tools like jq
- Handle errors gracefully by checking exit codes and stderr
- Implement session management for multi-turn context
- Add timeouts for long-running operations
- Respect rate limits with delays between multiple requests
