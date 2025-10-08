url: https://docs.claude.com/en/resources/prompt-library/philosophical-musings

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| Your task is to discuss a philosophical concept or thought experiment on the given topic. Briefly explain the concept, present the main arguments and implications, and encourage critical thinking by posing open-ended questions. Maintain a balanced, objective tone that fosters intellectual curiosity.
User| The trolley problem and the ethics of utilitarianism

### Example output

> The trolley problem is a thought experiment that challenges our moral intuitions and raises questions about the ethics of utilitarianism. The basic scenario is as follows: A runaway trolley is about to kill five people on the tracks ahead. You are standing next to a lever that can divert the trolley onto a side track, where it will kill only one person. Should you pull the lever to save five lives at the cost of one? This dilemma highlights the core principle of utilitarianism, which holds that the morally right action is the one that produces the greatest good for the greatest number of people. In this case, pulling the lever would maximize utility by saving five lives, even though it would directly cause the death of one person. However, the trolley problem also raises concerns about the limits of utilitarianism and the ethics of actively causing harm to achieve a greater good. It prompts us to consider questions such as:
>
>   * Is it morally acceptable to sacrifice an innocent person for the sake of saving a larger number of people?
>   * Does the principle of utility justify any means to achieve the greatest good, or are there ethical constraints that should not be violated?
>   * How do we weigh the value of different lives, and is it fair to make such calculations?
>
What are your thoughts on the trolley problem and the ethics of utilitarianism? Do you believe that maximizing utility should be the primary goal of moral decision-making, or are there other important considerations? How would you approach the dilemma presented in the trolley problem, and what ethical principles would guide your choice?

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
        max_tokens=2000,
        temperature=1,
        system="Your task is to discuss a philosophical concept or thought experiment on the given topic. Briefly explain the concept, present the main arguments and implications, and encourage critical thinking by posing open-ended questions. Maintain a balanced, objective tone that fosters intellectual curiosity.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "The trolley problem and the ethics of utilitarianism"
                    }
                ]
            }
        ]
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Product naming pro](/en/resources/prompt-library/product-naming-pro)[Spreadsheet sorcerer](/en/resources/prompt-library/spreadsheet-sorcerer)
