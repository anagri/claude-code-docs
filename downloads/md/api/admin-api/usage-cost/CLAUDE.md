# Directory: usage-cost

## Overview
This directory contains Admin API endpoints for retrieving cost and usage reports for Claude API usage. These endpoints enable organizations to track spending and token usage across workspaces, API keys, and models.

## Files in This Directory

### **get-cost-report.md**
Documents the GET `/v1/organizations/cost_report` endpoint for retrieving cost reports grouped by various dimensions.

- **Endpoint**: `GET /v1/organizations/cost_report`
- **Authentication**: Requires Admin API key via `x-api-key` header
- **Required Parameters**:
  - `starting_at`: RFC 3339 timestamp for report start (snapped to UTC minute/hour/day)
  - `anthropic-version`: API version header (required)
- **Optional Parameters**:
  - `ending_at`: RFC 3339 timestamp for report end
  - `limit`: Number of time buckets to return (default: 7, range: 1-31)
  - `page`: Pagination token from previous response
  - `group_by[]`: Group results by workspace_id, description, or other dimensions
  - `bucket_width`: Time granularity (only `1d` available)
- **Response Structure**:
  - Returns cost data in time buckets with currency, amount, workspace_id, model, service_tier, token_type
  - Includes pagination support with `has_more` and `next_page` fields
  - Cost breakdown includes description, cost_type, context_window details
- **Notes**: Unavailable for individual accounts; requires organization setup

### **get-messages-usage-report.md**
Documents the GET `/v1/organizations/usage_report/messages` endpoint for retrieving detailed token usage statistics for the Messages API.

- **Endpoint**: `GET /v1/organizations/usage_report/messages`
- **Authentication**: Requires Admin API key via `x-api-key` header
- **Required Parameters**:
  - `starting_at`: RFC 3339 timestamp for report start (snapped to UTC minute/hour/day)
  - `anthropic-version`: API version header (required)
- **Optional Parameters**:
  - `ending_at`: RFC 3339 timestamp for report end
  - `limit`: Number of time buckets (defaults/max vary by bucket_width: 7/31 for 1d, 24/168 for 1h, 60/1440 for 1m)
  - `page`: Pagination token from previous response
  - `bucket_width`: Time granularity (`1d`, `1h`, or `1m`)
  - **Filtering Arrays**:
    - `api_key_ids[]`: Filter by specific API key IDs
    - `workspace_ids[]`: Filter by specific workspace IDs
    - `models[]`: Filter by model names (e.g., claude-sonnet-4-20250514)
    - `service_tiers[]`: Filter by service tier (standard, batch, priority)
    - `context_window[]`: Filter by context window size (0-200k, 200k-1M)
  - `group_by[]`: Group by api_key_id, workspace_id, model, service_tier, or context_window
- **Response Structure**:
  - Returns token usage broken down by type: uncached_input_tokens, output_tokens, cache_read_input_tokens
  - Includes cache creation metrics (ephemeral_1h_input_tokens, ephemeral_5m_input_tokens)
  - Includes server_tool_use metrics (e.g., web_search_requests)
  - Pagination support with `has_more` and `next_page` fields
- **Notes**: Unavailable for individual accounts; requires organization setup
