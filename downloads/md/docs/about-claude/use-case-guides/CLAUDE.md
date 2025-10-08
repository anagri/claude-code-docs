# Directory: use-case-guides

## Overview
This directory contains production-ready implementation guides for common Claude use cases, providing best practices, code examples, and deployment strategies for building intelligent automation systems in customer support, content moderation, and legal workflows.

## Files in This Directory

### **overview.md**
An index page that introduces the use case guides collection. It highlights four main implementation guides: Ticket Routing (customer support ticket classification), Customer Support Agent (building conversational chatbots), Content Moderation (filtering and moderating user-generated content), and Legal Summarization (extracting key information from legal documents). Each guide provides in-depth production guidance for building these use cases with Claude.

### **ticket-routing.md**
A comprehensive guide for implementing automated support ticket classification and routing using Claude. The guide covers:

- **When to use Claude**: Key indicators include limited labeled training data, evolving classification categories, complex unstructured text, semantic understanding requirements, interpretable reasoning needs, multilingual support, and effective edge case handling.

- **Implementation process**: Understanding current support workflows, defining user intent categories (Technical Issues, Account Management, Product Information, User Guidance, Feedback, Order-Related, Service Requests, Security Concerns, Compliance/Legal, Emergency Support, Training/Education, Integration/API), establishing success criteria, selecting the right model (Claude 3.5 Haiku recommended), and building classification prompts.

- **Evaluation metrics**: Classification consistency (95%+ target), adaptation speed (50-100 samples), multilingual handling (5-10% accuracy drop max), edge case handling (80%+ accuracy), bias mitigation (2-3% variance max), routing accuracy (90-95%), time-to-assignment (under 5 minutes), rerouting rate (below 10%), and customer satisfaction (90%+).

- **Advanced strategies**: Hierarchical classification for 20+ intent categories, vector database similarity search for highly variable tickets, and explicit edge case handling for implicit requests, emotion vs. intent prioritization, and multiple issue scenarios.

- **Integration approaches**: Push-based (webhook-triggered) or pull-based (scheduled polling) integration patterns with existing support ticketing systems.

### **customer-support-chat.md**
A detailed guide for building intelligent customer support chatbots with Claude. Key components include:

- **Use case justification**: High volume of repetitive queries, need for quick information synthesis, 24/7 availability requirement, rapid scaling during peak periods, and consistent brand voice maintenance. Claude offers natural conversation, complex query handling, and scalable multilingual support.

- **Implementation workflow**: Defining ideal chat interactions, breaking interactions into unique tasks (greeting/guidance, product information, conversation management, quote generation), establishing success criteria (query comprehension 95%+, response relevance 90%+, response accuracy 100%, topic adherence 95%+, content generation effectiveness 100%, escalation efficiency 95%+).

- **Technical implementation**: Building prompts with identity, static context, examples, and guardrails; implementing tool use for dynamic capabilities (quote generation APIs); deploying with Streamlit UI; evaluating with systematic quantitative and qualitative methods.

- **Performance optimization**: RAG integration to reduce long context latency, real-time data integration with tool use, strengthened input/output guardrails (hallucination reduction, cross-checking, contractual commitment avoidance, jailbreak mitigation, competitor filtering, character consistency, PII removal), streaming for reduced perceived response time, and scaling with intent classifiers for complex routing.

- **Production deployment**: API wrapper creation with Server-Sent Events (SSE) for streaming, caching for improved response times, context retention for conversation continuity, and web interface implementation.

### **content-moderation.md**
A comprehensive guide for implementing content moderation systems using Claude to filter and moderate user-generated content. The guide includes:

- **Decision criteria**: Cost-effective rapid implementation, semantic understanding with quick decisions, consistent policy decisions, adaptable evolving policies, interpretable reasoning for moderation decisions, multilingual support without separate models, and multimodal support for text and images. Note: Claude models are trained to be honest, helpful, and harmless, which may result in moderation aligned with Anthropic's Acceptable Use Policy regardless of custom prompts.

- **Preparation**: Generating examples of content to moderate (both allowed and disallowed), creating well-defined moderation categories (Child Exploitation, Conspiracy Theories, Hate, Indiscriminate Weapons, Intellectual Property, Non-Violent Crimes, Privacy, Self-Harm, Sex Crimes, Sexual Content, Specialized Advice, Violent Crimes), understanding edge cases requiring nuanced language interpretation.

- **Implementation approach**: Selecting the right model (Claude Haiku 3 for cost-effectiveness - estimated $2,590/month for 1 billion posts vs. $31,080/month for Sonnet 4.5), building strong prompts with unsafe categories and JSON response format, evaluating using classification techniques with multiple risk levels (0-3 scale: no risk, low risk, medium risk, high risk).

- **Deployment best practices**: Providing clear feedback to users when content is flagged, analyzing moderated content to identify trends, continuously evaluating and improving with precision/recall tracking.

- **Performance improvements**: Defining topics with detailed definitions and examples for each unsafe category, implementing batch processing to reduce costs in non-real-time scenarios (processing multiple messages in a single API call with XML-tagged message IDs), optimizing batch size through experimentation.

### **legal-summarization.md**
An in-depth guide for implementing legal document summarization using Claude to extract key information and expedite research. The guide covers:

- **Use case indicators**: High volume of documents requiring efficient review, automated metadata extraction needs (parties, dates, terms, clauses), clear concise standardized summary generation, precise citation requirements, and streamlined legal research processes.

- **Preparation**: Determining specific details to extract (e.g., for sublease agreements: parties involved, property details, term and rent, responsibilities, consent and notices, special provisions), establishing success criteria (factual correctness, legal precision, conciseness, consistency across documents, readability, bias and fairness).

- **Model selection and costs**: Claude Sonnet 3.5 recommended for high accuracy; Claude Haiku 3 for cost optimization. Cost comparison for 1,000 sublease agreements (300K characters each): Sonnet 4.5 = $263.25, Haiku 3 = $21.96.

- **Implementation process**: Transforming PDFs to processable text using pypdf (extracting text, removing whitespace, removing page numbers), building structured prompts with details to extract, XML-tagged output format, system prompts for role definition, and assistant prefilling with stop sequences for structured output.

- **Evaluation metrics**: ROUGE scores (overlap with reference summaries, focuses on recall), BLEU scores (n-gram match precision), contextual embedding similarity (semantic meaning capture via cosine similarity), LLM-based grading (evaluation against custom rubrics), and human evaluation (expert review as sanity check).

- **Deployment considerations**: Legal liability disclaimers (AI-generated summaries should be reviewed by professionals), handling diverse document formats (PDFs, Word, text files), parallelizing API calls for large document collections (respecting rate limits).

- **Advanced techniques**: Meta-summarization for long documents (chunking text into 20K character segments, summarizing each chunk, then combining chunk summaries into final meta-summary), summary indexed documents for RAG (generating concise summaries for each document, ranking summary relevance for retrieval), and fine-tuning Claude on custom datasets via Amazon Bedrock (identifying errors, curating corrected examples, iterative improvement).
