# Directory: apikeys

## Overview
This directory contains Admin API documentation for managing API keys within an organization, including operations to retrieve, list, and update API keys with various filtering and pagination options.

## Files in This Directory

### **get-api-key.md**
Retrieves details of a specific API key by its ID.

- **Endpoint:** `GET /v1/organizations/api_keys/{api_key_id}`
- **Authentication:** Requires Admin API key (`x-api-key` header)
- **Path Parameters:**
  - `api_key_id` (required): ID of the API key to retrieve
- **Response Fields:**
  - `id`: Unique API key identifier (e.g., `apikey_01Rj2N8SVvo6BePZj99NhmiT`)
  - `name`: Human-readable name for the API key
  - `status`: Current state (`active`, `inactive`, or `archived`)
  - `partial_key_hint`: Partially redacted key hint (e.g., `sk-ant-api03-R2D...igAA`)
  - `created_at`: RFC 3339 datetime of creation
  - `created_by`: Object containing ID and type of creator
  - `workspace_id`: Associated workspace ID or null for default workspace
  - `type`: Always `api_key` for API key objects

### **list-api-keys.md**
Lists all API keys in the organization with pagination and filtering capabilities.

- **Endpoint:** `GET /v1/organizations/api_keys`
- **Authentication:** Requires Admin API key (`x-api-key` header)
- **Query Parameters:**
  - `before_id`: Cursor for pagination (returns page before this ID)
  - `after_id`: Cursor for pagination (returns page after this ID)
  - `limit`: Items per page (default: 20, range: 1-1000)
  - `status`: Filter by status (`active`, `inactive`, or `archived`)
  - `workspace_id`: Filter by workspace ID
  - `created_by_user_id`: Filter by creator user ID
- **Response Structure:**
  - `data`: Array of API key objects
  - `first_id`: First ID in the list (for previous page navigation)
  - `last_id`: Last ID in the list (for next page navigation)
  - `has_more`: Boolean indicating if more results exist

### **update-api-key.md**
Updates an existing API key's name or status.

- **Endpoint:** `POST /v1/organizations/api_keys/{api_key_id}`
- **Authentication:** Requires Admin API key (`x-api-key` header)
- **Path Parameters:**
  - `api_key_id` (required): ID of the API key to update
- **Request Body:**
  - `name`: New name for the API key (1-500 characters)
  - `status`: New status (`active`, `inactive`, or `archived`)
- **Response:** Returns the updated API key object with all fields
- **Use Cases:**
  - Rename API keys for better organization
  - Deactivate or archive keys without deletion
  - Reactivate previously inactive keys
