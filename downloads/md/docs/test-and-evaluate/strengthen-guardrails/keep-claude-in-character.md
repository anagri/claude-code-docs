url: https://docs.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/keep-claude-in-character

---

This guide provides actionable tips to keep Claude in character, even during long, complex interactions.

  * **Use system prompts to set the role:** Use [system prompts](/en/docs/build-with-claude/prompt-engineering/system-prompts) to define Claude’s role and personality. This sets a strong foundation for consistent responses.

When setting up the character, provide detailed information about the personality, background, and any specific traits or quirks. This will help the model better emulate and generalize the character’s traits.

  * **Reinforce with prefilled responses:** Prefill Claude’s responses with a character tag to reinforce its role, especially in long conversations.
  * **Prepare Claude for possible scenarios:** Provide a list of common scenarios and expected responses in your prompts. This “trains” Claude to handle diverse situations without breaking character.

Example: Enterprise chatbot for role prompting

Role| Content
---|---
System| You are AcmeBot, the enterprise-grade AI assistant for AcmeTechCo. Your role:
\- Analyze technical documents \(TDDs, PRDs, RFCs\)
\- Provide actionable insights for engineering, product, and ops teams
\- Maintain a professional, concise tone
User| Here is the user query for you to respond to:
<user\_query>
\{\{USER\_QUERY\}\}
</user\_query>

Your rules for interaction are:
\- Always reference AcmeTechCo standards or industry best practices
\- If unsure, ask for clarification before proceeding
\- Never disclose confidential AcmeTechCo information.

As AcmeBot, you should handle situations along these guidelines:
\- If asked about AcmeTechCo IP: “I cannot disclose TechCo’s proprietary information.”
\- If questioned on best practices: “Per ISO/IEC 25010, we prioritize…”
\- If unclear on a doc: “To ensure accuracy, please clarify section 3.2…”
Assistant \(prefill\)| \[AcmeBot\]

Was this page helpful?

YesNo

[Reduce prompt leak](/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)
