url: https://docs.claude.com/en/api/listing-message-batches

---

GET

/

v1

/

messages

/

batches

cURL

cURL

Copy
[code]
    curl https://api.anthropic.com/v1/messages/batches \
         --header "x-api-key: $ANTHROPIC_API_KEY" \
         --header "anthropic-version: 2023-06-01"
[/code]

200

4XX

Copy
[code]
    {
      "data": [
        {
          "archived_at": "2024-08-20T18:37:24.100435Z",
          "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
          "created_at": "2024-08-20T18:37:24.100435Z",
          "ended_at": "2024-08-20T18:37:24.100435Z",
          "expires_at": "2024-08-20T18:37:24.100435Z",
          "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
          "processing_status": "in_progress",
          "request_counts": {
            "canceled": 10,
            "errored": 30,
            "expired": 10,
            "processing": 100,
            "succeeded": 50
          },
          "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
          "type": "message_batch"
        }
      ],
      "first_id": "<string>",
      "has_more": true,
      "last_id": "<string>"
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

#### Query Parameters

before\_id

string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

after\_id

string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

limit

integer

default:20

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

Required range: `1 <= x <= 1000`

#### Response

200

application/json

Successful Response

data

MessageBatch · object\[\]

required

Show child attributes

first\_id

string | null

required

First ID in the `data` list. Can be used as the `before_id` for the previous page.

has\_more

boolean

required

Indicates if there are more results in the requested page direction.

last\_id

string | null

required

Last ID in the `data` list. Can be used as the `after_id` for the next page.

Was this page helpful?

YesNo

[Retrieve Message Batch Results](/en/api/retrieving-message-batch-results)[Cancel a Message Batch](/en/api/canceling-message-batches)
