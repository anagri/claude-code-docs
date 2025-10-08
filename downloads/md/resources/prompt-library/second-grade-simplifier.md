url: https://docs.claude.com/en/resources/prompt-library/second-grade-simplifier

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.
User| The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate \(ATP\) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur.

## Example Output

Mitochondria are tiny parts inside cells that work like little power stations. They make a special molecule called ATP, which is like the cell’s energy money. ATP helps the cell do important jobs and keeps it running smoothly, just like how money helps people buy things they need. Mitochondria are very important because without them, cells wouldn’t have the energy to function properly.

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

    client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=0,
      system="Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
            }
          ]
        }
      ]
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Mindfulness mentor](/en/resources/prompt-library/mindfulness-mentor)[VR fitness innovator](/en/resources/prompt-library/vr-fitness-innovator)
