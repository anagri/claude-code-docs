# Directory: Claude Code Documentation (Root)

## Overview
This is the complete documentation collection for Claude AI and Claude Code, covering the developer platform API, the Claude Code CLI tool, model capabilities, agent development, and all associated tools and resources.

## Files in This Directory

### **api.md**
Entry point documentation for accessing the Claude API through the Anthropic Console. Covers authentication using x-api-key header, JSON content-type requirements, and request size limits (32MB for Messages/Token Counting, 256MB for Batch API, 500MB for Files API). Includes response headers for debugging (request-id, anthropic-organization-id) and basic usage examples in cURL, Python, and TypeScript for making Messages API calls.

### **docs.md**
Main landing page introducing the Claude model family, highlighting Claude Sonnet 4.5 (best for complex agents and coding with highest intelligence) and Claude Opus 4.1 (exceptional for specialized complex tasks requiring advanced reasoning). Organized into three sections: Get Started (setup, model learning, prompt library), Develop with Claude (Console, API Reference, Cookbook), and Key Capabilities (text/code generation, vision). Links to Help Center and Service Status for support.

### **index.md**
Homepage for all Claude documentation providing navigation to two main product areas: Claude Developer Platform (API getting started, features overview, Claude Sonnet 4.5 updates, API reference, Console access, release notes) and Claude Code (quickstart guide, reference documentation, changelog). Also includes links to learning resources: Anthropic Courses, Claude Cookbook GitHub repository, and Claude Quickstarts deployable applications.

## Subdirectories

### **api/**
Comprehensive API reference documentation for Claude's APIs, including Messages API, Admin API, Usage & Cost APIs, Agent SDK, and third-party platform integrations
- administration-api.md: Complete Admin API guide for organization management, user/workspace administration, API key lifecycle
- agent-sdk/: TypeScript and Python SDK documentation for building production AI agents
- beta-headers.md: Accessing experimental features using anthropic-beta header
- client-sdks.md: Official SDKs for 7 languages with installation and authentication patterns
- errors.md: Error handling guide with HTTP codes, error types, and debugging strategies
- messages.md: Complete Messages API reference with all parameters, streaming, tools, and configuration
- rate-limits.md: Usage tiers, token bucket algorithm, rate limit headers, and workspace limits
- service-tiers.md: Standard vs Priority tier options with reliability and pricing differences
- usage-cost-api.md: Programmatic access to token consumption and cost breakdowns

### **docs/**
Comprehensive hub covering Claude models, API features, Claude Code CLI, agent development, and production deployment strategies
- about-claude/: Model information, pricing, terminology, production use cases, and deprecation policies
- agents-and-tools/: Claude's agent capabilities, MCP implementation, Google Sheets integration, and tool ecosystem
- build-with-claude/: Core capabilities including batch processing, citations, extended thinking, files, PDFs, prompt engineering
- claude-code/: Complete CLI documentation for installation, configuration, IDE integrations, GitHub Actions, and enterprise deployment
- get-started.md: Quick start guide for making first API call with prerequisites and next steps
- models-overview.md: Central model reference with platform names, aliases, feature comparisons, and pricing
- prompt-generator.md: Tool for creating high-quality prompt templates following best practices
- test-and-evaluate/: Testing workflow from success criteria to evaluation tooling

### **release-notes/**
Release notes and changelog documentation for Claude products including API, web/mobile apps, Claude Code CLI, and system prompts
- api.md: Developer Platform API changelog from May 2024-September 2025 covering Claude 4 models, Files API, MCP connector, web tools
- claude-apps.md: Web and mobile app release history including Sonnet 4.5, custom instructions, Styles, Analysis tool, Projects, Artifacts
- claude-code.md: Reference to complete CHANGELOG.md in claude-code GitHub repository
- system-prompts.md: Archive of system prompts used across Claude models from Haiku 3 through Sonnet 4.5

### **resources/**
Development resources including quickstarts, courses, code examples, prompt templates, and model documentation
- overview.md: Central hub listing quickstarts, Skilljar courses, Cookbook, prompt library, API primer, model/system cards
- prompt-library/: 60+ ready-to-use prompt templates for coding, data analysis, creative writing, and business applications
- prompt-library.md: Introduction to optimized prompts for business and personal tasks
