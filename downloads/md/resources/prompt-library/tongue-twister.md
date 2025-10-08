url: https://docs.claude.com/en/resources/prompt-library/tongue-twister

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

Role| Content
---|---
User| Generate complex and creative tongue twisters. Aim to create tongue twisters that are not only challenging to say but also engaging, entertaining, and potentially humorous. Consider incorporating wordplay, rhyme, and alliteration to enhance the difficulty and enjoyment of the tongue twisters.

## Example Output

Tongue Twister 1:
The shrewd shrew chewed through the shiny, shimmering shoe. Tongue Twister 2:
Brisk breezes blew by the blue-blooded, blabbering, babbling baboon. Tongue Twister 3:
The perplexed piper picked a peck of pickled peppers while practicing his piping. Tongue Twister 4:
Six sleek, slick, slender sleds slid swiftly down the steep, snowy slope.

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
      temperature=1,
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate complex and creative tongue twisters. Aim to create tongue twisters that are not only challenging to say but also engaging, entertaining, and potentially humorous. Consider incorporating wordplay, rhyme, and alliteration to enhance the difficulty and enjoyment of the tongue twisters."
            }
          ]
        }
      ]
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Grading guru](/en/resources/prompt-library/grading-guru)[Interview question crafter](/en/resources/prompt-library/interview-question-crafter)
