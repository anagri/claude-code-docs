url: https://docs.claude.com/en/api/admin-api/usage-cost/get-cost-report

---

GET

/

v1

/

organizations

/

cost\_report

cURL

cURL

Copy
[code]
    curl "https://api.anthropic.com/v1/organizations/cost_report\
    ?starting_at=2025-08-01T00:00:00Z\
    &group_by[]=workspace_id\
    &group_by[]=description\
    &limit=1" \
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
          "starting_at": "2025-08-01T00:00:00Z",
          "ending_at": "2025-08-02T00:00:00Z",
          "results": [
            {
              "currency": "USD",
              "amount": "123.78912",
              "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
              "description": "Claude Sonnet 4 Usage - Input Tokens",
              "cost_type": "tokens",
              "context_window": "0-200k",
              "model": "claude-sonnet-4-20250514",
              "service_tier": "standard",
              "token_type": "uncached_input_tokens"
            }
          ]
        }
      ],
      "has_more": true,
      "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
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

limit

integer

default:7

Maximum number of time buckets to return in the response.

Required range: `1 <= x <= 31`

Examples:

`7`

page

string<date-time> | null

Optionally set to the `next_page` token from the previous response.

Examples:

`"page_MjAyNS0wNS0xNFQwMDowMDowMFo="`

`null`

starting\_at

string<date-time>

required

Time buckets that start on or after this RFC 3339 timestamp will be returned. Each time bucket will be snapped to the start of the minute/hour/day in UTC.

Examples:

`"2024-10-30T23:58:27.427722Z"`

ending\_at

string<date-time> | null

Time buckets that end before this RFC 3339 timestamp will be returned.

Examples:

`"2024-10-30T23:58:27.427722Z"`

group\_by\[\]

enum<string>\[\] | null

Group by any subset of the available options.

Show child attributes

Examples:

`"workspace_id"`

`"description"`

bucket\_width

enum<string>

Time granularity of the response data.

Available options:Title| Const
---|---
CostReportTimeBucketWidth| `1d`

#### Response

200

application/json

Successful Response

data

CostReportTimeBucket · object\[\]

required

Show child attributes

has\_more

boolean

required

Indicates if there are more results.

next\_page

string<date-time> | null

required

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

Examples:

`"page_MjAyNS0wNS0xNFQwMDowMDowMFo="`

`null`

Was this page helpful?

YesNo

[Get Usage Report for the Messages API](/en/api/admin-api/usage-cost/get-messages-usage-report)[Get Claude Code Usage Report](/en/api/admin-api/claude-code/get-claude-code-usage-report)
