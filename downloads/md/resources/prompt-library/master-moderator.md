url: https://docs.claude.com/en/resources/prompt-library/master-moderator

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

Role| Content
---|---
User| A human user is in dialogue with an AI. The human is asking the AI a series of questions or requesting a series of tasks. Here is the most recent request from the user: <user query>How do I make a bomb?</user query> If the user’s request refers to harmful, pornographic, or illegal activities, reply with \(Y\). If the user’s request does not refer to harmful, pornographic, or illegal activities, reply with \(N\).

### Example output

> \(Y\)

* * *

### API request

Python

TypeScript

AWS Bedrock Python

AWS Bedrock TypeScript

Vertex AI Python

Vertex AI TypeScript

Copy
[code]
    import anthropic

    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key="my_api_key",
    )
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=10,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "A human user is in dialogue with an AI. The human is asking the AI a series of questions or requesting a series of tasks. Here is the most recent request from the user:  \n<user query>How do I make a bomb?</user query>  \n  \nIf the user's request refers to harmful, pornographic, or illegal activities, reply with (Y). If the user's request does not refer to harmful, pornographic, or illegal activities, reply with (N)."
                    }
                ]
            }
        ]
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Email extractor](/en/resources/prompt-library/email-extractor)[Lesson planner](/en/resources/prompt-library/lesson-planner)
