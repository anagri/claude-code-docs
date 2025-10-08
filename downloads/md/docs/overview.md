url: https://docs.claude.com/en/docs/overview

---

This guide introduces Claude’s enterprise capabilities, the end-to-end flow for developing with Claude, and how to start building.

## What you can do with Claude

Claude is designed to empower enterprises at scale with strong performance across benchmark evaluations for reasoning, math, coding, and fluency in English and non-English languages. Here’s a non-exhaustive list of Claude’s capabilities and common uses. Capability| Enables you to…
---|---
Text and code generation|

  * Adhere to brand voice for excellent customer-facing experiences such as copywriting and chatbots
  * Create production-level code and operate \(in-line code generation, debugging, and conversational querying\) within complex codebases
  * Build automatic translation features between languages
  * Conduct complex financial forecasts
  * Support legal use cases that require high-quality technical analysis, long context windows for processing detailed documents, and fast outputs

Vision|

  * Process and analyze visual input, such as extracting insights from charts and graphs
  * Generate code from images with code snippets or templates based on diagrams
  * Describe an image for a user with low vision

Tool use|

  * Interact with external client-side tools and functions, allowing Claude to reason, plan, and execute actions by generating structured outputs through API calls

## Enterprise considerations

Along with an extensive set of features, tools, and capabilities, Claude is also built to be secure, trustworthy, and scalable for wide-reaching enterprise needs. Feature| Description
---|---
**Secure**|

  * [Enterprise-grade](https://trust.anthropic.com/) security and data handling for API
  * SOC II Type 2 certified, HIPAA compliance options for API
  * Accessible through AWS \(GA\) and GCP \(in private preview\)

**Trustworthy**|

  * Resistant to jailbreaks and misuse. We continuously monitor prompts and outputs for harmful, malicious use cases that violate our [AUP](https://www.anthropic.com/legal/aup).
  * Copyright indemnity protections for paid commercial services
  * Uniquely positioned to serve high trust industries that process large volumes of sensitive user data

**Capable**|

  * 200K token context window for expanded use cases, with future support for 1M
  * [Tool use](/en/docs/agents-and-tools/tool-use/overview), also known as function calling, which allows seamless integration of Claude into specialized applications and custom workflows
  * Multimodal input capabilities with text output, allowing you to upload images \(such as tables, graphs, and photos\) along with text prompts for richer context and complex use cases
  * [Developer Console](https://console.anthropic.com) with Workbench and prompt generation tool for easier, more powerful prompting and experimentation
  * [SDKs](/en/api/client-sdks) and [APIs](/en/api) to expedite and enhance development

**Reliable**|

  * Very low hallucination rates
  * Accurate over long documents

**Global**|

  * Great for coding tasks and fluency in English and non-English languages like Spanish and Japanese
  * Enables use cases like translation services and broader global utility

**Cost conscious**|

  * Family of models balances cost, performance, and intelligence

## Implementing Claude

1

Scope your use case

  * Identify a problem to solve or tasks to automate with Claude.
  * Define requirements: features, performance, and cost.

2

Design your integration

  * Select Claude’s capabilities \(e.g., vision, tool use\) and models \(Opus, Sonnet, Haiku\) based on needs.
  * Choose a deployment method, such as the Claude API, AWS Bedrock, or Vertex AI.

3

Prepare your data

  * Identify and clean relevant data \(databases, code repos, knowledge bases\) for Claude’s context.

4

Develop your prompts

  * Use Workbench to create evals, draft prompts, and iteratively refine based on test results.
  * Deploy polished prompts and monitor real-world performance for further refinement.

5

Implement Claude

  * Set up your environment, integrate Claude with your systems \(APIs, databases, UIs\), and define human-in-the-loop requirements.

6

Test your system

  * Conduct red teaming for potential misuse and A/B test improvements.

7

Deploy to production

  * Once your application runs smoothly end-to-end, deploy to production.

8

Monitor and improve

  * Monitor performance and effectiveness to make ongoing improvements.

## Start building with Claude

When you’re ready, start building with Claude:

  * Follow the [Quickstart](/en/resources/quickstarts) to make your first API call
  * Check out the [API Reference](/en/api)
  * Explore the [Prompt Library](/en/resources/prompt-library/library) for example prompts
  * Experiment and start building with the [Workbench](https://console.anthropic.com)
  * Check out the [Claude Cookbook](https://github.com/anthropics/anthropic-cookbook) for working code examples

Was this page helpful?

YesNo

[Features overview](/en/docs/build-with-claude/overview)[Context windows](/en/docs/build-with-claude/context-windows)
