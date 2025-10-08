url: https://docs.claude.com/en/api/messages-batch-examples

---

The Message Batches API supports the same set of features as the Messages API. While this page focuses on how to use the Message Batches API, see [Messages API examples](/en/api/messages-examples) for examples of the Messages API feature set.

## Creating a Message Batch

Python

TypeScript

Shell

Copy
[code]
    import anthropic
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request

    client = anthropic.Anthropic()

    message_batch = client.messages.batches.create(
        requests=[
            Request(
                custom_id="my-first-request",
                params=MessageCreateParamsNonStreaming(
                    model="claude-sonnet-4-5",
                    max_tokens=1024,
                    messages=[{
                        "role": "user",
                        "content": "Hello, world",
                    }]
                )
            ),
            Request(
                custom_id="my-second-request",
                params=MessageCreateParamsNonStreaming(
                    model="claude-sonnet-4-5",
                    max_tokens=1024,
                    messages=[{
                        "role": "user",
                        "content": "Hi again, friend",
                    }]
                )
            )
        ]
    )
    print(message_batch)

[/code]

JSON

Copy
[code]
    {
      "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
      "type": "message_batch",
      "processing_status": "in_progress",
      "request_counts": {
        "processing": 2,
        "succeeded": 0,
        "errored": 0,
        "canceled": 0,
        "expired": 0
      },
      "ended_at": null,
      "created_at": "2024-09-24T18:37:24.100435Z",
      "expires_at": "2024-09-25T18:37:24.100435Z",
      "cancel_initiated_at": null,
      "results_url": null
    }

[/code]

## Polling for Message Batch completion

To poll a Message Batch, you’ll need its `id`, which is provided in the response when creating request or by listing batches. Example `id`: `msgbatch_013Zva2CMHLNnXjNJJKqJ2EF`.

Python

TypeScript

Shell

Copy
[code]
    import anthropic

    client = anthropic.Anthropic()

    message_batch = None
    while True:
        message_batch = client.messages.batches.retrieve(
            MESSAGE_BATCH_ID
        )
        if message_batch.processing_status == "ended":
            break

        print(f"Batch {MESSAGE_BATCH_ID} is still processing...")
        time.sleep(60)
    print(message_batch)

[/code]

## Listing all Message Batches in a Workspace

Python

TypeScript

Shell

Copy
[code]
    import anthropic

    client = anthropic.Anthropic()

    # Automatically fetches more pages as needed.
    for message_batch in client.messages.batches.list(
        limit=20
    ):
        print(message_batch)

[/code]

Output

Copy
[code]
    {
      "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
      "type": "message_batch",
      ...
    }
    {
      "id": "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d",
      "type": "message_batch",
      ...
    }

[/code]

## Retrieving Message Batch Results

Once your Message Batch status is `ended`, you will be able to view the `results_url` of the batch and retrieve results in the form of a `.jsonl` file.

Python

TypeScript

Shell

Copy
[code]
    import anthropic

    client = anthropic.Anthropic()

    # Stream results file in memory-efficient chunks, processing one at a time
    for result in client.messages.batches.results(
        MESSAGE_BATCH_ID,
    ):
        print(result)

[/code]

Output

Copy
[code]
    {
      "id": "my-second-request",
      "result": {
        "type": "succeeded",
        "message": {
          "id": "msg_018gCsTGsXkYJVqYPxTgDHBU",
          "type": "message",
          ...
        }
      }
    }
    {
      "custom_id": "my-first-request",
      "result": {
        "type": "succeeded",
        "message": {
          "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
          "type": "message",
          ...
        }
      }
    }

[/code]

## Canceling a Message Batch

Immediately after cancellation, a batch’s `processing_status` will be `canceling`. You can use the same polling for batch completion technique to poll for when cancellation is finalized as canceled batches also end up `ended` and may contain results.

Python

TypeScript

Shell

Copy
[code]
    import anthropic

    client = anthropic.Anthropic()

    message_batch = client.messages.batches.cancel(
        MESSAGE_BATCH_ID,
    )
    print(message_batch)

[/code]

JSON

Copy
[code]
    {
      "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
      "type": "message_batch",
      "processing_status": "canceling",
      "request_counts": {
        "processing": 2,
        "succeeded": 0,
        "errored": 0,
        "canceled": 0,
        "expired": 0
      },
      "ended_at": null,
      "created_at": "2024-09-24T18:37:24.100435Z",
      "expires_at": "2024-09-25T18:37:24.100435Z",
      "cancel_initiated_at": "2024-09-24T18:39:03.114875Z",
      "results_url": null
    }

[/code]

Was this page helpful?

YesNo

[Messages examples](/en/api/messages-examples)[Amazon Bedrock API](/en/api/claude-on-amazon-bedrock)
