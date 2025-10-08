# Directory: organization

## Overview
This directory contains Admin API documentation for retrieving organization information. The endpoint allows administrators to fetch details about their organization using Admin API keys.

## Files in This Directory
### **get-me.md**
API endpoint for retrieving the current organization's information.

**Endpoint:** `GET /v1/organizations/me`

**Key Features:**
- Retrieves organization details for the authenticated admin account
- Returns organization ID, name, and type
- Unavailable for individual accounts (requires organization setup)

**Required Headers:**
- `x-api-key` (string) - Admin API key for authentication (obtain from Console Settings)
- `anthropic-version` (string) - Claude API version (e.g., "2023-06-01")

**Response Fields (200 - application/json):**
- `id` (string<uuid>, required) - Organization UUID
- `name` (string, required) - Organization name
- `type` (enum<string>, required) - Always "organization" for this object type

**Authentication:**
- Uses Admin API key (different from regular API key)
- Must be set up in Console → Settings → Organization
- Individual accounts cannot access this endpoint

**Example Response:**
```json
{
  "id": "12345678-1234-5678-1234-567812345678",
  "name": "Organization Name",
  "type": "organization"
}
```
