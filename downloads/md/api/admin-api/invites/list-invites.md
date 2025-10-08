url: https://docs.claude.com/en/api/admin-api/invites/list-invites

---

GET

/

v1

/

organizations

/

invites

cURL

cURL

Copy
[code]
    curl https://api.anthropic.com/v1/organizations/invites \
         --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
         --header "anthropic-version: 2023-06-01"
[/code]

200

4XX

Copy
[code]
    {
      "data": [
        {
          "email": "[email protected]",
          "expires_at": "2024-11-20T23:58:27.427722Z",
          "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
          "invited_at": "2024-10-30T23:58:27.427722Z",
          "role": "user",
          "status": "pending",
          "type": "invite"
        }
      ],
      "first_id": "<string>",
      "has_more": true,
      "last_id": "<string>"
    }
[/code]

**The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.

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

#### Response

200

application/json

Successful Response

data

InviteSchema · object\[\]

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

[Get Invite](/en/api/admin-api/invites/get-invite)[Create Invite](/en/api/admin-api/invites/create-invite)
