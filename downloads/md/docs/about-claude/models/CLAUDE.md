# Directory: models

## Overview
This directory contains comprehensive documentation about Claude's model lineup, including model selection guidance, capabilities comparison, migration instructions, and detailed information about extended thinking features and the latest Sonnet 4.5 release.

## Files in This Directory

### **choosing-a-model.md**
Provides a framework for selecting the appropriate Claude model based on specific needs. The guide recommends establishing key criteria first: capabilities, speed, and cost. It presents two approaches for model selection: starting with a fast, cost-effective model like Claude 3.5 Haiku for prototyping and high-volume tasks, or beginning with the most capable model (Claude Sonnet 4.5) for complex reasoning and advanced coding. The document includes a detailed model selection matrix that matches use cases to recommended models, ranging from complex autonomous coding agents (Sonnet 4.5) to basic customer support (Haiku 3.5). It emphasizes the importance of creating benchmark tests specific to your use case and provides guidance on deciding whether to upgrade or change models based on performance metrics.

### **extended-thinking-models.md**
Comprehensive technical documentation on Claude's extended thinking feature, which provides enhanced reasoning capabilities for complex tasks with varying levels of transparency into the step-by-step thought process. Extended thinking is supported in Claude Opus 4.1, Opus 4, Sonnet 4.5, Sonnet 4, and Sonnet 3.7. Key topics covered include:

- **Basic usage**: Enabling extended thinking via the `thinking` parameter with configurable token budgets, where larger budgets enable more thorough analysis
- **Summarized thinking**: Claude 4 models return summaries of the full thinking process (with billing based on full tokens, not summary tokens), while Claude Sonnet 3.7 returns full thinking output
- **Streaming**: Support for server-sent events (SSE) with `thinking_delta` events for real-time delivery
- **Tool use integration**: Detailed explanation of how extended thinking works with tool calls, including the requirement to preserve complete thinking blocks when passing tool results back to the API
- **Interleaved thinking**: Beta feature for Claude 4 models (requires `interleaved-thinking-2025-05-14` header) that enables Claude to reason between tool calls, creating sophisticated reasoning chains
- **Prompt caching**: Important considerations about how thinking blocks affect cache breakpoints and invalidation patterns
- **Context window management**: How thinking tokens are counted and managed, with thinking blocks from previous turns stripped from context
- **Thinking encryption**: Technical details about the `signature` field used to verify thinking blocks, plus handling of `redacted_thinking` blocks when safety systems flag internal reasoning
- **Best practices**: Recommendations for budget optimization, performance considerations, feature compatibility, and when to use extended thinking

Includes extensive code examples in multiple languages (Shell, Python, TypeScript, Java) demonstrating implementation patterns.

### **migrating-to-claude-4.md**
Step-by-step migration guide for transitioning from Claude 3.7 models to Claude 4 models (Opus 4.1 and Sonnet 4.5). The basic migration is simple - just update the model name - but the document highlights important changes:

- **New refusal stop reason**: Claude 4 introduces a `refusal` stop reason for safety-declined content
- **Summarized thinking**: Claude 4 returns thinking summaries instead of full output (though billing is for full tokens)
- **Interleaved thinking**: Beta feature enabling tool use mixed with reasoning steps
- **Behavioral differences**: Claude 4 is more concise, direct, and natural in communication style; requires more explicit instructions (e.g., "Make these changes" vs "Can you suggest")
- **Updated tools**: Text editor tool changed to `text_editor_20250728` with name `str_replace_based_edit_tool` (no more `undo_edit`); code execution tool updated to `code_execution_20250825`
- **Removed features**: Token-efficient tool use and extended output (128k) no longer supported in Claude 4
- **Performance recommendations**: Choose Sonnet 4.5 for long-running agents, coding, and large context workflows; choose Opus 4.1 for specialized complex tasks where speed is not critical
- **Extended thinking impact**: Strong recommendation to enable extended thinking for complex tasks, with warning about prompt caching efficiency trade-offs

Includes a comprehensive migration checklist covering all necessary updates and testing steps.

### **overview.md**
Central reference for Claude's model lineup, providing comprehensive comparison tables, pricing, and capabilities. Highlights the two flagship models:

- **Claude Sonnet 4.5**: Best model for complex agents and coding, with highest intelligence across most tasks, 200K context window (1M beta available), 64K max output
- **Claude Opus 4.1**: Exceptional for specialized complex tasks, superior reasoning capabilities, 200K context window, 32K max output

The document includes detailed tables showing:
- **Model names** across platforms (Claude API, AWS Bedrock, GCP Vertex AI)
- **Model aliases** for development/testing that auto-update to newest snapshots
- **Feature comparison** covering strengths, multilingual support, vision, extended thinking, latency, context windows, max output, knowledge cutoffs, and training data cutoffs
- **Pricing** for all models showing base input, cache writes (5m and 1h durations), cache hits, and output tokens

Key information about model capabilities, migration guidance, and links to getting started resources. Notes that models with the same snapshot date are identical across all platforms, and starting with Sonnet 4.5, AWS Bedrock and Google Vertex AI offer both global and regional endpoints.

### **whats-new-sonnet-4-5.md**
Detailed release notes for Claude Sonnet 4.5, highlighting key improvements and new features:

**Coding excellence:**
- Advanced state-of-the-art SWE-bench Verified performance
- Enhanced planning, system design, and security engineering
- Improved instruction following
- Significantly better performance when extended thinking is enabled (though it impacts prompt caching efficiency)

**Agent capabilities:**
- Extended autonomous operation for hours while maintaining clarity and incremental progress
- Context awareness: tracks token usage throughout conversations to prevent premature task abandonment
- Enhanced tool usage with effective parallel tool calls for simultaneous searches and file reading
- Advanced context management with exceptional state tracking in external files

**Communication and interaction:**
- More concise, direct, and natural communication style
- Fact-based progress updates with less verbose summaries (adjustable via prompting)

**Creative content generation:**
- Matches/exceeds Opus 4.1 for presentations, animations, and visual content
- Strong instruction following with polished, professional output

**New API features:**
- Memory tool (beta, requires `context-management-2025-06-27` header): enables storing/retrieving information outside context window
- Context editing: automatic tool call clearing for intelligent context management
- New `model_context_window_exceeded` stop reason for explicit context window limit detection
- Improved tool parameter handling: preserves intentional formatting including trailing newlines
- Token count optimizations that don't affect billing

**Pricing and availability:**
- Same pricing as Sonnet 4: $3/MTok input, $15/MTok output
- Available on Claude API, Amazon Bedrock, Google Cloud Vertex AI, Claude.ai, and Claude Code
