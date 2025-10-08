url: https://docs.claude.com/en/api/admin-api/apikeys/list-api-keys

---

GET

/

v1

/

organizations

/

api\_keys

cURL

cURL

Copy
[code]
    curl "https://api.anthropic.com/v1/organizations/api_keys" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
[/code]

200

4XX

Copy
[code]
    {
      "data": [
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
      ],
      "first_id": "<string>",
      "has_more": true,
      "last_id": "<string>"
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

status

enum<string> | null

Filter by API key status.

Available options:

`active`,

`inactive`,

`archived`

workspace\_id

string | null

Filter by Workspace ID.

created\_by\_user\_id

string | null

Filter by the ID of the User who created the object.

#### Response

200

application/json

Successful Response

data

ApiKey · object\[\]

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

[Get API Key](/en/api/admin-api/apikeys/get-api-key)[Update API Keys](/en/api/admin-api/apikeys/update-api-key)
