# Directory: about-claude

## Overview
This directory provides comprehensive information about Claude's models, pricing, terminology, and production use cases. It covers model selection, deprecation policies, pricing structures, and real-world implementation guides.

## Files in This Directory

### **glossary.md**
A comprehensive glossary of key terms and concepts related to Claude and large language models. Defines fundamental concepts including context windows (working memory for models), fine-tuning (additional training on specialized data), HHH principles (helpful, honest, harmless AI goals), latency and TTFT (time to first token), LLMs (large language models), MCP and MCP connector (Model Context Protocol for standardized context sharing), pretraining (initial training on large text corpora), RAG (retrieval augmented generation for grounding responses in external knowledge), RLHF (reinforcement learning from human feedback), temperature (randomness control parameter), and tokens (smallest units of text processed by models, approximately 3.5 characters in English).

### **model-deprecations.md**
Documentation of Claude's model lifecycle and deprecation policy. Defines four lifecycle stages: Active (fully supported), Legacy (no longer updated), Deprecated (available to existing users with assigned retirement date), and Retired (no longer available). Provides 60-day advance notice before retirements and recommends migration to active models. Includes comprehensive status table for all publicly released models, showing current state, deprecation dates, and retirement dates. Features detailed deprecation history with recommended replacements for each deprecated model. Provides guidance on auditing model usage via Console export, best practices for migration testing, and links to Claude 4 migration instructions.

### **models.md**
Central reference for Claude's model lineup featuring Claude Sonnet 4.5 (best for complex agents and coding) and Claude Opus 4.1 (exceptional for specialized complex tasks). Contains comprehensive tables showing model names across platforms (Claude API, AWS Bedrock, GCP Vertex AI), model aliases for development convenience, detailed feature comparison (strengths, capabilities, latency, context windows, max output, knowledge cutoffs), and per-model pricing including base input, cache writes (5m and 1h durations), cache hits, and output tokens. Notes that models with identical snapshot dates are consistent across platforms, and starting with Sonnet 4.5, AWS Bedrock and Google Vertex AI offer both global and regional endpoints. Includes migration guidance to Claude 4 and links to quickstart resources.

### **pricing.md**
Detailed pricing information for all Claude models, features, and deployment scenarios. Covers standard model pricing across all tiers with detailed breakdowns for input tokens, cache writes (5-minute and 1-hour durations), cache hits/refreshes, and output tokens. Explains third-party platform pricing for AWS Bedrock and Google Vertex AI, including new global vs regional endpoint options (regional endpoints have 10% premium for Sonnet 4.5 and future models). Provides feature-specific pricing for batch processing (50% discount), long context (premium rates for requests exceeding 200K input tokens with 1M context window beta), tool use (client-side and server-side pricing), and specific tools (bash, code execution at $0.05/session-hour, text editor, web search at $10/1000 searches, web fetch at no additional cost, computer use). Includes real-world agent use case pricing examples for customer support agents and general agent workflows, cost optimization strategies, rate limit tiers, volume discount information, enterprise pricing options, and billing/payment details.

### **use-case-guides.md**
Index page introducing production-ready implementation guides for common Claude use cases. Links to four comprehensive guides: Ticket Routing (classify and route customer support tickets at scale), Customer Support Agent (build intelligent context-aware chatbots), Content Moderation (content filtering and moderation techniques), and Legal Summarization (extract key information from legal documents to expedite research). Each guide provides detailed best practices for building these production applications with Claude.

## Subdirectories

### **models/**
Detailed documentation about Claude model selection, capabilities, migration, and advanced features like extended thinking
- choosing-a-model.md: Framework for selecting the appropriate Claude model based on capabilities, speed, and cost criteria with model selection matrix
- extended-thinking-models.md: Comprehensive technical documentation on extended thinking feature with configurable token budgets and streaming support
- migrating-to-claude-4.md: Step-by-step migration guide from Claude 3.7 to Claude 4 with API changes and behavioral differences
- overview.md: Central model reference with comparison tables, pricing, and capabilities for all Claude models across platforms
- whats-new-sonnet-4-5.md: Release notes highlighting Sonnet 4.5's coding excellence, agent capabilities, and new API features

### **use-case-guides/**
Production implementation guides with best practices, code examples, and deployment strategies for common use cases
- customer-support-chat.md: Guide for building intelligent customer support chatbots with tool use, RAG, and streaming deployment
- content-moderation.md: Content moderation system implementation with semantic understanding and multilingual support
- legal-summarization.md: Legal document summarization for metadata extraction and research with meta-summarization techniques
- ticket-routing.md: Automated support ticket classification and routing with hierarchical classification strategies
