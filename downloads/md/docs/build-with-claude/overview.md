url: https://docs.claude.com/en/docs/build-with-claude/overview

---

## Core capabilities

These features enhance Claude’s fundamental abilities for processing, analyzing, and generating content across various formats and use cases. Feature| Description| Availability
---|---|---
[1M token context window](/en/docs/build-with-claude/context-windows#1m-token-context-window)| An extended context window that allows you to process much larger documents, maintain longer conversations, and work with more extensive codebases.| Claude API \(Beta\)

Amazon Bedrock \(Beta\)

Google Cloud's Vertex AI \(Beta\)
[Batch processing](/en/docs/build-with-claude/batch-processing)| Process large volumes of requests asynchronously for cost savings. Send batches with a large number of queries per batch. Batch API calls costs 50% less than standard API calls.| Claude API

Amazon Bedrock

Google Cloud's Vertex AI
[Citations](/en/docs/build-with-claude/citations)| Ground Claude’s responses in source documents. With Citations, Claude can provide detailed references to the exact sentences and passages it uses to generate responses, leading to more verifiable, trustworthy outputs.| Claude API

Amazon Bedrock

Google Cloud's Vertex AI
[Context editing](/en/docs/build-with-claude/context-editing)| Automatically manage conversation context with configurable strategies. Currently supports clearing older tool results and calls when approaching token limits.| Claude API \(Beta\)

Amazon Bedrock \(Beta\)

Google Cloud's Vertex AI \(Beta\)
[Extended thinking](/en/docs/build-with-claude/extended-thinking)| Enhanced reasoning capabilities for complex tasks, providing transparency into Claude’s step-by-step thought process before delivering its final answer.| Claude API

Amazon Bedrock

Google Cloud's Vertex AI
[Files API](/en/docs/build-with-claude/files)| Upload and manage files to use with Claude without re-uploading content with each request. Supports PDFs, images, and text files.| Claude API \(Beta\)
[PDF support](/en/docs/build-with-claude/pdf-support)| Process and analyze text and visual content from PDF documents.| Claude API

Amazon Bedrock

Google Cloud's Vertex AI
[Prompt caching \(5m\)](/en/docs/build-with-claude/prompt-caching)| Provide Claude with more background knowledge and example outputs to reduce costs and latency.| Claude API

Amazon Bedrock

Google Cloud's Vertex AI
[Prompt caching \(1hr\)](/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration)| Extended 1-hour cache duration for less frequently accessed but important context, complementing the standard 5-minute cache.| Claude API
[Search results](/en/docs/build-with-claude/search-results)| Enable natural citations for RAG applications by providing search results with proper source attribution. Achieve web search-quality citations for custom knowledge bases and tools.| Claude API

Google Cloud's Vertex AI
[Token counting](/en/api/messages-count-tokens)| Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage.| Claude API

Amazon Bedrock

Google Cloud's Vertex AI
[Tool use](/en/docs/agents-and-tools/tool-use/overview)| Enable Claude to interact with external tools and APIs to perform a wider variety of tasks. For a list of supported tools, see the Tools table.| Claude API

Amazon Bedrock

Google Cloud's Vertex AI

## Tools

These features enable Claude to interact with external systems, execute code, and perform automated tasks through various tool interfaces. Feature| Description| Availability
---|---|---
[Bash](/en/docs/agents-and-tools/tool-use/bash-tool)| Execute bash commands and scripts to interact with the system shell and perform command-line operations.| Claude API

Amazon Bedrock

Google Cloud's Vertex AI
[Code execution](/en/docs/agents-and-tools/tool-use/code-execution-tool)| Run Python code in a sandboxed environment for advanced data analysis.| Claude API \(Beta\)
[Computer use](/en/docs/agents-and-tools/tool-use/computer-use-tool)| Control computer interfaces by taking screenshots and issuing mouse and keyboard commands.| Claude API \(Beta\)

Amazon Bedrock \(Beta\)

Google Cloud's Vertex AI \(Beta\)
[Fine-grained tool streaming](/en/docs/agents-and-tools/tool-use/fine-grained-tool-streaming)| Stream tool use parameters without buffering/JSON validation, reducing latency for receiving large parameters.| Claude API

Amazon Bedrock

Google Cloud's Vertex AI
[MCP connector](/en/docs/agents-and-tools/mcp-connector)| Connect to remote [MCP](/en/docs/agents-and-tools/mcp) servers directly from the Messages API without a separate MCP client.| Claude API \(Beta\)
[Memory](/en/docs/agents-and-tools/tool-use/memory-tool)| Enable Claude to store and retrieve information across conversations. Build knowledge bases over time, maintain project context, and learn from past interactions.| Claude API \(Beta\)

Amazon Bedrock \(Beta\)

Google Cloud's Vertex AI \(Beta\)
[Text editor](/en/docs/agents-and-tools/tool-use/text-editor-tool)| Create and edit text files with a built-in text editor interface for file manipulation tasks.| Claude API

Amazon Bedrock

Google Cloud's Vertex AI
[Web fetch](/en/docs/agents-and-tools/tool-use/web-fetch-tool)| Retrieve full content from specified web pages and PDF documents for in-depth analysis.| Claude API \(Beta\)
[Web search](/en/docs/agents-and-tools/tool-use/web-search-tool)| Augment Claude’s comprehensive knowledge with current, real-world data from across the web.| Claude API

Was this page helpful?

YesNo

[Pricing](/en/docs/about-claude/pricing)[Building with Claude](/en/docs/overview)
