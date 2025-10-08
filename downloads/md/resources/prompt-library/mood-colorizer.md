url: https://docs.claude.com/en/resources/prompt-library/mood-colorizer

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| Your task is to take the provided text description of a mood or emotion and generate a HEX color code that visually represents that mood. Use color psychology principles and common associations to determine the most appropriate color for the given mood. If the text description is unclear, ambiguous, or does not provide enough information to determine a suitable color, respond with “Unable to determine a HEX color code for the given mood.”
User| A passionate, intense, and fiery emotion, full of love and desire.

## Example Output

`# FF1744` This HEX color code represents a vivid, bold shade of red. Red is commonly associated with passion, intensity, love, and desire. The specific shade chosen here is a fiery, energetic red that captures the heat and fervor of the described emotion. Red is known to stimulate feelings of excitement and passion, making it an appropriate choice for representing this mood.

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
      max_tokens=500,
      temperature=0.5,
      system="Your task is to take the provided text description of a mood or emotion and generate a HEX color code that visually represents that mood. Use color psychology principles and common associations to determine the most appropriate color for the given mood. If the text description is unclear, ambiguous, or does not provide enough information to determine a suitable color, respond with \"Unable to determine a HEX color code for the given mood.\"",
      messages=[
        {
        "role": "user",
        "content": [
            {
              "type": "text",
              "text": "A passionate, intense, and fiery emotion, full of love and desire."
            }
          ]
        }
      ]
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[LaTeX legend](/en/resources/prompt-library/latex-legend)[Git gud](/en/resources/prompt-library/git-gud)
