# Directory: docs

## Overview
This directory serves as the comprehensive documentation hub for Claude, Anthropic's family of AI models and associated tools. It covers everything from getting started with the API to advanced features, model capabilities, Claude Code CLI tool, agent development, and production deployment strategies.

## Files in This Directory

### **claude-code.md**
Migration guide documenting the transition from Claude Code SDK to Claude Agent SDK. The SDK package names changed from @anthropic-ai/claude-code to @anthropic-ai/claude-agent-sdk (TypeScript/JavaScript) and claude-code-sdk to claude-agent-sdk (Python). Documentation moved from Claude Code docs to API Guide under a dedicated Agent SDK section. Includes step-by-step migration instructions for both languages, breaking changes in v0.1.0 (system prompt no longer default, settings sources not loaded by default, Python type rename ClaudeCodeOptions to ClaudeAgentOptions), and rationale for changes focusing on better control, isolation, and explicit configuration for SDK applications.

### **claude_api_primer.md.md**
Comprehensive technical primer designed to give Claude itself the fundamentals of using the Claude API. Covers model IDs (Sonnet 4.5, Haiku 3.5), basic Messages API usage with request/response formats, multiple conversational turns, prompt prefilling, vision capabilities with base64 and URL images, extended thinking with budget_tokens configuration, extended thinking with tool use including thinking block preservation and interleaved thinking, tool use implementation (defining tools with JSON Schema, best practices for descriptions, forcing tool use, parallel/sequential tools, chain of thought), handling tool results and errors, JSON mode for structured output, and streaming with server-sent events including all delta types (text_delta, input_json_delta, thinking_delta). Provides extensive code examples in Python for each concept.

### **get-started.md**
Quick start guide for making your first Claude API call. Prerequisites include an Anthropic Console account and API key. Provides example cURL request for creating a simple web search assistant using claude-sonnet-4-5 model with expected output. Links to next steps including Features Overview, Client SDKs, and Claude Cookbook for deeper learning.

### **initial-setup.md**
Initial setup guide identical to get-started.md, providing the same prerequisites, API key setup via environment variable, and first API call example using cURL to create a web search assistant. Includes the same next steps for exploring Claude's advanced features, client libraries, and interactive Jupyter notebooks.

### **intro-to-claude.md**
Comprehensive introduction to Claude's enterprise capabilities and development workflow. Covers what you can do with Claude (text/code generation, vision, tool use), enterprise considerations (security with SOC 2 Type 2 and HIPAA compliance, trustworthiness, 200K token context window with future 1M support, reliability, global language fluency, cost consciousness), and the 8-step implementation flow: scope use case, design integration, prepare data, develop prompts, implement Claude, test system, deploy to production, and monitor/improve. Provides links to quickstart guides, API reference, prompt library, Workbench, and Claude Cookbook.

### **intro.md**
Main landing page introducing Claude Sonnet 4.5 (best for complex agents and coding) and Claude Opus 4.1 (exceptional for specialized complex tasks). Organized into four sections: Get Started (setup, model overview, prompt library), Develop with Claude (Console, API Reference, Cookbook), Key Capabilities (text/code generation, vision), and Support (Help Center, Service Status). Serves as the primary navigation hub for all Claude documentation.

### **legacy-model-guide.md**
Complete model reference featuring Claude Sonnet 4.5 and Claude Opus 4.1 with comprehensive tables showing model names across platforms (Claude API, AWS Bedrock, GCP Vertex AI), model aliases (claude-sonnet-4-5, claude-opus-4-1, etc.), detailed feature comparison table (strengths, capabilities, latency, context windows, max output, knowledge cutoffs), and per-model pricing with cache write/hit rates. Notes that models with identical snapshot dates are consistent across platforms, and starting with Sonnet 4.5, AWS Bedrock and Google Vertex AI offer both global and regional endpoints. Includes migration guidance to Claude 4 and links to quickstart resources.

### **mcp.md**
High-level introduction to Model Context Protocol (MCP) as an open protocol standardizing how applications provide context to LLMs. Compares MCP to USB-C as a universal connector for AI applications. Links to external MCP documentation at modelcontextprotocol.io for building servers and clients. Lists MCP integration across Anthropic products: Messages API (MCP connector for remote servers), Claude Code (server management and client usage), Claude.ai (team connectors), and Claude Desktop (local server configuration).

### **models-overview.md**
Identical to legacy-model-guide.md. Central model reference with comprehensive comparison tables, pricing structures, and capabilities for all Claude models. Features Claude Sonnet 4.5 and Claude Opus 4.1 with detailed tables showing API names across platforms, model aliases for development convenience, feature comparison (description, strengths, multilingual support, vision, extended thinking, latency, context windows, max output, knowledge cutoffs), and complete pricing breakdown for input tokens, cache writes (5-minute and 1-hour), cache hits/refreshes, and output tokens. Includes prompt/output performance characteristics and migration guidance to Claude 4.

### **overview.md**
Duplicate of intro-to-claude.md. Comprehensive introduction covering Claude's capabilities (text/code generation for production-level code and complex financial forecasts, vision for chart analysis and image-to-code generation, tool use for external integrations), enterprise features (security, trustworthiness, 200K token context window, reliability, global fluency, cost optimization), and the complete 8-step implementation workflow from scoping use cases through monitoring production deployments. Links to quickstart, API reference, prompt library, Workbench, and Claude Cookbook.

### **prompt-generator.md**
Documentation for the prompt generation tool that guides Claude to create high-quality prompt templates following best practices. Compatible with all Claude models including extended thinking capabilities. The tool helps solve the "blank page problem" and provides jumping-off points for further testing and iteration. Available directly in the Console dashboard. Links to the prompt generator Google Colab notebook for analyzing underlying architecture and running code to construct prompts. Next steps include prompt engineering guide, prompt library, GitHub prompting tutorial, and Google Sheets interactive tutorial.

### **system-prompts.md**
Comprehensive guide to using the system parameter for role prompting, the most powerful way to use system prompts with Claude. Explains why role prompting enhances accuracy (especially in legal/financial contexts), tailors tone (CFO brevity vs copywriter flair), and improves focus. Provides implementation examples using the Messages API system parameter with detailed before/after comparisons for legal contract analysis (missing critical issues without role, catching million-dollar risks with role) and financial analysis (surface-level analysis without role, actionable strategic insights with role). Links to prompt library and tutorials.

### **tool-use.md**
Foundational overview of Claude's tool use capabilities distinguishing client tools (user-defined custom tools and Anthropic-defined tools like computer use/text editor that execute on client systems) from server tools (web search/web fetch that execute on Anthropic servers). Explains the complete workflow for client tools (provide tools, Claude decides, execute and return results, Claude formulates response) and server tools (provide tools, Claude executes automatically, Claude formulates response). Provides code examples demonstrating single tool usage, parallel tool use (multiple independent operations), multiple tool selection, missing information handling, sequential tools (chained operations), chain of thought tool use, and JSON mode for structured output. Covers pricing including tool use system prompt token counts by model and tool_choice type. Links to cookbooks for calculator tool, customer service agent, and JSON extractor implementations.

## Subdirectories

### **about-claude/**
Model information, pricing, terminology, and production use cases for Claude
- glossary.md: Comprehensive definitions of key Claude and LLM terms including context windows, fine-tuning, HHH principles, tokens, and RAG
- model-deprecations.md: Model lifecycle stages (Active, Legacy, Deprecated, Retired) with 60-day notice policy and deprecation history
- models.md: Central model reference with platform names, aliases, feature comparisons, and pricing across Claude API/AWS/GCP
- pricing.md: Detailed pricing for all models, features, deployment scenarios including batch, long context, tools, and volume discounts
- use-case-guides.md: Index linking to production guides for ticket routing, customer support, content moderation, and legal summarization
- models/: Detailed model selection, capabilities, migration guides, and extended thinking documentation
- use-case-guides/: Production implementation guides with best practices and deployment strategies

### **agents-and-tools/**
Claude's agent capabilities, tool ecosystem, MCP implementation, and Google Sheets integration
- claude-for-sheets.md: Google Workspace extension with CLAUDE() and CLAUDEMESSAGES() functions for prompt engineering at scale
- mcp-connector.md: Beta MCP connector for connecting to remote MCP servers directly from Messages API
- mcp.md: High-level MCP introduction as open protocol for standardizing LLM context provision
- remote-mcp-servers.md: Third-party remote MCP servers categorized by function (development, project management, databases, payments, etc.)
- tool-use/: Client-side and server-side tools including bash, code execution, computer use, web search, and text editor

### **build-with-claude/**
Core capabilities, API features, tools, and prompt engineering for building Claude applications
- batch-processing.md: Message Batches API for asynchronous processing at 50% cost reduction with up to 100,000 requests per batch
- citations.md: Source references for documents with automatic chunking and cited text extraction
- context-editing.md: Beta feature for automatic conversation context management by clearing tool results near token thresholds
- context-windows.md: 200K standard capacity growing linearly with conversation turns, 1M beta for Sonnet 4/4.5 with premium pricing
- define-success.md: Framework for establishing measurable success criteria across multiple dimensions
- develop-tests.md: Designing evaluation test cases with automated grading strategies and edge case coverage
- embeddings.md: Voyage AI embedding recommendations with model options and implementation guidance
- extended-thinking.md: Enhanced reasoning with configurable token budgets, streaming support, and tool use integration
- files.md: Beta Files API for uploading and managing files without re-uploading content with each request
- multilingual-support.md: Robust multilingual capabilities with performance data across 14 languages
- overview.md: Comprehensive reference table of all Claude capabilities and tools across deployment platforms
- pdf-support.md: Analyze PDFs up to 100 pages with text and visual content extraction
- prompt-caching.md: Cache prompt prefixes with 5-minute or 1-hour lifetime for cost optimization
- prompt-engineering.md: Overview establishing prompt engineering techniques from most to least broadly effective
- search-results.md: Natural citations with source attribution for RAG applications
- streaming.md: Incremental response streaming via server-sent events with delta types and error recovery
- text-generation.md: Text capabilities including summarization, content generation, data extraction, and code explanation
- token-counting.md: Count tokens before sending to manage rate limits and costs
- tool-use.md: Complete tool use implementation with client/server tools, parallel/sequential patterns, and pricing
- vision.md: Image analysis via API with up to 100 images, base64/URL support, and optimization guidance
- prompt-engineering/: Comprehensive prompt engineering techniques including clarity, examples, chain of thought, and XML tags

### **claude-code/**
Anthropic's official CLI tool for AI-powered coding assistance with comprehensive configuration and deployment documentation
- amazon-bedrock.md: Complete Bedrock configuration guide with IAM policies, credential setup, and inference profiles
- analytics.md: Dashboard metrics for organization usage including lines of code accepted and spend tracking
- bedrock-vertex-proxies.md: Deployment options comparing Anthropic API, Bedrock, and Vertex AI with proxy/gateway configuration
- checkpointing.md: Automatic code state tracking with undo/rewind capabilities persisting for 30 days
- cli-reference.md: Complete CLI commands and flags including directory access, custom subagents, and permission management
- common-workflows.md: Practical workflows for understanding codebases, fixing bugs, refactoring, tests, PRs, and custom commands
- costs.md: Cost tracking with $6/developer/day average, usage monitoring, workspace limits, and optimization strategies
- data-usage.md: Data policies, retention periods (5-year with opt-in, 30-day standard), and flow documentation
- devcontainer.md: Production-ready Node.js development container with security-focused network restrictions
- github-actions.md: GitHub Actions integration for PR creation, automated implementation, and bug fixes via @claude mentions
- gitlab-ci-cd.md: GitLab CI/CD beta integration with instant MR creation and project-aware changes
- google-vertex-ai.md: Vertex AI configuration with GCP credentials, IAM permissions, and quota management
- headless.md: Non-interactive programmatic usage with output formats for scripts and automation
- hooks-guide.md: User-defined shell commands executing at lifecycle points for notifications, formatting, and logging
- hooks.md: Complete hooks reference with event types, input/output schemas, and security considerations
- iam.md: Authentication methods, permission system with tiered approval, and credential management
- ide-integrations.md: VS Code extension (beta) with sidebar panel, plan mode, auto-accept edits, and keyboard shortcuts
- interactive-mode.md: Keyboard shortcuts, multiline input methods, quick commands, and vim editor mode
- jetbrains.md: JetBrains plugin for IntelliJ IDEA, PyCharm, WebStorm with quick launch and diff viewing
- legal-and-compliance.md: Commercial/Consumer Terms, BAA healthcare compliance, and security vulnerability reporting
- llm-gateway.md: LiteLLM configuration for centralized proxy layer with authentication and usage tracking
- mcp.md: MCP integration with server installation, OAuth authentication, and enterprise configuration
- memory.md: CLAUDE.md file hierarchy (Enterprise, Project, User, Local) with imports and best practices
- model-config.md: Model configuration with aliases, setting methods, and extended context options
- monitoring-usage.md: OpenTelemetry metrics (beta) for session count, cost, tokens, and ROI measurement
- network-config.md: Enterprise network configurations including proxy, custom CA certificates, and mTLS authentication
- output-styles.md: Built-in and custom output styles modifying Claude's system prompt for different behaviors
- overview.md: 30-second installation guide and feature overview highlighting terminal-native, action-taking capabilities
- quickstart.md: 5-minute getting started guide from installation through first code changes and Git usage
- sdk.md: SDK migration guide from Claude Code SDK to Claude Agent SDK with breaking changes
- security.md: SOC 2/ISO 27001 foundation, permission-based architecture, prompt injection protections, and best practices
- settings.md: Comprehensive configuration covering settings files hierarchy, environment variables, and subagent configuration
- setup.md: System requirements, installation methods (npm, native binary), authentication options, and auto-updates
- slash-commands.md: Built-in commands and custom command creation with arguments, bash execution, and file references
- statusline.md: Custom status line configuration displaying session context at bottom of interface
- sub-agents.md: Specialized AI assistants with task-specific configurations, separate context windows, and reusability
- terminal-config.md: Terminal appearance, themes, line breaks, notifications, and large input handling
- third-party-integrations.md: Deployment options overview comparing providers with configuration examples
- troubleshooting.md: Common installation, permission, authentication, and performance issues with solutions
- vs-code.md: VS Code extension documentation (identical to ide-integrations.md)
- sdk/: SDK migration guides and headless operation documentation

### **test-and-evaluate/**
Complete workflow for testing and evaluating Claude applications from success criteria to evaluation tooling
- define-success.md: Establishing clear, measurable success criteria with quantitative metrics and qualitative scales
- develop-tests.md: Designing test cases with automation strategies including exact match, similarity, ROUGE-L, and LLM-based grading
- eval-tool.md: Claude Console's Evaluation tool for prompt testing, version comparison, and iterative refinement
