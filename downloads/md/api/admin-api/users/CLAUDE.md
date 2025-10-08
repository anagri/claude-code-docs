# Directory: users

## Overview
This directory contains Admin API reference documentation for managing users within an organization, including operations to retrieve, list, update, and remove users.

## Files in This Directory
### **get-user.md**
Retrieves detailed information about a specific user by ID.
- Endpoint: `GET /v1/organizations/users/{user_id}`
- Path Parameters:
  - `user_id` (required): ID of the user to retrieve
- Response includes:
  - User ID, email, name
  - Organization role (user, developer, billing, admin, claude_code_user)
  - Added timestamp (RFC 3339 datetime)
  - Type field (always "user")
- Authentication: Requires `x-api-key` header with Admin API key
- Versioning: Requires `anthropic-version` header (e.g., "2023-06-01")

### **list-users.md**
Returns a paginated list of all users in the organization.
- Endpoint: `GET /v1/organizations/users`
- Query Parameters:
  - `limit` (optional): Number of items per page (default: 20, range: 1-1000)
  - `before_id` (optional): Cursor for pagination (page before this ID)
  - `after_id` (optional): Cursor for pagination (page after this ID)
  - `email` (optional): Filter users by email address
- Response structure:
  - `data`: Array of user objects
  - `first_id`: First ID in the list (for previous page navigation)
  - `last_id`: Last ID in the list (for next page navigation)
  - `has_more`: Boolean indicating more results available
- Each user object contains: id, email, name, role, added_at, type
- Authentication: Requires `x-api-key` header with Admin API key

### **remove-user.md**
Deletes a user from the organization.
- Endpoint: `DELETE /v1/organizations/users/{user_id}`
- Path Parameters:
  - `user_id` (required): ID of the user to remove
- Response on success:
  - `id`: ID of the deleted user
  - `type`: Always "user_deleted"
- Authentication: Requires `x-api-key` header with Admin API key
- Versioning: Requires `anthropic-version` header
- Note: Permanently removes user access from the organization

### **update-user.md**
Updates a user's organization role.
- Endpoint: `POST /v1/organizations/users/{user_id}`
- Path Parameters:
  - `user_id` (required): ID of the user to update
- Request Body:
  - `role` (required): New role for the user
  - Available roles: user, developer, billing, admin, claude_code_user
  - Restriction: Cannot be set to "admin" via this endpoint
- Response: Returns updated user object with all fields
  - id, email, name, role, added_at, type
- Authentication: Requires `x-api-key` header with Admin API key
- Use case: Change user permissions within the organization
