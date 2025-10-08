url: https://docs.claude.com/en/api/prompt-tools-generate

---

POST

/

v1

/

experimental

/

generate\_prompt

cURL

cURL

Copy
[code]
    curl -X POST https://api.anthropic.com/v1/experimental/generate_prompt \
         --header "x-api-key: $ANTHROPIC_API_KEY" \
         --header "anthropic-version: 2023-06-01" \
         --header "anthropic-beta: prompt-tools-2025-04-02" \
         --header "content-type: application/json" \
         --data \
    '{
        "task": "a chef for a meal prep planning service",
        "target_model": "claude-3-7-sonnet-20250219"
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
              "text": "<generated prompt>",
              "type": "text"
            }
          ],
          "role": "user"
        }
      ],
      "system": "",
      "usage": [
        {
          "input_tokens": 490,
          "output_tokens": 661
        }
      ]
    }
[/code]

The prompt tools APIs are in a closed research preview. [Request to join the closed research preview](https://forms.gle/LajXBafpsf1SuJHp7).

## Before you begin

The prompt tools are a set of APIs to generate and improve prompts. Unlike our other APIs, this is an experimental API: you’ll need to request access, and it doesn’t have the same level of commitment to long-term support as other APIs. These APIs are similar to what’s available in the [Anthropic Workbench](https://console.anthropic.com/workbench), and are intended for use by other prompt engineering platforms and playgrounds.

## Getting started with the prompt generator

To use the prompt generation API, you’ll need to:

  1. Have joined the closed research preview for the prompt tools APIs
  2. Use the API directly, rather than the SDK
  3. Add the beta header `prompt-tools-2025-04-02`

This API is not available in the SDK

## Generate a prompt

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

task

string

required

Description of the prompt's purpose.

The `task` parameter tells Claude what the prompt should do or what kind of role or functionality you want to create. This helps guide the prompt generation process toward your intended use case.

Example:
[code]
    {"task": "a chef for a meal prep planning service"}
[/code]

Examples:

`"a chef for a meal prep planning service"`

target\_model

string | null

default:""

The model this prompt will be used for. This optional parameter helps us understand which models our prompt tools are being used with, but it doesn't currently affect functionality.

Example:
[code]
    "claude-3-7-sonnet-20250219"
[/code]

Required string length: `1 - 256`

Examples:

`"claude-3-7-sonnet-20250219"`

#### Response

200

application/json

Successful Response

messages

InputMessage · object\[\]

required

The response contains a list of message objects in the same format used by the Messages API. Typically includes a user message with the complete generated prompt text, and may include an assistant message with a prefill to guide the model's initial response.

These messages can be used directly in a Messages API request to start a conversation with the generated prompt.

Example:
[code]
    {  "messages": [    {      "role": "user",      "content": [        {          "type": "text",          "text": "You are a chef for a meal prep planning service..."        }      ]    },    {      "role": "assistant",      "content": [        {          "type": "text",          "text": "<recipe_planning>"        }      ]    }  ]}
[/code]

Show child attributes

Examples:
[code]
    [  {    "content": [      {        "text": "<generated prompt>",        "type": "text"      }    ],    "role": "user"  }]
[/code]

system

string

default:""

required

Currently, the `system` field is always returned as an empty string \(""\). In future iterations, this field may contain generated system prompts.

Directions similar to what would normally be included in a system prompt are included in `messages` when generating a prompt.

Examples:

`""`

usage

object

required

Usage information

Show child attributes

Was this page helpful?

YesNo

[Get Claude Code Usage Report](/en/api/admin-api/claude-code/get-claude-code-usage-report)[Improve a prompt](/en/api/prompt-tools-improve)
