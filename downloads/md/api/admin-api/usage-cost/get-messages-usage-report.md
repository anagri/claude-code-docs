url: https://docs.claude.com/en/api/admin-api/usage-cost/get-messages-usage-report

---

GET

/

v1

/

organizations

/

usage\_report

/

messages

cURL

cURL

Copy
[code]
    curl "https://api.anthropic.com/v1/organizations/usage_report/messages\
    ?starting_at=2025-08-01T00:00:00Z\
    &group_by[]=api_key_id\
    &group_by[]=workspace_id\
    &group_by[]=model\
    &group_by[]=service_tier\
    &group_by[]=context_window\
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
              "uncached_input_tokens": 1500,
              "cache_creation": {
                "ephemeral_1h_input_tokens": 1000,
                "ephemeral_5m_input_tokens": 500
              },
              "cache_read_input_tokens": 200,
              "output_tokens": 500,
              "server_tool_use": {
                "web_search_requests": 10
              },
              "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
              "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
              "model": "claude-sonnet-4-20250514",
              "service_tier": "standard",
              "context_window": "0-200k"
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

Maximum number of time buckets to return in the response.

The default and max limits depend on `bucket_width`: • `"1d"`: Default of 7 days, maximum of 31 days • `"1h"`: Default of 24 hours, maximum of 168 hours • `"1m"`: Default of 60 minutes, maximum of 1440 minutes

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

api\_key\_ids\[\]

string\[\] | null

Restrict usage returned to the specified API key ID\(s\).

Examples:

`"apikey_01Rj2N8SVvo6BePZj99NhmiT"`

workspace\_ids\[\]

string\[\] | null

Restrict usage returned to the specified workspace ID\(s\).

Examples:

`"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"`

models\[\]

string\[\] | null

Restrict usage returned to the specified model\(s\).

Examples:

`"claude-sonnet-4-20250514"`

`"claude-3-5-haiku-20241022"`

service\_tiers\[\]

enum<string>\[\] | null

Restrict usage returned to the specified service tier\(s\).

Show child attributes

Examples:

`"standard"`

`"batch"`

`"priority"`

context\_window\[\]

enum<string>\[\] | null

Restrict usage returned to the specified context window\(s\).

Show child attributes

Examples:

`"0-200k"`

`"200k-1M"`

group\_by\[\]

enum<string>\[\] | null

Group by any subset of the available options.

Show child attributes

Examples:

`"api_key_id"`

`"workspace_id"`

`"model"`

`"service_tier"`

`"context_window"`

bucket\_width

enum<string>

Time granularity of the response data.

Available options:

`1d`,

`1m`,

`1h`

#### Response

200

application/json

Successful Response

data

MessagesUsageReportTimeBucket · object\[\]

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

[Update API Keys](/en/api/admin-api/apikeys/update-api-key)[Get Cost Report](/en/api/admin-api/usage-cost/get-cost-report)
