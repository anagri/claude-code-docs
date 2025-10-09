---
allowed-tools: Bash(gh:*)
argument-hint: [title] [description]
description: Create GitHub issue and verify creation with retries
---

## Context

- Current repository: !`gh repo view --json nameWithOwner -q .nameWithOwner`

## Your task

Create a GitHub issue and verify it was created successfully:

1. **Create the issue:**
   ```bash
   gh issue create --title "$1" --body "$2"
   ```

2. **Capture the issue number** from the output

3. **Verify with up to 5 retries:**
   - Wait 2 seconds between each retry
   - Use either:
     - `gh issue view <issue-number>` OR
     - `gh api repos/<repo>/issues/<issue-number>`
   - Stop when verification succeeds

4. **Report result:**
   - Success: Issue number and URL
   - Failure: Error message after 5 failed retries
