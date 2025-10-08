url: https://docs.claude.com/en/api/prompt-tools-templatize

---

POST

/

v1

/

experimental

/

templatize\_prompt

cURL

cURL

Copy
[code]
    curl -X POST https://api.anthropic.com/v1/experimental/templatize_prompt \
         --header "x-api-key: $ANTHROPIC_API_KEY" \
         --header "anthropic-version: 2023-06-01" \
         --header "anthropic-beta: prompt-tools-2025-04-02" \
         --header "content-type: application/json" \
         --data \
    '{
        "messages": [{"role": "user", "content": "Translate hello to German"}],
        "system": "You are an English to German translator"
    }'
[/code]

200

4XX

Copy
[code]
    {
      "messages": [
        {
          "content": [
            {
              "text": "Translate {{WORD_TO_TRANSLATE}} to {{TARGET_LANGUAGE}}",
              "type": "text"
            }
          ],
          "role": "user"
        }
      ],
      "system": "You are a professional English to {{TARGET_LANGUAGE}} translator",
      "usage": [
        {
          "input_tokens": 490,
          "output_tokens": 661
        }
      ],
      "variable_values": {
        "TARGET_LANGUAGE": "German",
        "WORD_TO_TRANSLATE": "hello"
      }
    }
[/code]

The prompt tools APIs are in a closed research preview. [Request to join the closed research preview](https://forms.gle/LajXBafpsf1SuJHp7).

## Before you begin

The prompt tools are a set of APIs to generate and improve prompts. Unlike our other APIs, this is an experimental API: you’ll need to request access, and it doesn’t have the same level of commitment to long-term support as other APIs. These APIs are similar to what’s available in the [Anthropic Workbench](https://console.anthropic.com/workbench), and are intented for use by other prompt engineering platforms and playgrounds.

## Getting started with the prompt improver

To use the prompt generation API, you’ll need to:

  1. Have joined the closed research preview for the prompt tools APIs
  2. Use the API directly, rather than the SDK
  3. Add the beta header `prompt-tools-2025-04-02`

This API is not available in the SDK

## Templatize a prompt

#### Headers

anthropic-beta

string\[\]

Optional header to specify the beta version\(s\) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

x-api-key

string

required

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a Workspace.

#### Body

application/json

messages

InputMessage · object\[\]

required

The prompt to templatize, structured as a list of `message` objects.

Each message in the `messages` array must:

  * Contain only text-only content blocks
  * Not include tool calls, images, or prompt caching blocks

Example of a simple text prompt:
[code]
    [  {    "role": "user",     "content": [      {        "type": "text",        "text": "Translate hello to German"      }    ]  }]
[/code]

Note that only contiguous user messages with text content are allowed. Assistant prefill is permitted, but other content types will cause validation errors.

Show child attributes

Examples:
[code]
    [  {    "content": [      {        "text": "Translate hello to German",        "type": "text"      }    ],    "role": "user"  }]
[/code]

system

string | null

The existing system prompt to templatize.
[code]
    {  "system": "You are a professional English to German translator",  [...]}
[/code]

Note that this differs from the Messages API; it is strictly a string.

Examples:

`"You are a professional English to German translator"`

#### Response

200

application/json

Successful Response

messages

InputMessage · object\[\]

required

The templatized prompt with variable placeholders.

The response includes the input messages with specific values replaced by variable placeholders. These messages maintain the original message structure but contain uppercase variable names in place of concrete values.

For example, an input message content like `"Translate hello to German"` would be transformed to `"Translate {{WORD_TO_TRANSLATE}} to {{TARGET_LANGUAGE}}"`.
[code]
    {  "messages": [    {      "role": "user",      "content": [        {          "type": "text",          "text": "Translate {{WORD_TO_TRANSLATE}} to {{TARGET_LANGUAGE}}"        }      ]    }  ]}
[/code]

Show child attributes

Examples:
[code]
    [  {    "content": [      {        "text": "Translate {{WORD_TO_TRANSLATE}} to {{TARGET_LANGUAGE}}",        "type": "text"      }    ],    "role": "user"  }]
[/code]

system

string

required

The input system prompt with variables identified and replaced.

If no system prompt was provided in the original request, this field will be an empty string.

Examples:

`"You are a professional English to {{TARGET_LANGUAGE}} translator"`

usage

object

required

Usage information

Show child attributes

variable\_values

object

required

A mapping of template variable names to their original values, as extracted from the input prompt during templatization. Each key represents a variable name identified in the templatized prompt, and each value contains the corresponding content from the original prompt that was replaced by that variable.

Example:
[code]
    "variable_values": {  "WORD_TO_TRANSLATE": "hello",  "TARGET_LANGUAGE": "German"}
[/code]

In this example response, the original prompt – `Translate hello to German` – was templatized to `Translate WORD_TO_TRANSLATE to TARGET_LANGUAGE`, with the variable values extracted as shown.

Show child attributes

Examples:
[code]
    {  "TARGET_LANGUAGE": "German",  "WORD_TO_TRANSLATE": "hello"}
[/code]

Was this page helpful?

YesNo

[Improve a prompt](/en/api/prompt-tools-improve)[Migrating from Text Completions](/en/api/migrating-from-text-completions-to-messages)
