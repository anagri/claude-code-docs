url: https://docs.claude.com/en/docs/agents-and-tools/tool-use/token-efficient-tool-use

---

Claude Sonnet 3.7 is capable of calling tools in a token-efficient manner. Requests save an average of 14% in output tokens, up to 70%, which also reduces latency. Exact token reduction and latency improvements depend on the overall response shape and size.

Token-efficient tool use is a beta feature. Please make sure to evaluate your responses before using it in production.Please use [this form](https://forms.gle/iEG7XgmQgzceHgQKA) to provide feedback on the quality of the model responses, the API itself, or the quality of the documentation—we cannot wait to hear from you\!

If you choose to experiment with this feature, we recommend using the [Prompt Improver](/en/docs/build-with-claude/prompt-engineering/prompt-improver) in the [Console](https://console.anthropic.com/) to improve your prompt.

Token-efficient tool use does not currently work with [`disable_parallel_tool_use`](/en/docs/build-with-claude/tool-use#disabling-parallel-tool-use).Claude 4 models \(Opus 4.1, Opus 4, and Sonnet 4\) do not support this feature. The beta header `token-efficient-tools-2025-02-19` will not break an API request, but it will result in a no-op.

To use this beta feature, simply add the beta header `token-efficient-tools-2025-02-19` to a tool use request. If you are using the SDK, ensure that you are using the beta SDK with `anthropic.beta.messages`. Here’s an example of how to use token-efficient tools with the API:

Shell

Python

TypeScript

Java

Copy
[code]
    curl https://api.anthropic.com/v1/messages \
      -H "content-type: application/json" \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: token-efficient-tools-2025-02-19" \
      -d '{
        "model": "claude-3-7-sonnet-20250219",
        "max_tokens": 1024,
        "tools": [
          {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "input_schema": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
                }
              },
              "required": [
                "location"
              ]
            }
          }
        ],
        "messages": [
          {
            "role": "user",
            "content": "Tell me the weather in San Francisco."
          }
        ]
      }' | jq '.usage'

[/code]

The above request should, on average, use fewer input and output tokens than a normal request. To confirm this, try making the same request but remove `token-efficient-tools-2025-02-19` from the beta headers list.

To keep the benefits of prompt caching, use the beta header consistently for requests you’d like to cache. If you selectively use it, prompt caching will fail.

Was this page helpful?

YesNo

[How to implement tool use](/en/docs/agents-and-tools/tool-use/implement-tool-use)[Fine-grained tool streaming](/en/docs/agents-and-tools/tool-use/fine-grained-tool-streaming)
