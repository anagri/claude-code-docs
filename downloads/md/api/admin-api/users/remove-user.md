url: https://docs.claude.com/en/api/admin-api/users/remove-user

---

DELETE

/

v1

/

organizations

/

users

/

\{user\_id\}

cURL

cURL

Copy
[code]
    curl --request DELETE "https://api.anthropic.com/v1/organizations/users/user_01WCz1FkmYMm4gnmykNKUu3Q" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
[/code]

200

4XX

Copy
[code]
    {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "type": "user_deleted"
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

user\_id

string

required

ID of the User.

#### Response

200

application/json

Successful Response

id

string

required

ID of the User.

Examples:

`"user_01WCz1FkmYMm4gnmykNKUu3Q"`

type

enum<string>

default:user\_deleted

required

Deleted object type.

For Users, this is always `"user_deleted"`.

Available options:Title| Const
---|---
Type| `user_deleted`

Was this page helpful?

YesNo

[Update User](/en/api/admin-api/users/update-user)[Get Invite](/en/api/admin-api/invites/get-invite)
