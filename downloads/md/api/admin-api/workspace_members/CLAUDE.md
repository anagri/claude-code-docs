# Directory: workspace_members

## Overview
This directory contains API reference documentation for managing workspace members in the Claude Admin API. These endpoints allow organization administrators to add, update, retrieve, list, and remove members from workspaces with different role assignments.

## Files in This Directory

### **create-workspace-member.md**
Documents the POST endpoint for adding a new member to a workspace.

- Endpoint: `POST /v1/organizations/workspaces/{workspace_id}/members`
- Path Parameters: `workspace_id` (required)
- Body Parameters:
  - `user_id` (string, required) - ID of the user to add
  - `workspace_role` (enum, required) - Role assignment for the new member
- Available Roles: `workspace_user`, `workspace_developer`, `workspace_admin`
- Restriction: Cannot assign `workspace_billing` role during creation
- Response: Returns workspace member object with type, user_id, workspace_id, and workspace_role
- Note: Admin API unavailable for individual accounts; requires organization setup

### **delete-workspace-member.md**
Documents the DELETE endpoint for removing a member from a workspace.

- Endpoint: `DELETE /v1/organizations/workspaces/{workspace_id}/members/{user_id}`
- Path Parameters:
  - `workspace_id` (string, required) - ID of the workspace
  - `user_id` (string, required) - ID of the user to remove
- Response: Returns deleted object confirmation with type `workspace_member_deleted`, user_id, and workspace_id
- Authentication: Requires Admin API key in header
- Note: Requires organization-level access

### **get-workspace-member.md**
Documents the GET endpoint for retrieving a specific workspace member's details.

- Endpoint: `GET /v1/organizations/workspaces/{workspace_id}/members/{user_id}`
- Path Parameters:
  - `workspace_id` (string, required) - ID of the workspace
  - `user_id` (string, required) - ID of the user to retrieve
- Response Fields:
  - `type` - Always `workspace_member`
  - `user_id` - User identifier
  - `workspace_id` - Workspace identifier
  - `workspace_role` - Current role (workspace_user, workspace_developer, workspace_admin, or workspace_billing)
- Use Case: Verify member status and role assignment

### **list-workspace-members.md**
Documents the GET endpoint for retrieving all members in a workspace with pagination support.

- Endpoint: `GET /v1/organizations/workspaces/{workspace_id}/members`
- Path Parameters: `workspace_id` (required)
- Query Parameters:
  - `before_id` (string, optional) - Cursor for previous page
  - `after_id` (string, optional) - Cursor for next page
  - `limit` (integer, optional) - Results per page (default: 20, range: 1-1000)
- Response Structure:
  - `data` - Array of workspace member objects
  - `first_id` - First ID in current page (for previous page navigation)
  - `last_id` - Last ID in current page (for next page navigation)
  - `has_more` - Boolean indicating if more results exist
- Pagination: Uses cursor-based pagination with before_id/after_id

### **update-workspace-member.md**
Documents the POST endpoint for modifying a workspace member's role.

- Endpoint: `POST /v1/organizations/workspaces/{workspace_id}/members/{user_id}`
- Path Parameters:
  - `workspace_id` (string, required) - ID of the workspace
  - `user_id` (string, required) - ID of the user to update
- Body Parameters:
  - `workspace_role` (enum, required) - New role assignment
- Available Roles: `workspace_user`, `workspace_developer`, `workspace_admin`, `workspace_billing`
- Note: Unlike creation, update allows assignment of `workspace_billing` role
- Response: Returns updated workspace member object with new role
- Use Case: Role promotions, demotions, or permission adjustments
