url: https://docs.claude.com/en/resources/prompt-library/airport-code-analyst

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| Your task is to analyze the provided text and identify any airport codes mentioned within it. Present these airport codes as a list in the order they appear in the text. If no airport codes are found, return an empty list.
User| My next trip involves flying from Seattle to Amsterdam. I’ll be spending a few days in Amsterdam before heading to Paris for a connecting flight to Rome.

### Example Output

> Here is the list of airport codes mentioned in the text, in the order they appear:
>
>   1. SEA \(Seattle\)
>   2. AMS \(Amsterdam\)
>   3. CDG \(Paris\)
>   4. FCO \(Rome\)
>

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
        max_tokens=1000,
        temperature=0,
        system="Your task is to analyze the provided text and identify any airport codes mentioned within it. Present these airport codes as a list in the order they appear in the text. If no airport codes are found, return an empty list.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "My next trip involves flying from Seattle to Amsterdam. I'll be spending a few days in Amsterdam before heading to Paris for a connecting flight to Rome."
                    }
                ]
            }
        ]
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Tweet tone detector](/en/resources/prompt-library/tweet-tone-detector)
