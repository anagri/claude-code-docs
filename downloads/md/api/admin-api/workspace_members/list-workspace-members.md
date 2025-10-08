url: https://docs.claude.com/en/api/admin-api/workspace_members/list-workspace-members

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

cURL

cURL

Copy
[code]
    curl "https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ/members" \
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
          "type": "workspace_member",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
          "workspace_role": "workspace_user"
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

#### Path Parameters

workspace\_id

string

required

ID of the Workspace.

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

WorkspaceMemberSchema · object\[\]

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

[Get Workspace Member](/en/api/admin-api/workspace_members/get-workspace-member)[Add Workspace Member](/en/api/admin-api/workspace_members/create-workspace-member)
