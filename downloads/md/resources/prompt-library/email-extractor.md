url: https://docs.claude.com/en/resources/prompt-library/email-extractor

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| Precisely copy any email addresses from the following text and then write them, one per line. Only write an email address if it’s precisely spelled out in the input text. If there are no email addresses in the text, write “N/A”. Do not say anything else.
User| Phone Directory: John Latrabe, 555-232-1995, \[[\[email protected\]](/cdn-cgi/l/email-protection#93f9fcfbfdaaa3aaa4a3aad3f4f6f6fef2faffbdf0fcfe)\] Josie Lana, 555-759-2905, \[[\[email protected\]](/cdn-cgi/l/email-protection#1b717468727e5b717468727e777a757a75727e6935787476)\] Keven Stevens, 555-980-7000, \[[\[email protected\]](/cdn-cgi/l/email-protection#6b0f19000e1d020559592b0c0e0e060a020745080406)\] Phone directory will be kept up to date by the HR manager.

### Example output

> [\[email protected\]](/cdn-cgi/l/email-protection#90fafff8fea9a0a9a7a0a9d0f7f5f5fdf1f9fcbef3fffd) > [\[email protected\]](/cdn-cgi/l/email-protection#ec86839f8589ac86839f8589808d828d8285899ec28f8381) > [\[email protected\]](/cdn-cgi/l/email-protection#0367716866756a6d3131436466666e626a6f2d606c6e)

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
        max_tokens=1000,
        temperature=0,
        system="Precisely copy any email addresses from the following text and then write them, one per line. Only write an email address if it's precisely spelled out in the input text. If there are no email addresses in the text, write \"N/A\".  Do not say anything else.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Phone Directory:  \nJohn Latrabe, 555-232-1995, [[email protected]]  \nJosie Lana, 555-759-2905, [[email protected]]  \nKeven Stevens, 555-980-7000, [[email protected]]  \n  \nPhone directory will be kept up to date by the HR manager."
                    }
                ]
            }
        ]
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Motivational muse](/en/resources/prompt-library/motivational-muse)[Master moderator](/en/resources/prompt-library/master-moderator)
