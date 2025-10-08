url: https://docs.claude.com/en/api/files-list

---

GET

/

v1

/

files

cURL

cURL

Copy
[code]
    curl "https://api.anthropic.com/v1/files" \
         -H "x-api-key: $ANTHROPIC_API_KEY" \
         -H "anthropic-version: 2023-06-01" \
         -H "anthropic-beta: files-api-2025-04-14"
[/code]

200

4XX

Copy
[code]
    {
      "data": [
        {
          "created_at": "2023-11-07T05:31:56Z",
          "downloadable": false,
          "filename": "<string>",
          "id": "<string>",
          "mime_type": "<string>",
          "size_bytes": 1,
          "type": "file"
        }
      ],
      "first_id": "<string>",
      "has_more": false,
      "last_id": "<string>"
    }
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

#### Query Parameters

before\_id

string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

after\_id

string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

limit

integer

default:20

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

Required range: `1 <= x <= 1000`

#### Response

200

application/json

Successful Response

data

FileMetadataSchema · object\[\]

required

List of file metadata objects.

Show child attributes

first\_id

string | null

ID of the first file in this page of results.

has\_more

boolean

default:false

Whether there are more results available.

last\_id

string | null

ID of the last file in this page of results.

Was this page helpful?

YesNo

[Create a File](/en/api/files-create)[Get File Metadata](/en/api/files-metadata)
