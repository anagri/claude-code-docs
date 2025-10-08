url: https://docs.claude.com/en/docs/agents-and-tools/remote-mcp-servers

---

Several companies have deployed remote MCP servers that developers can connect to via the Anthropic MCP connector API. These servers expand the capabilities available to developers and end users by providing remote access to various services and tools through the MCP protocol.

The remote MCP servers listed below are third-party services designed to work with the Claude API. These servers are not owned, operated, or endorsed by Anthropic. Users should only connect to remote MCP servers they trust and should review each server’s security practices and terms before connecting.

## Connecting to remote MCP servers

To connect to a remote MCP server:

  1. Review the documentation for the specific server you want to use.
  2. Ensure you have the necessary authentication credentials.
  3. Follow the server-specific connection instructions provided by each company.

For more information about using remote MCP servers with the Claude API, see the [MCP connector docs](/en/docs/agents-and-tools/mcp-connector).

## Remote MCP server examples

### Development & Testing Tools

[**Hugging Face**](https://huggingface.co/settings/mcp)

Provides access to Hugging Face Hub information and Gradio AI ApplicationsURL

`https://huggingface.co/mcp`

[**Jam**](https://jam.dev/docs/debug-a-jam/mcp)

Debug faster with AI agents that can access Jam recordings like video, console logs, network requests, and errorsURL

`https://mcp.jam.dev/mcp`

### Project Management & Documentation

[**Asana**](https://developers.asana.com/docs/using-asanas-model-control-protocol-mcp-server)

Interact with your Asana workspace to keep projects on trackURL

`https://mcp.asana.com/sse`

[**Atlassian**](https://www.atlassian.com/platform/remote-mcp-server)

Manage your Jira tickets and Confluence docsURL

`https://mcp.atlassian.com/v1/sse`

[**Intercom**](https://developers.intercom.com/docs/guides/mcp)

Access real-time customer conversations, tickets, and user dataURL

`https://mcp.intercom.com/mcp`

[**Linear**](https://linear.app/docs/mcp)

Integrate with Linear's issue tracking and project managementURL

`https://mcp.linear.app/sse`

[**Box**](https://box.dev/guides/box-mcp/remote/)

Ask questions about your enterprise content, get insights from unstructured data, automate content workflowsURL

`https://mcp.box.com/`

[**Fireflies**](https://guide.fireflies.ai/articles/8272956938-learn-about-the-fireflies-mcp-server-model-context-protocol)

Extract valuable insights from meeting transcripts and summariesURL

`https://api.fireflies.ai/mcp`

[**Monday**](https://developer.monday.com/apps/docs/mondaycom-mcp-integration)

Manage monday.com boards by creating items, updating columns, assigning owners, setting timelines, adding CRM activities, and writing summariesURL

`https://mcp.monday.com/sse`

### Databases & Data Management

[**Daloopa**](https://docs.daloopa.com/docs/daloopa-mcp)

Supplies high quality fundamental financial data sourced from SEC Filings, investor presentationsURL

`https://mcp.daloopa.com/server/mcp`

[**HubSpot**](https://developers.hubspot.com/mcp)

Access and manage HubSpot CRM data by fetching contacts, companies, and deals, and creating and updating recordsURL

`https://mcp.hubspot.com/anthropic`

### Payments & Commerce

[**PayPal**](https://www.paypal.ai/)

Integrate PayPal commerce capabilities, payment processing, transaction managementURL

`https://mcp.paypal.com/mcp`

[**Plaid**](https://plaid.com/blog/plaid-mcp-ai-assistant-claude/)

Analyze, troubleshoot, and optimize Plaid integrations. Banking data, financial account linkingURL

`https://api.dashboard.plaid.com/mcp/sse`

[**Square**](https://developer.squareup.com/docs/mcp)

Use an agent to build on Square APIs. Payments, inventory, orders, and moreURL

`https://mcp.squareup.com/sse`

[**Stripe**](https://docs.stripe.com/mcp)

Payment processing, subscription management, and financial transactionsURL

`https://mcp.stripe.com`

### Design & Media

[**Cloudinary**](https://cloudinary.com/documentation/cloudinary_llm_mcp#mcp_servers)

Upload, manage, transform, and analyze your media assetsMultiple services available. See documentation for specific server URLs.

[**invideo**](https://invideo.io/ai/mcp)

Build video creation capabilities into your applicationsURL

`https://mcp.invideo.io/sse`

[**Canva**](https://www.canva.dev/docs/connect/canva-mcp-server-setup/)

Browse, summarize, autofill, and even generate new Canva designs directly from ClaudeURL

`https://mcp.canva.com/mcp`

### Infrastructure & DevOps

[**Cloudflare**](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/)

Build applications, analyze traffic, monitor performance, and manage security settings through CloudflareMultiple services available. See documentation for specific server URLs. Claude Code can use the Cloudflare CLI if installed.

[**Netlify**](https://docs.netlify.com/build/build-with-ai/netlify-mcp-server/)

Create, deploy, and manage websites on Netlify. Control all aspects of your site from creating secrets to enforcing access controls to aggregating form submissionsURL

`https://netlify-mcp.netlify.app/mcp`

[**Stytch**](https://stytch.com/docs/workspace-management/stytch-mcp)

Configure and manage Stytch authentication services, redirect URLs, email templates, and workspace settingsURL

`http://mcp.stytch.dev/mcp`

[**Vercel**](https://vercel.com/docs/mcp/vercel-mcp)

Vercel's official MCP server, allowing you to search and navigate documentation, manage projects and deployments, and analyze deployment logs—all in one placeURL

`https://mcp.vercel.com/`

### Automation & Integration

[**Workato**](https://docs.workato.com/mcp.html)

Access any application, workflows or data via Workato, made accessible for AIMCP servers are programmatically generated

[**Zapier**](https://help.zapier.com/hc/en-us/articles/36265392843917)

Connect to nearly 8,000 apps through Zapier's automation platformGenerate a user-specific URL at mcp.zapier.com

**Looking for more?** [Find hundreds more MCP servers on GitHub](https://github.com/modelcontextprotocol/servers).

Was this page helpful?

YesNo

[MCP connector](/en/docs/agents-and-tools/mcp-connector)[Overview](/en/docs/about-claude/use-case-guides/overview)
