# Directory: workspaces

## Overview
This directory contains API reference documentation for workspace management endpoints in the Claude Admin API. These endpoints allow you to create, retrieve, list, update, and archive workspaces within your organization.

## Files in This Directory

### **archive-workspace.md**
Archives a workspace by its ID using a POST request to `/v1/organizations/workspaces/{workspace_id}/archive`.

- **Method:** POST
- **Path Parameters:** `workspace_id` (string, required) - ID of the Workspace to archive
- **Headers:**
  - `x-api-key` (required) - Admin API key for authentication
  - `anthropic-version` (required) - API version (e.g., "2023-06-01")
- **Response:** Returns workspace object with `archived_at` timestamp set to RFC 3339 datetime
- **Key Fields:** id, name, display_color, archived_at, created_at, type (always "workspace")

### **create-workspace.md**
Creates a new workspace within the organization using a POST request to `/v1/organizations/workspaces`.

- **Method:** POST
- **Body Parameters:** `name` (string, required) - Workspace name (1-40 characters)
- **Headers:**
  - `x-api-key` (required) - Admin API key for authentication
  - `anthropic-version` (required) - API version
- **Response:** Returns newly created workspace object with auto-generated ID and display color
- **Key Fields:** id, name, display_color, created_at, archived_at (null for new workspaces), type

### **get-workspace.md**
Retrieves details of a specific workspace by ID using a GET request to `/v1/organizations/workspaces/{workspace_id}`.

- **Method:** GET
- **Path Parameters:** `workspace_id` (string, required) - ID of the Workspace to retrieve
- **Headers:**
  - `x-api-key` (required) - Admin API key for authentication
  - `anthropic-version` (required) - API version
- **Response:** Returns complete workspace object with all metadata
- **Key Fields:** id, name, display_color (hex color code), archived_at, created_at, type

### **list-workspaces.md**
Retrieves a paginated list of all workspaces in the organization using a GET request to `/v1/organizations/workspaces`.

- **Method:** GET
- **Query Parameters:**
  - `include_archived` (boolean, default: false) - Include archived workspaces
  - `limit` (integer, default: 20, range: 1-1000) - Number of items per page
  - `before_id` (string) - Cursor for pagination (previous page)
  - `after_id` (string) - Cursor for pagination (next page)
- **Headers:** `x-api-key`, `anthropic-version` (both required)
- **Response:** Returns paginated list with `data` array, `first_id`, `last_id`, and `has_more` flag
- **Pagination:** Uses cursor-based pagination with `before_id`/`after_id` for navigation

### **update-workspace.md**
Updates an existing workspace's name using a POST request to `/v1/organizations/workspaces/{workspace_id}`.

- **Method:** POST
- **Path Parameters:** `workspace_id` (string, required) - ID of the Workspace to update
- **Body Parameters:** `name` (string, required) - New workspace name (1-40 characters)
- **Headers:**
  - `x-api-key` (required) - Admin API key for authentication
  - `anthropic-version` (required) - API version
- **Response:** Returns updated workspace object with modified name
- **Key Fields:** All workspace fields returned with updated name value
