url: https://docs.claude.com/en/api/models

---

GET

/

v1

/

models

/

\{model\_id\}

cURL

cURL

Copy
[code]
    curl https://api.anthropic.com/v1/models/claude-sonnet-4-20250514 \
         --header "x-api-key: $ANTHROPIC_API_KEY" \
         --header "anthropic-version: 2023-06-01"
[/code]

200

4XX

Copy
[code]
    {
      "created_at": "2025-02-19T00:00:00Z",
      "display_name": "Claude Sonnet 4",
      "id": "claude-sonnet-4-20250514",
      "type": "model"
    }
[/code]

#### Headers

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

anthropic-beta

string\[\]

Optional header to specify the beta version\(s\) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

#### Path Parameters

model\_id

string

required

Model identifier or alias.

#### Response

200

application/json

Successful Response

created\_at

string<date-time>

required

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

Examples:

`"2025-02-19T00:00:00Z"`

display\_name

string

required

A human-readable name for the model.

Examples:

`"Claude Sonnet 4"`

id

string

required

Unique model identifier.

Examples:

`"claude-sonnet-4-20250514"`

type

enum<string>

default:model

required

Object type.

For Models, this is always `"model"`.

Available options:Title| Const
---|---
Type| `model`

Was this page helpful?

YesNo

[List Models](/en/api/models-list)[Create a Message Batch](/en/api/creating-message-batches)
