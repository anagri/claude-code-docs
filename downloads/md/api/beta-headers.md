url: https://docs.claude.com/en/api/beta-headers

---

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API. These features are subject to change and may be modified or removed in future releases.

Beta headers are often used in conjunction with the [beta namespace in the client SDKs](/en/api/client-sdks#beta-namespace-in-client-sdks)

## How to use beta headers

To access beta features, include the `anthropic-beta` header in your API requests:

Copy
[code]
    POST /v1/messages
    Content-Type: application/json
    X-API-Key: YOUR_API_KEY
    anthropic-beta: BETA_FEATURE_NAME

[/code]

When using the SDK, you can specify beta headers in the request options:

Python

TypeScript

cURL

Copy
[code]
    from anthropic import Anthropic

    client = Anthropic()

    response = client.beta.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hello, Claude"}
        ],
        betas=["beta-feature-name"]
    )

[/code]

Beta features are experimental and may:

  * Have breaking changes without notice
  * Be deprecated or removed
  * Have different rate limits or pricing
  * Not be available in all regions

### Multiple beta features

To use multiple beta features in a single request, include all feature names in the header separated by commas:

Copy
[code]
    anthropic-beta: feature1,feature2,feature3

[/code]

### Version naming conventions

Beta feature names typically follow the pattern: `feature-name-YYYY-MM-DD`, where the date indicates when the beta version was released. Always use the exact beta feature name as documented.

## Error handling

If you use an invalid or unavailable beta header, you’ll receive an error response:

Copy
[code]
    {
      "type": "error",
      "error": {
        "type": "invalid_request_error",
        "message": "Unsupported beta header: invalid-beta-name"
      }
    }

[/code]

## Getting help

For questions about beta features:

  1. Check the documentation for the specific feature
  2. Review the [API changelog](/en/api/versioning) for updates
  3. Contact support for assistance with production usage

Remember that beta features are provided “as-is” and may not have the same SLA guarantees as stable API features.

Was this page helpful?

YesNo

[Handling stop reasons](/en/api/handling-stop-reasons)[Messages](/en/api/messages)
