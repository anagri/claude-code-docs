url: https://docs.claude.com/en/api/admin-api/invites/get-invite

---

GET

/

v1

/

organizations

/

invites

/

\{invite\_id\}

cURL

cURL

Copy
[code]
    curl "https://api.anthropic.com/v1/organizations/invites/invite_015gWxCN9Hfg2QhZwTK7Mdeu" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
[/code]

200

4XX

Copy
[code]
    {
      "email": "[email protected]",
      "expires_at": "2024-11-20T23:58:27.427722Z",
      "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
      "invited_at": "2024-10-30T23:58:27.427722Z",
      "role": "user",
      "status": "pending",
      "type": "invite"
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

#### Path Parameters

invite\_id

string

required

ID of the Invite.

#### Response

200

application/json

Successful Response

email

string

required

Email of the User being invited.

Examples:

`"[email protected]"`

expires\_at

string<date-time>

required

RFC 3339 datetime string indicating when the Invite expires.

Examples:

`"2024-11-20T23:58:27.427722Z"`

id

string

required

ID of the Invite.

Examples:

`"invite_015gWxCN9Hfg2QhZwTK7Mdeu"`

invited\_at

string<date-time>

required

RFC 3339 datetime string indicating when the Invite was created.

Examples:

`"2024-10-30T23:58:27.427722Z"`

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

status

enum<string>

required

Status of the Invite.

Available options:

`accepted`,

`expired`,

`deleted`,

`pending`

type

enum<string>

default:invite

required

Object type.

For Invites, this is always `"invite"`.

Available options:Title| Const
---|---
Type| `invite`

Was this page helpful?

YesNo

[Remove User](/en/api/admin-api/users/remove-user)[List Invites](/en/api/admin-api/invites/list-invites)
