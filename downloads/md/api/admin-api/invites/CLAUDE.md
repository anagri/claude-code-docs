# Directory: invites

## Overview
This directory contains API reference documentation for managing organization invitations in the Claude Admin API. These endpoints allow administrators to create, retrieve, list, and delete user invitations to their organization.

## Files in This Directory

### **create-invite.md**
Documents the POST endpoint for creating organization invitations.

- **Endpoint:** `POST /v1/organizations/invites`
- **Purpose:** Invite a new user to the organization via email
- **Required Parameters:**
  - `email` (string): Email address of the user to invite
  - `role` (enum): Organization role - `user`, `developer`, `billing`, `admin`, or `claude_code_user` (cannot be "admin")
- **Headers:** Requires `x-api-key` (Admin API key) and `anthropic-version`
- **Response:** Returns invite object with:
  - `id`: Unique invite identifier
  - `email`: Invitee's email address
  - `invited_at`: RFC 3339 datetime when invite was created
  - `expires_at`: RFC 3339 datetime when invite expires (21 days from creation)
  - `role`: Assigned organization role
  - `status`: Invite status (`pending`, `accepted`, `expired`, or `deleted`)
  - `type`: Always "invite"
- **Note:** Admin API is unavailable for individual accounts - requires organization setup

### **delete-invite.md**
Documents the DELETE endpoint for removing pending invitations.

- **Endpoint:** `DELETE /v1/organizations/invites/{invite_id}`
- **Purpose:** Delete a pending organization invitation
- **Path Parameters:**
  - `invite_id` (string, required): ID of the invite to delete
- **Headers:** Requires `x-api-key` (Admin API key) and `anthropic-version`
- **Response:** Returns confirmation object with:
  - `id`: ID of the deleted invite
  - `type`: Always "invite_deleted"
- **Use Case:** Cancel invitations that are no longer needed or were sent in error

### **get-invite.md**
Documents the GET endpoint for retrieving a specific invitation by ID.

- **Endpoint:** `GET /v1/organizations/invites/{invite_id}`
- **Purpose:** Retrieve details of a specific organization invitation
- **Path Parameters:**
  - `invite_id` (string, required): ID of the invite to retrieve
- **Headers:** Requires `x-api-key` (Admin API key) and `anthropic-version`
- **Response:** Returns complete invite object with:
  - `id`: Invite identifier
  - `email`: Invitee's email address
  - `invited_at`: Creation timestamp (RFC 3339 format)
  - `expires_at`: Expiration timestamp (RFC 3339 format)
  - `role`: Organization role (`user`, `developer`, `billing`, `admin`, `claude_code_user`)
  - `status`: Current status (`pending`, `accepted`, `expired`, `deleted`)
  - `type`: Always "invite"
- **Use Case:** Check status and details of a specific invitation

### **list-invites.md**
Documents the GET endpoint for retrieving all organization invitations with pagination.

- **Endpoint:** `GET /v1/organizations/invites`
- **Purpose:** List all invitations for the organization
- **Headers:** Requires `x-api-key` (Admin API key) and `anthropic-version`
- **Query Parameters (optional):**
  - `limit` (integer): Number of items per page (default: 20, range: 1-1000)
  - `after_id` (string): Cursor for pagination - returns page after this ID
  - `before_id` (string): Cursor for pagination - returns page before this ID
- **Response:** Returns paginated list with:
  - `data`: Array of invite objects (each containing id, email, role, status, invited_at, expires_at, type)
  - `has_more`: Boolean indicating if more results exist
  - `first_id`: First ID in current page (use as `before_id` for previous page)
  - `last_id`: Last ID in current page (use as `after_id` for next page)
- **Use Case:** View and manage all pending, accepted, expired, and deleted invitations
