url: https://docs.claude.com/en/api/deleting-message-batches

---

DELETE

/

v1

/

messages

/

batches

/

\{message\_batch\_id\}

cURL

cURL

Copy
[code]
    curl -X DELETE https://api.anthropic.com/v1/messages/batches/msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d \
         --header "x-api-key: $ANTHROPIC_API_KEY" \
         --header "anthropic-version: 2023-06-01"
[/code]

200

4XX

Copy
[code]
    {
      "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
      "type": "message_batch_deleted"
    }
[/code]

#### Headers

anthropic-beta

string\[\]

Optional header to specify the beta version\(s\) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

anthropic-version

string

required

The version of the Claude API you want to use.

Read more about versioning and our version history [here](/api/versioning).

x-api-key

string

required

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a Workspace.

#### Path Parameters

message\_batch\_id

string

required

ID of the Message Batch.

#### Response

200

application/json

Successful Response

id

string

required

ID of the Message Batch.

Examples:

`"msgbatch_013Zva2CMHLNnXjNJJKqJ2EF"`

type

enum<string>

default:message\_batch\_deleted

required

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Available options:Title| Const
---|---
Type| `message_batch_deleted`

Was this page helpful?

YesNo

[Cancel a Message Batch](/en/api/canceling-message-batches)[Create a File](/en/api/files-create)
