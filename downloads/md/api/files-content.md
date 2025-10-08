url: https://docs.claude.com/en/api/files-content

---

GET

/

v1

/

files

/

\{file\_id\}

/

content

cURL

cURL

Copy
[code]
    curl "https://api.anthropic.com/v1/files/file_011CNha8iCJcU1wXNR6q4V8w/content" \
         -H "x-api-key: $ANTHROPIC_API_KEY" \
         -H "anthropic-version: 2023-06-01" \
         -H "anthropic-beta: files-api-2025-04-14" \
         --output downloaded_file.pdf
[/code]

200

4XX

Copy
[code]
    "<string>"
[/code]

The Files API allows you to upload and manage files to use with the Claude API without having to re-upload content with each request. For more information about the Files API, see the [developer guide for files](/en/docs/build-with-claude/files).

The Files API is currently in beta. To use the Files API, you’ll need to include the beta feature header: `anthropic-beta: files-api-2025-04-14`.Please reach out through our [feedback form](https://forms.gle/tisHyierGwgN4DUE9) to share your experience with the Files API.

#### Headers

anthropic-beta

string\[\]

Optional header to specify the beta version\(s\) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

anthropic-version

string

required

The version of the Claude API you want to use.

Read more about versioning and our version history [here](/api/versioning).

x-api-key

string

required

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a Workspace.

#### Path Parameters

file\_id

string

required

ID of the File.

#### Response

200

application/octet-stream

Successful Response

The response is of type `string`.

Was this page helpful?

YesNo

[Get File Metadata](/en/api/files-metadata)[Delete a File](/en/api/files-delete)
