# Directory: release-notes

## Overview
This directory contains release notes and changelog documentation for Claude products, including the developer platform API, web and mobile applications, Claude Code CLI, and system prompts used across different Claude models.

## Files in This Directory

### **api.md**
Comprehensive changelog for the Claude Developer Platform API and Console, documenting feature releases, SDK updates, and platform changes from May 2024 through September 2025. Key releases include Claude 4 model family (Sonnet 4.5, Opus 4.1, Sonnet 4, Opus 4) with extended thinking capabilities, the Files API, Code Execution tool, MCP connector, web search and web fetch tools, memory tool, context editing, search result content blocks for RAG applications, prompt caching with 1-hour cache duration, Message Batches API for 50% cost reduction, Token Counting API, Admin API, Usage & Cost API, Claude Code Analytics API, fine-grained tool streaming, and multiple official SDK releases (Java, Go, Ruby, PHP, C#). Platform improvements include unified Claude branding (console moved to platform.claude.com), rate limit monitoring charts, OpenAI-compatible endpoints, URL source blocks for images/PDFs, citations capability, and enhanced tool use features including parallel tool execution and citable documents in tool results.

### **claude-apps.md**
Release history for Claude's web interface (claude.ai) and mobile/desktop applications from May 2024 to September 2025. Major updates include the addition of Claude Sonnet 4.5 (September 2025), Claude Opus 4.1 (August 2025), Claude Sonnet 4 (May 2025), and Claude Sonnet 3.7 with extended thinking (February 2025). Features introduced include custom instructions (December 2024), Styles for response customization (November 2024), Analysis tool for code execution and data analysis with Excel support up to 30MB (October 2024), Projects for knowledge grounding (June 2024), and Artifacts for generating interactive content (June 2020). Platform expansions include desktop applications for Windows and Mac (October 2024), Android app (July 2024), iOS app (May 2024), and availability in Canada and Europe. Additional features include Google Docs integration, voice dictation, LaTeX rendering, screenshot capture, and enhanced PDF support with visual analysis.

### **claude-code.md**
Brief reference page directing users to the complete CHANGELOG.md file in the claude-code GitHub repository for detailed version information and changelogs about Claude Code releases.

### **overview.md**
Landing page providing navigation links to three main release note categories: Claude Developer Platform updates (API and Console enhancements), Claude Apps updates (web and mobile application features), and System Prompt updates (default prompts used in Claude's applications).

### **system-prompts.md**
Archive of system prompts used in Claude's web interface (claude.ai) and mobile applications, documenting the evolution of prompts across different model versions from Claude Haiku 3 through Claude Sonnet 4.5. Each entry includes the release date and complete system prompt text that provides Claude with contextual information (current date, model capabilities, product details), behavioral instructions (refusal handling for harmful content, tone and formatting guidelines, user wellbeing considerations), knowledge cutoff information (January 2025), and specific guidance on handling various conversation types. The prompts define how Claude should respond in the consumer applications, including information about available Anthropic products (Claude API, Claude Code CLI), appropriate formatting for different conversation contexts, content restrictions for child safety and malicious use cases, and empathetic response patterns for emotional or advice-driven conversations.
