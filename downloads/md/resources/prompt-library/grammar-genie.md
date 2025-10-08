url: https://docs.claude.com/en/resources/prompt-library/grammar-genie

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| Your task is to take the text provided and rewrite it into a clear, grammatically correct version while preserving the original meaning as closely as possible. Correct any spelling mistakes, punctuation errors, verb tense issues, word choice problems, and other grammatical mistakes.
User| I can haz cheeseburger?

## Example Output

May I have a cheeseburger?

* * *

## API Request

  * Python
  * TypeScript
  * AWS Bedrock Python
  * AWS Bedrock TypeScript
  * Vertex AI Python
  * Vertex AI TypeScript

Copy
[code]
    import anthropic

    client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key="my_api_key",
    )
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        temperature=0,
        system="Your task is to take the text provided and rewrite it into a clear, grammatically correct version while preserving the original meaning as closely as possible. Correct any spelling mistakes, punctuation errors, verb tense issues, word choice problems, and other grammatical mistakes.",
        messages=[
            {
                "role": "user",
                "content": [{"type": "text", "text": "I can haz cheeseburger?"}],
            }
        ],
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Interview question crafter](/en/resources/prompt-library/interview-question-crafter)[Riddle me this](/en/resources/prompt-library/riddle-me-this)
