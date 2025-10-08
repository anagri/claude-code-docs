# Directory: claude-code

## Overview
This directory contains API reference documentation for retrieving Claude Code usage reports through the Admin API. It provides detailed metrics on Claude Code activity, including session counts, code changes, model usage, and tool interactions.

## Files in This Directory
### **get-claude-code-usage-report.md**
API endpoint for retrieving Claude Code usage metrics for a specific date.

**Endpoint:** `GET /v1/organizations/usage_report/claude_code`

**Key Query Parameters:**
- `starting_at` (required): UTC date in YYYY-MM-DD format - returns metrics for this single day only
- `limit` (optional): Number of records per page (default: 20, max: 1000)
- `page` (optional): Opaque cursor token for pagination from previous response's `next_page` field

**Required Headers:**
- `x-api-key`: Admin API key for authentication
- `anthropic-version`: API version (e.g., "2023-06-01")

**Response Metrics:**
- **Actor Information**: User email and type
- **Core Metrics**:
  - Number of sessions
  - Commits by Claude Code
  - Pull requests by Claude Code
  - Lines of code added/removed
- **Model Breakdown**: Token usage and estimated costs per model (input, output, cache creation, cache read)
- **Tool Actions**: Accept/reject counts for edit tools (edit_tool, multi_edit_tool, notebook_edit_tool, write_tool)
- **Environment Details**: Terminal type, organization ID, subscription type, customer type

**Pagination:**
- `has_more`: Boolean indicating if more records exist
- `next_page`: Cursor token for fetching next page (null if no more pages)

**Availability:** Admin API is unavailable for individual accounts - requires organization setup in Console
