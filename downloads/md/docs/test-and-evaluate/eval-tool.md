url: https://docs.claude.com/en/docs/test-and-evaluate/eval-tool

---

## Accessing the Evaluate Feature

To get started with the Evaluation tool:

  1. Open the Claude Console and navigate to the prompt editor.
  2. After composing your prompt, look for the ‘Evaluate’ tab at the top of the screen.

![Accessing Evaluate Feature](https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/access_evaluate.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=663abe685548444261647cce0baefe9c)

Ensure your prompt includes at least 1-2 dynamic variables using the double brace syntax: \{\{variable\}\}. This is required for creating eval test sets.

## Generating Prompts

The Console offers a built-in [prompt generator](/en/docs/build-with-claude/prompt-engineering/prompt-generator) powered by Claude Opus 4.1:

1

Click 'Generate Prompt'

Clicking the ‘Generate Prompt’ helper tool will open a modal that allows you to enter your task information.

2

Describe your task

Describe your desired task \(e.g., “Triage inbound customer support requests”\) with as much or as little detail as you desire. The more context you include, the more Claude can tailor its generated prompt to your specific needs.

3

Generate your prompt

Clicking the orange ‘Generate Prompt’ button at the bottom will have Claude generate a high quality prompt for you. You can then further improve those prompts using the Evaluation screen in the Console.

This feature makes it easier to create prompts with the appropriate variable syntax for evaluation. ![Prompt Generator](https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/promptgenerator.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=65c7176d98dac6a07367adb03161b3ae)

## Creating Test Cases

When you access the Evaluation screen, you have several options to create test cases:

  1. Click the ’+ Add Row’ button at the bottom left to manually add a case.
  2. Use the ‘Generate Test Case’ feature to have Claude automatically generate test cases for you.
  3. Import test cases from a CSV file.

To use the ‘Generate Test Case’ feature:

1

Click on 'Generate Test Case'

Claude will generate test cases for you, one row at a time for each time you click the button.

2

Edit generation logic \(optional\)

You can also edit the test case generation logic by clicking on the arrow dropdown to the right of the ‘Generate Test Case’ button, then on ‘Show generation logic’ at the top of the Variables window that pops up. You may have to click \`Generate’ on the top right of this window to populate initial generation logic.Editing this allows you to customize and fine tune the test cases that Claude generates to greater precision and specificity.

Here’s an example of a populated Evaluation screen with several test cases: ![Populated Evaluation Screen](https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/eval_populated.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=aa5f378cd1fd8bee94acbb557476f690)

If you update your original prompt text, you can re-run the entire eval suite against the new prompt to see how changes affect performance across all test cases.

## Tips for Effective Evaluation

Prompt Structure for Evaluation

To make the most of the Evaluation tool, structure your prompts with clear input and output formats. For example:

Copy
[code]
    In this task, you will generate a cute one sentence story that incorporates two elements: a color and a sound.
    The color to include in the story is:
    <color>
    {{COLOR}}
    </color>
    The sound to include in the story is:
    <sound>
    {{SOUND}}
    </sound>
    Here are the steps to generate the story:
    1. Think of an object, animal, or scene that is commonly associated with the color provided. For example, if the color is "blue", you might think of the sky, the ocean, or a bluebird.
    2. Imagine a simple action, event or scene involving the colored object/animal/scene you identified and the sound provided. For instance, if the color is "blue" and the sound is "whistle", you might imagine a bluebird whistling a tune.
    3. Describe the action, event or scene you imagined in a single, concise sentence. Focus on making the sentence cute, evocative and imaginative. For example: "A cheerful bluebird whistled a merry melody as it soared through the azure sky."
    Please keep your story to one sentence only. Aim to make that sentence as charming and engaging as possible while naturally incorporating the given color and sound.
    Write your completed one sentence story inside <story> tags.

[/code]

This structure makes it easy to vary inputs \(\{\{COLOR\}\} and \{\{SOUND\}\}\) and evaluate outputs consistently.

Use the ‘Generate a prompt’ helper tool in the Console to quickly create prompts with the appropriate variable syntax for evaluation.

## Understanding and comparing results

The Evaluation tool offers several features to help you refine your prompts:

  1. **Side-by-side comparison** : Compare the outputs of two or more prompts to quickly see the impact of your changes.
  2. **Quality grading** : Grade response quality on a 5-point scale to track improvements in response quality per prompt.
  3. **Prompt versioning** : Create new versions of your prompt and re-run the test suite to quickly iterate and improve results.

By reviewing results across test cases and comparing different prompt versions, you can spot patterns and make informed adjustments to your prompt more efficiently. Start evaluating your prompts today to build more robust AI applications with Claude\!

Was this page helpful?

YesNo

[Develop test cases](/en/docs/test-and-evaluate/develop-tests)[Reducing latency](/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency)
