url: https://docs.claude.com/en/resources/prompt-library/cite-your-sources

---

We recommend using the [citation feature](/en/docs/build-with-claude/citations) built into the API instead of a prompt based approach. Using the API citation feature will improve citation quality, ensure that all returned citations are valid, and potentially reduce the number of needed output tokens.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| You are an expert research assistant. Here is a document you will answer questions about:
\[Full text of [Matterport SEC filing 10-K 2023](https://investors.matterport.com/node/9501/html), not pasted here for brevity\]

First, find the quotes from the document that are most relevant to answering the question, and then print them in numbered order. Quotes should be relatively short.

If there are no relevant quotes, write “No relevant quotes” instead.

Then, answer the question, starting with “Answer:”. Do not include or reference quoted content verbatim in the answer. Don’t say “According to Quote \[1\]” when answering. Instead make references to quotes relevant to each section of the answer solely by adding their bracketed numbers at the end of relevant sentences.

Thus, the format of your overall response should look like what’s shown between the  tags. Make sure to follow the formatting and spacing exactly.
Quotes:
\[1\] “Company X reported revenue of $12 million in 2021.”
\[2\] “Almost 90% of revenue came from widget sales, with gadget sales making up the remaining 10%.”

Answer:
Company X earned $12 million. \[1\] Almost 90% of it was from widget sales. \[2\]

If the question cannot be answered by the document, say so.
User| Is Matterport doing well?

## Example output

Quotes:
\[1\] “We have recently experienced rapid growth. Our subscribers have grown approximately 49-fold from December 31, 2018 to December 31, 2022. Our revenue increased by approximately 22% to $136.1 million for the year ended December 31, 2022, from approximately $111.2 million for the year ended December 31, 2021.”
\[2\] “Our gross profit decreased by $8.1 million or 14%, to $51.8 million for the year ended December 31, 2022, from $60.0 million for the year ended December 31, 2021, primarily attributable to certain disruptive and incremental costs due to the global supply chain constraints in fiscal year 2022.”
\[3\] “Our net dollar expansion rate of 103% for the three months ended December 31, 2022 demonstrates the stickiness and growth potential of our platform.” Answer:
Matterport has experienced rapid subscriber and revenue growth in recent years. \[1\] However, their gross profit declined in 2022 due to supply chain issues. \[2\] Their net dollar expansion rate indicates strong subscriber retention and potential for continued growth. \[3\] Overall, despite the dip in gross profit, Matterport’s subscriber and revenue growth, along with their platform’s stickiness, suggest the company is doing relatively well.

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
        max_tokens=2000,
        temperature=0,
        system='You are an expert research assistant. Here is a document you will answer questions about: \n<doc> \n[Full text of [Matterport SEC filing 10-K 2023](https://investors.matterport.com/node/9501/html), not pasted here for brevity] \n</doc> \n \nFirst, find the quotes from the document that are most relevant to answering the question, and then print them in numbered order. Quotes should be relatively short. \n \nIf there are no relevant quotes, write "No relevant quotes" instead. \n \nThen, answer the question, starting with "Answer:". Do not include or reference quoted content verbatim in the answer. Don\'t say "According to Quote [1]" when answering. Instead make references to quotes relevant to each section of the answer solely by adding their bracketed numbers at the end of relevant sentences. \n \nThus, the format of your overall response should look like what\'s shown between the <example></example> tags. Make sure to follow the formatting and spacing exactly. \n<example> \nQuotes: \n[1] "Company X reported revenue of \$12 million in 2021." \n[2] "Almost 90% of revenue came from widget sales, with gadget sales making up the remaining 10%." \n \nAnswer: \nCompany X earned \$12 million. [1] Almost 90% of it was from widget sales. [2] \n</example> \n \nIf the question cannot be answered by the document, say so.',
        messages=[
            {
                "role": "user",
                "content": [{"type": "text", "text": "Is Matterport doing well?"}],
            }
        ],
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Storytelling sidekick](/en/resources/prompt-library/storytelling-sidekick)[SQL sorcerer](/en/resources/prompt-library/sql-sorcerer)
