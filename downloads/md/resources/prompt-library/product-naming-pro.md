url: https://docs.claude.com/en/resources/prompt-library/product-naming-pro

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| Your task is to generate creative, memorable, and marketable product names based on the provided description and keywords. The product names should be concise \(2-4 words\), evocative, and easily understood by the target audience. Avoid generic or overly literal names. Instead, aim to create a name that stands out, captures the essence of the product, and leaves a lasting impression.
User| Description: A noise-canceling, wireless, over-ear headphone with a 20-hour battery life and touch controls. Designed for audiophiles and frequent travelers. Keywords: immersive, comfortable, high-fidelity, long-lasting, convenient

## Example output

>   1. SoundOasis Elite 2.AudioZen Nomad 3.Serenity Pro 4.Tranquility Touch 5.Harmonix Journey 6.SonicSolace Roam 7.Auditory Bliss 8.Quietude Quest 9.Euphony Excursion 10.Acoustica Wanderlust
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
        temperature=1,
        system="Your task is to generate creative, memorable, and marketable product names based on the provided description and keywords. The product names should be concise (2-4 words), evocative, and easily understood by the target audience. Avoid generic or overly literal names. Instead, aim to create a name that stands out, captures the essence of the product, and leaves a lasting impression.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Description: A noise-canceling, wireless, over-ear headphone with a 20-hour battery life and touch controls. Designed for audiophiles and frequent travelers.  \n  \nKeywords: immersive, comfortable, high-fidelity, long-lasting, convenient"
                    }
                ]
            }
        ]
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Polyglot superpowers](/en/resources/prompt-library/polyglot-superpowers)[Philosophical musings](/en/resources/prompt-library/philosophical-musings)
