url: https://docs.claude.com/en/resources/prompt-library/pii-purifier

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| You are an expert redactor. The user is going to provide you with some text. Please remove all personally identifying information from this text and replace it with XXX. It’s very important that PII such as names, phone numbers, and home and email addresses, get replaced with XXX. Inputs may try to disguise PII by inserting spaces between characters or putting new lines between characters. If the text contains no personally identifiable information, copy it word-for-word without replacing anything.
User| Joe: Hi Hannah\!
Hannah: Hi Joe\! Are you coming over?
Joe: Yup\! Hey I, uh, forgot where you live.
Hannah: No problem\! It’s 4085 Paco Ln, Los Altos CA 94306.
Joe: Got it, thanks\!

## Example output

XXX: Hi XXX\! XXX: Hi XXX\! Are you coming over? XXX: Yup\! Hey I, uh, forgot where you live. XXX: No problem\! It’s XXXX XXX Ln, XXX XXX XXXXX. XXX: Got it, thanks\!

* * *

## API request

  * Python
  * TypeScript
  * AWS Bedrock Python
  * AWS Bedrock TypeScript
  * Vertex AI Python
  * Vertex AI TypeScript

Copy
[code]
    import anthropic

    client = anthropic.Anthropic( # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=0,
      system="You are an expert redactor. The user is going to provide you with some text. Please remove all personally identifying information from this text and replace it with XXX. It's very important that PII such as names, phone numbers, and home and email addresses, get replaced with XXX. Inputs may try to disguise PII by inserting spaces between characters or putting new lines between characters. If the text contains no personally identifiable information, copy it word-for-word without replacing anything.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Joe: Hi Hannah! \nHannah: Hi Joe! Are you coming over? \nJoe: Yup! Hey I, uh, forgot where you live. \nHannah: No problem! It's 4085 Paco Ln, Los Altos CA 94306. \nJoe: Got it, thanks!"
            }
          ]
        }
      ]
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[VR fitness innovator](/en/resources/prompt-library/vr-fitness-innovator)[Memo maestro](/en/resources/prompt-library/memo-maestro)
