# Directory: admin-api

## Overview
This directory contains comprehensive API reference documentation for the Claude Admin API, which enables organization administrators to programmatically manage users, workspaces, API keys, invitations, usage reporting, and Claude Code analytics.

## Files in This Directory
(No files in this directory - all documentation is organized in subdirectories)

## Subdirectories

### **apikeys/**
API endpoints for managing organization API keys, including retrieval, listing with filters, and status updates.
- get-api-key.md: Retrieve details of a specific API key by its ID
- list-api-keys.md: List all API keys with pagination and filtering by status, workspace, or creator
- update-api-key.md: Update an API key's name or status (active, inactive, archived)

### **claude-code/**
API endpoint for retrieving Claude Code usage reports with detailed session and model metrics.
- get-claude-code-usage-report.md: Retrieve Claude Code usage metrics for a specific date, including sessions, commits, PRs, token usage, model breakdown, and tool actions

### **invites/**
API endpoints for managing organization invitations to onboard new users.
- create-invite.md: Create organization invitations with role assignments (user, developer, billing, claude_code_user)
- delete-invite.md: Delete pending invitations before they are accepted
- get-invite.md: Retrieve details and status of a specific invitation by ID
- list-invites.md: List all organization invitations with pagination support

### **organization/**
API endpoint for retrieving current organization information.
- get-me.md: Retrieve the authenticated organization's ID, name, and type using Admin API key

### **usage-cost/**
API endpoints for tracking API usage costs and token consumption across the organization.
- get-cost-report.md: Retrieve cost reports grouped by workspace, model, or other dimensions with time-bucket granularity
- get-messages-usage-report.md: Retrieve detailed token usage statistics for Messages API with filtering by API keys, workspaces, models, and service tiers

### **users/**
API endpoints for managing organization users and their roles.
- get-user.md: Retrieve detailed information about a specific user by ID
- list-users.md: List all organization users with pagination and email filtering
- remove-user.md: Delete a user from the organization
- update-user.md: Update a user's organization role (user, developer, billing, claude_code_user)

### **workspace_members/**
API endpoints for managing workspace membership and role assignments.
- create-workspace-member.md: Add a new member to a workspace with role assignment
- delete-workspace-member.md: Remove a member from a workspace
- get-workspace-member.md: Retrieve a specific workspace member's details and role
- list-workspace-members.md: List all members in a workspace with pagination
- update-workspace-member.md: Modify a workspace member's role (workspace_user, workspace_developer, workspace_admin, workspace_billing)

### **workspaces/**
API endpoints for workspace lifecycle management within the organization.
- archive-workspace.md: Archive a workspace by ID (sets archived_at timestamp)
- create-workspace.md: Create a new workspace with a name (1-40 characters)
- get-workspace.md: Retrieve details of a specific workspace by ID
- list-workspaces.md: List all workspaces with pagination and optional inclusion of archived workspaces
- update-workspace.md: Update a workspace's name
