url: https://docs.claude.com/en/resources/prompt-library/data-organizer

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| Your task is to take the unstructured text provided and convert it into a well-organized table format using JSON. Identify the main entities, attributes, or categories mentioned in the text and use them as keys in the JSON object. Then, extract the relevant information from the text and populate the corresponding values in the JSON object. Ensure that the data is accurately represented and properly formatted within the JSON structure. The resulting JSON table should provide a clear, structured overview of the information presented in the original text.
User| Silvermist Hollow, a charming village, was home to an extraordinary group of individuals. Among them was Dr. Liam Patel, a 45-year-old Yale-taught neurosurgeon who revolutionized surgical techniques at the regional medical center. Olivia Chen, at 28, was an innovative architect from UC Berkeley who transformed the village’s landscape with her sustainable and breathtaking designs. The local theater was graced by the enchanting symphonies of Ethan Kovacs, a 72-year-old Juilliard-trained musician and composer. Isabella Torres, a self-taught chef with a passion for locally sourced ingredients, created a culinary sensation with her farm-to-table restaurant, which became a must-visit destination for food lovers. These remarkable individuals, each with their distinct talents, contributed to the vibrant tapestry of life in Silvermist Hollow.

### Example output

Copy
[code]
    [
      {
        "name": "Dr. Liam Patel",
        "age": 45,
        "profession": "Neurosurgeon",
        "education": "Yale",
        "accomplishments": "Revolutionized surgical techniques at the regional medical center"
      },
      {
        "name": "Olivia Chen",
        "age": 28,
        "profession": "Architect",
        "education": "UC Berkeley",
        "accomplishments": "Transformed the village's landscape with sustainable and breathtaking designs"
      },
      {
        "name": "Ethan Kovacs",
        "age": 72,
        "profession": "Musician and Composer",
        "education": "Juilliard",
        "accomplishments": "Graced the local theater with enchanting symphonies"
      },
      {
        "name": "Isabella Torres",
        "age": null,
        "profession": "Chef",
        "education": "Self-taught",
        "accomplishments": "Created a culinary sensation with her farm-to-table restaurant, which became a must-visit destination for food lovers"
      }
    ]

[/code]

* * *

Python

TypeScript

AWS Bedrock Python

AWS Bedrock TypeScript

Vertex AI Python

Vertex AI Type

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
        system="Your task is to take the unstructured text provided and convert it into a well-organized table format using JSON. Identify the main entities, attributes, or categories mentioned in the text and use them as keys in the JSON object. Then, extract the relevant information from the text and populate the corresponding values in the JSON object. Ensure that the data is accurately represented and properly formatted within the JSON structure. The resulting JSON table should provide a clear, structured overview of the information presented in the original text.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Silvermist Hollow, a charming village, was home to an extraordinary group of individuals. Among them was Dr. Liam Patel, a 45-year-old Yale-taught neurosurgeon who revolutionized surgical techniques at the regional medical center. Olivia Chen, at 28, was an innovative architect from UC Berkeley who transformed the village's landscape with her sustainable and breathtaking designs. The local theater was graced by the enchanting symphonies of Ethan Kovacs, a 72-year-old Juilliard-trained musician and composer. Isabella Torres, a self-taught chef with a passion for locally sourced ingredients, created a culinary sensation with her farm-to-table restaurant, which became a must-visit destination for food lovers. These remarkable individuals, each with their distinct talents, contributed to the vibrant tapestry of life in Silvermist Hollow."
                    }
                ]
            }
        ]
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Alien anthropologist](/en/resources/prompt-library/alien-anthropologist)[Brand builder](/en/resources/prompt-library/brand-builder)
