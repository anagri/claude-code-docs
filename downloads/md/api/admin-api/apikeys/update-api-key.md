url: https://docs.claude.com/en/api/admin-api/apikeys/update-api-key

---

POST

/

v1

/

organizations

/

api\_keys

/

\{api\_key\_id\}

cURL

cURL

Copy
[code]
    curl "https://api.anthropic.com/v1/organizations/api_keys/apikey_01Rj2N8SVvo6BePZj99NhmiT" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
      --data '{
        "status": "active",
        "name": "Developer Key"
      }'
[/code]

200

4XX

Copy
[code]
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "type": "user"
      },
      "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
      "name": "Developer Key",
      "partial_key_hint": "sk-ant-api03-R2D...igAA",
      "status": "active",
      "type": "api_key",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
    }
[/code]

#### Headers

x-api-key

string

required

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the [Console](https://console.anthropic.com/settings/admin-keys).

anthropic-version

string

required

The version of the Claude API you want to use.

Read more about versioning and our version history [here](/api/versioning).

#### Path Parameters

api\_key\_id

string

required

ID of the API key.

#### Body

application/json

name

string

Name of the API key.

Required string length: `1 - 500`

status

enum<string> | null

Status of the API key.

Available options:

`active`,

`inactive`,

`archived`

#### Response

200

application/json

Successful Response

created\_at

string<date-time>

required

RFC 3339 datetime string indicating when the API Key was created.

Examples:

`"2024-10-30T23:58:27.427722Z"`

created\_by

object

required

The ID and type of the actor that created the API key.

Show child attributes

id

string

required

ID of the API key.

Examples:

`"apikey_01Rj2N8SVvo6BePZj99NhmiT"`

name

string

required

Name of the API key.

Examples:

`"Developer Key"`

partial\_key\_hint

string | null

required

Partially redacted hint for the API key.

Examples:

`"sk-ant-api03-R2D...igAA"`

status

enum<string>

required

Status of the API key.

Available options:

`active`,

`inactive`,

`archived`

Examples:

`"active"`

type

enum<string>

default:api\_key

required

Object type.

For API Keys, this is always `"api_key"`.

Available options:Title| Const
---|---
Type| `api_key`

workspace\_id

string | null

required

ID of the Workspace associated with the API key, or null if the API key belongs to the default Workspace.

Examples:

`"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"`

Was this page helpful?

YesNo

[List API Keys](/en/api/admin-api/apikeys/list-api-keys)[Get Usage Report for the Messages API](/en/api/admin-api/usage-cost/get-messages-usage-report)
