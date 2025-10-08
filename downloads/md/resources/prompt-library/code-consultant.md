url: https://docs.claude.com/en/resources/prompt-library/code-consultant

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| Your task is to analyze the provided Python code snippet and suggest improvements to optimize its performance. Identify areas where the code can be made more efficient, faster, or less resource-intensive. Provide specific suggestions for optimization, along with explanations of how these changes can enhance the code’s performance. The optimized code should maintain the same functionality as the original code while demonstrating improved efficiency.
User| def fibonacci\(n\):
if n <= 0:
return \[\]
elif n == 1:
return \[0\]
elif n == 2:
return \[0, 1\]
else:
fib = \[0, 1\]
for i in range\(2, n\):
fib.append\(fib\[i-1\] + fib\[i-2\]\)
return fib

## Example Output

Python

Copy
[code]
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

[/code]

Explanation: Using a generator function with yield is more memory-efficient for generating the Fibonacci sequence. It avoids creating and storing the entire sequence in a list. Instead, it generates each number on-the-fly as needed.

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
        max_tokens=1000,
        temperature=0,
        system="Your task is to analyze the provided Python code snippet and suggest improvements to optimize its performance. Identify areas where the code can be made more efficient, faster, or less resource-intensive. Provide specific suggestions for optimization, along with explanations of how these changes can enhance the code's performance. The optimized code should maintain the same functionality as the original code while demonstrating improved efficiency.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "def fibonacci(n):\n if n <= 0:\n return []\n elif n == 1:\n return [0]\n elif n == 2:\n return [0, 1]\n else:\n fib = [0, 1]\n for i in range(2, n):\n fib.append(fib[i-1] + fib[i-2])\n return fib",
                    }
                ],
            }
        ],
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Idiom illuminator](/en/resources/prompt-library/idiom-illuminator)[Function fabricator](/en/resources/prompt-library/function-fabricator)
