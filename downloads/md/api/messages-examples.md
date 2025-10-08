url: https://docs.claude.com/en/api/messages-examples

---

See the [API reference](/en/api/messages) for full documentation on available parameters.

## Basic request and response

Shell

Python

TypeScript

Copy
[code]
    #!/bin/sh
    curl https://api.anthropic.com/v1/messages \
         --header "x-api-key: $ANTHROPIC_API_KEY" \
         --header "anthropic-version: 2023-06-01" \
         --header "content-type: application/json" \
         --data \
    '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Hello, Claude"}
        ]
    }'

[/code]

JSON

Copy
[code]
    {
      "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
      "type": "message",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "Hello!"
        }
      ],
      "model": "claude-sonnet-4-5",
      "stop_reason": "end_turn",
      "stop_sequence": null,
      "usage": {
        "input_tokens": 12,
        "output_tokens": 6
      }
    }

[/code]

## Multiple conversational turns

The Messages API is stateless, which means that you always send the full conversational history to the API. You can use this pattern to build up a conversation over time. Earlier conversational turns don’t necessarily need to actually originate from Claude — you can use synthetic `assistant` messages.

Shell

Python

TypeScript

Copy
[code]
    #!/bin/sh
    curl https://api.anthropic.com/v1/messages \
         --header "x-api-key: $ANTHROPIC_API_KEY" \
         --header "anthropic-version: 2023-06-01" \
         --header "content-type: application/json" \
         --data \
    '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Hello, Claude"},
            {"role": "assistant", "content": "Hello!"},
            {"role": "user", "content": "Can you describe LLMs to me?"}

        ]
    }'

[/code]

JSON

Copy
[code]
    {
        "id": "msg_018gCsTGsXkYJVqYPxTgDHBU",
        "type": "message",
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "Sure, I'd be happy to provide..."
            }
        ],
        "stop_reason": "end_turn",
        "stop_sequence": null,
        "usage": {
          "input_tokens": 30,
          "output_tokens": 309
        }
    }

[/code]

## Putting words in Claude’s mouth

You can pre-fill part of Claude’s response in the last position of the input messages list. This can be used to shape Claude’s response. The example below uses `"max_tokens": 1` to get a single multiple choice answer from Claude.

Shell

Python

TypeScript

Copy
[code]
    #!/bin/sh
    curl https://api.anthropic.com/v1/messages \
         --header "x-api-key: $ANTHROPIC_API_KEY" \
         --header "anthropic-version: 2023-06-01" \
         --header "content-type: application/json" \
         --data \
    '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1,
        "messages": [
            {"role": "user", "content": "What is latin for Ant? (A) Apoidea, (B) Rhopalocera, (C) Formicidae"},
            {"role": "assistant", "content": "The answer is ("}
        ]
    }'

[/code]

JSON

Copy
[code]
    {
      "id": "msg_01Q8Faay6S7QPTvEUUQARt7h",
      "type": "message",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "C"
        }
      ],
      "model": "claude-sonnet-4-5",
      "stop_reason": "max_tokens",
      "stop_sequence": null,
      "usage": {
        "input_tokens": 42,
        "output_tokens": 1
      }
    }

[/code]

## Vision

Claude can read both text and images in requests. We support both `base64` and `url` source types for images, and the `image/jpeg`, `image/png`, `image/gif`, and `image/webp` media types. See our [vision guide](/en/docs/build-with-claude/vision) for more details.

Shell

Python

TypeScript

Copy
[code]
    #!/bin/sh

    # Option 1: Base64-encoded image
    IMAGE_URL="https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
    IMAGE_MEDIA_TYPE="image/jpeg"
    IMAGE_BASE64=$(curl "$IMAGE_URL" | base64)

    curl https://api.anthropic.com/v1/messages \
         --header "x-api-key: $ANTHROPIC_API_KEY" \
         --header "anthropic-version: 2023-06-01" \
         --header "content-type: application/json" \
         --data \
    '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": [
                {"type": "image", "source": {
                    "type": "base64",
                    "media_type": "'$IMAGE_MEDIA_TYPE'",
                    "data": "'$IMAGE_BASE64'"
                }},
                {"type": "text", "text": "What is in the above image?"}
            ]}
        ]
    }'

    # Option 2: URL-referenced image
    curl https://api.anthropic.com/v1/messages \
         --header "x-api-key: $ANTHROPIC_API_KEY" \
         --header "anthropic-version: 2023-06-01" \
         --header "content-type: application/json" \
         --data \
    '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": [
                {"type": "image", "source": {
                    "type": "url",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
                }},
                {"type": "text", "text": "What is in the above image?"}
            ]}
        ]
    }'

[/code]

JSON

Copy
[code]
    {
      "id": "msg_01EcyWo6m4hyW8KHs2y2pei5",
      "type": "message",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "This image shows an ant, specifically a close-up view of an ant. The ant is shown in detail, with its distinct head, antennae, and legs clearly visible. The image is focused on capturing the intricate details and features of the ant, likely taken with a macro lens to get an extreme close-up perspective."
        }
      ],
      "model": "claude-sonnet-4-5",
      "stop_reason": "end_turn",
      "stop_sequence": null,
      "usage": {
        "input_tokens": 1551,
        "output_tokens": 71
      }
    }

[/code]

## Tool use, JSON mode, and computer use

See our [guide](/en/docs/agents-and-tools/tool-use/overview) for examples for how to use tools with the Messages API. See our [computer use guide](/en/docs/agents-and-tools/tool-use/computer-use-tool) for examples of how to control desktop computer environments with the Messages API.

Was this page helpful?

YesNo

[Todo Lists](/en/api/agent-sdk/todo-tracking)[Message Batches examples](/en/api/messages-batch-examples)
