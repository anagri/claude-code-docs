url: https://docs.claude.com/en/api/admin-api/claude-code/get-claude-code-usage-report

---

GET

/

v1

/

organizations

/

usage\_report

/

claude\_code

cURL

cURL

Copy
[code]
    curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code\
    ?starting_at=2025-08-08\
    &limit=20" \
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
          "actor": {
            "email_address": "[email protected]",
            "type": "user_actor"
          },
          "core_metrics": {
            "commits_by_claude_code": 8,
            "lines_of_code": {
              "added": 342,
              "removed": 128
            },
            "num_sessions": 15,
            "pull_requests_by_claude_code": 2
          },
          "customer_type": "api",
          "date": "2025-08-08T00:00:00Z",
          "model_breakdown": [
            {
              "estimated_cost": {
                "amount": 186,
                "currency": "USD"
              },
              "model": "claude-sonnet-4-20250514",
              "tokens": {
                "cache_creation": 2340,
                "cache_read": 8790,
                "input": 45230,
                "output": 12450
              }
            },
            {
              "estimated_cost": {
                "amount": 42,
                "currency": "USD"
              },
              "model": "claude-3-5-haiku-20241022",
              "tokens": {
                "cache_creation": 890,
                "cache_read": 3420,
                "input": 23100,
                "output": 5680
              }
            }
          ],
          "organization_id": "12345678-1234-5678-1234-567812345678",
          "subscription_type": "enterprise",
          "terminal_type": "iTerm.app",
          "tool_actions": {
            "edit_tool": {
              "accepted": 25,
              "rejected": 3
            },
            "multi_edit_tool": {
              "accepted": 12,
              "rejected": 1
            },
            "notebook_edit_tool": {
              "accepted": 5,
              "rejected": 2
            },
            "write_tool": {
              "accepted": 8,
              "rejected": 0
            }
          }
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

starting\_at

string

required

UTC date in YYYY-MM-DD format. Returns metrics for this single day only.

limit

integer

default:20

Number of records per page \(default: 20, max: 1000\).

Required range: `1 <= x <= 1000`

page

string | null

Opaque cursor token from previous response's `next_page` field.

#### Response

200

application/json

Successful Response

data

ClaudeCodeUsageReportItem · object\[\]

required

List of Claude Code usage records for the requested date.

Show child attributes

has\_more

boolean

required

True if there are more records available beyond the current page.

next\_page

string | null

required

Opaque cursor token for fetching the next page of results, or null if no more pages are available.

Examples:

`"page_MjAyNS0wNS0xNFQwMDowMDowMFo="`

`null`

Was this page helpful?

YesNo

[Get Cost Report](/en/api/admin-api/usage-cost/get-cost-report)[Generate a prompt](/en/api/prompt-tools-generate)
