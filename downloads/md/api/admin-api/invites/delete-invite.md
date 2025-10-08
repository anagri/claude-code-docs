url: https://docs.claude.com/en/api/admin-api/invites/delete-invite

---

DELETE

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
    curl --request DELETE "https://api.anthropic.com/v1/organizations/invites/invite_015gWxCN9Hfg2QhZwTK7Mdeu" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
[/code]

200

4XX

Copy
[code]
    {
      "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
      "type": "invite_deleted"
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

id

string

required

ID of the Invite.

Examples:

`"invite_015gWxCN9Hfg2QhZwTK7Mdeu"`

type

enum<string>

default:invite\_deleted

required

Deleted object type.

For Invites, this is always `"invite_deleted"`.

Available options:Title| Const
---|---
Type| `invite_deleted`

Was this page helpful?

YesNo

[Create Invite](/en/api/admin-api/invites/create-invite)[Get Workspace](/en/api/admin-api/workspaces/get-workspace)
