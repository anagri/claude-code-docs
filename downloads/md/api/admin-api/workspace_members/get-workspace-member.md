url: https://docs.claude.com/en/api/admin-api/workspace_members/get-workspace-member

---

GET

/

v1

/

organizations

/

workspaces

/

\{workspace\_id\}

/

members

/

\{user\_id\}

cURL

cURL

Copy
[code]
    curl "https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ/members/user_01WCz1FkmYMm4gnmykNKUu3Q" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
[/code]

200

4XX

Copy
[code]
    {
      "type": "workspace_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "workspace_role": "workspace_user"
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

user\_id

string

required

ID of the User.

workspace\_id

string

required

ID of the Workspace.

#### Response

200

application/json

Successful Response

type

enum<string>

default:workspace\_member

required

Object type.

For Workspace Members, this is always `"workspace_member"`.

Available options:Title| Const
---|---
Type| `workspace_member`

user\_id

string

required

ID of the User.

Examples:

`"user_01WCz1FkmYMm4gnmykNKUu3Q"`

workspace\_id

string

required

ID of the Workspace.

Examples:

`"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"`

workspace\_role

enum<string>

required

Role of the Workspace Member.

Available options:

`workspace_user`,

`workspace_developer`,

`workspace_admin`,

`workspace_billing`

Was this page helpful?

YesNo

[Archive Workspace](/en/api/admin-api/workspaces/archive-workspace)[List Workspace Members](/en/api/admin-api/workspace_members/list-workspace-members)
