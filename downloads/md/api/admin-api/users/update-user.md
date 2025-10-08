url: https://docs.claude.com/en/api/admin-api/users/update-user

---

POST

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
    curl "https://api.anthropic.com/v1/organizations/users/user_01WCz1FkmYMm4gnmykNKUu3Q" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
      --data '{
        "role": "user"
      }'
[/code]

200

4XX

Copy
[code]
    {
      "added_at": "2024-10-30T23:58:27.427722Z",
      "email": "[email protected]",
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "name": "Jane Doe",
      "role": "user",
      "type": "user"
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

#### Body

application/json

role

enum<string>

required

New role for the User. Cannot be "admin".

Available options:

`user`,

`developer`,

`billing`,

`admin`,

`claude_code_user`

#### Response

200

application/json

Successful Response

added\_at

string<date-time>

required

RFC 3339 datetime string indicating when the User joined the Organization.

Examples:

`"2024-10-30T23:58:27.427722Z"`

email

string

required

Email of the User.

Examples:

`"[email protected]"`

id

string

required

ID of the User.

Examples:

`"user_01WCz1FkmYMm4gnmykNKUu3Q"`

name

string

required

Name of the User.

Examples:

`"Jane Doe"`

role

enum<string>

required

Organization role of the User.

Available options:

`user`,

`developer`,

`billing`,

`admin`,

`claude_code_user`

type

enum<string>

default:user

required

Object type.

For Users, this is always `"user"`.

Available options:Title| Const
---|---
Type| `user`

Was this page helpful?

YesNo

[List Users](/en/api/admin-api/users/list-users)[Remove User](/en/api/admin-api/users/remove-user)
