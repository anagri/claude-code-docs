# Directory: test-and-evaluate

## Overview
This directory covers the complete workflow for testing and evaluating Claude-based applications, from defining measurable success criteria to developing comprehensive test suites and using the Console's Evaluation tool for iterative prompt improvement.

## Files in This Directory

### **define-success.md**
Guides developers in establishing clear, measurable success criteria for LLM applications. Emphasizes the importance of specific, measurable, achievable, and relevant criteria across multiple dimensions including task fidelity, consistency, relevance, tone, privacy preservation, context utilization, latency, and price. Provides detailed examples of good versus bad criteria definitions, with practical guidance on using both quantitative metrics (F1 scores, ROUGE-L, response times) and qualitative scales (Likert scales, expert rubrics) to create multidimensional evaluation frameworks.

### **develop-tests.md**
Comprehensive guide to designing and implementing evaluation test cases for LLM applications. Covers three core principles: task-specific design with edge cases, automation when possible, and prioritizing volume over perfection. Provides detailed code examples for six different evaluation methods including exact match (sentiment analysis), cosine similarity (FAQ consistency), ROUGE-L (summarization), LLM-based Likert scales (tone assessment), binary classification (privacy preservation), and ordinal scales (context utilization). Includes practical guidance on grading strategies (code-based, human, and LLM-based) with implementation tips for creating reliable, scalable evaluations.

### **eval-tool.md**
Documentation for Claude Console's built-in Evaluation tool, which provides a web-based interface for prompt testing and iteration. Covers:
- Accessing the Evaluate feature and prompt variable syntax requirements ({{variable}})
- Using the prompt generator powered by Claude Opus 4.1
- Creating test cases manually, via generation, or CSV import
- Customizing test case generation logic for precision
- Comparing prompt versions side-by-side with quality grading
- Prompt versioning and iterative refinement workflows
