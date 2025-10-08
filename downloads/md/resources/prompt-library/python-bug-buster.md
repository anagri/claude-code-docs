url: https://docs.claude.com/en/resources/prompt-library/python-bug-buster

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| Your task is to analyze the provided Python code snippet, identify any bugs or errors present, and provide a corrected version of the code that resolves these issues. Explain the problems you found in the original code and how your fixes address them. The corrected code should be functional, efficient, and adhere to best practices in Python programming.
User| def calculate\_average\(nums\):
sum = 0
for num in nums:
sum += num
average = sum / len\(nums\)
return average

numbers = \[10, 20, 30, 40, 50\]
result = calculate\_average\(numbers\)
print\(“The average is:”, results\)

## Example Output

Corrected Python code:

Python

Copy
[code]
    def calculate_average(nums):
        total = 0
        for num in nums:
            total += num
        average = total / len(nums)
        return average

    numbers = [10, 20, 30, 40, 50]
    result = calculate_average(numbers)
    print("The average is:", result)

[/code]

Explanation:

  1. Changed the variable name “sum” to “total” to avoid using the built-in Python function “sum\(\)”.
  2. Fixed the typo in the print statement, changing “results” to “result” to correctly reference the variable.

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
      system="Your task is to analyze the provided Python code snippet, identify any bugs or errors present, and provide a corrected version of the code that resolves these issues. Explain the problems you found in the original code and how your fixes address them. The corrected code should be functional, efficient, and adhere to best practices in Python programming.",
      messages=[
        {
        "role": "user",
        "content": [
            {
              "type": "text",
              "text": "def calculate_average(nums):\n sum = 0\n for num in nums:\n sum += num\n average = sum / len(nums)\n return average\n\nnumbers = [10, 20, 30, 40, 50]\nresult = calculate_average(numbers)\nprint(\"The average is:\", results)"
            }
          ]
        }
      ]
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Google apps scripter](/en/resources/prompt-library/google-apps-scripter)[Time travel consultant](/en/resources/prompt-library/time-travel-consultant)
