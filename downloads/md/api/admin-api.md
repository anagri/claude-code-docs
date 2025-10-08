url: https://docs.claude.com/en/api/admin-api

---

GET

/

v1

/

organizations

/

me

cURL

cURL

Copy
[code]
    curl "https://api.anthropic.com/v1/organizations/me" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
[/code]

200

4XX

Copy
[code]
    {
      "id": "12345678-1234-5678-1234-567812345678",
      "name": "Organization Name",
      "type": "organization"
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

#### Response

200

application/json

Successful Response

id

string<uuid>

required

ID of the Organization.

Examples:

`"12345678-1234-5678-1234-567812345678"`

name

string

required

Name of the Organization.

Examples:

`"Organization Name"`

type

enum<string>

default:organization

required

Object type.

For Organizations, this is always `"organization"`.

Available options:Title| Const
---|---
Type| `organization`

Was this page helpful?

YesNo

[Delete a File](/en/api/files-delete)[Get User](/en/api/admin-api/users/get-user)
