url: https://docs.claude.com/en/api/admin-api/workspaces/archive-workspace

---

POST

/

v1

/

organizations

/

workspaces

/

\{workspace\_id\}

/

archive

cURL

cURL

Copy
[code]
    curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ/archive" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
[/code]

200

4XX

Copy
[code]
    {
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_color": "#6C5BB9",
      "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "name": "Workspace Name",
      "type": "workspace"
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

workspace\_id

string

required

ID of the Workspace.

#### Response

200

application/json

Successful Response

archived\_at

string<date-time> | null

required

RFC 3339 datetime string indicating when the Workspace was archived, or null if the Workspace is not archived.

Examples:

`"2024-11-01T23:59:27.427722Z"`

created\_at

string<date-time>

required

RFC 3339 datetime string indicating when the Workspace was created.

Examples:

`"2024-10-30T23:58:27.427722Z"`

display\_color

string

required

Hex color code representing the Workspace in the Anthropic Console.

Examples:

`"#6C5BB9"`

id

string

required

ID of the Workspace.

Examples:

`"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"`

name

string

required

Name of the Workspace.

Examples:

`"Workspace Name"`

type

enum<string>

default:workspace

required

Object type.

For Workspaces, this is always `"workspace"`.

Available options:Title| Const
---|---
Type| `workspace`

Was this page helpful?

YesNo

[Create Workspace](/en/api/admin-api/workspaces/create-workspace)[Get Workspace Member](/en/api/admin-api/workspace_members/get-workspace-member)
