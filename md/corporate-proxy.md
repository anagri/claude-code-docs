url: https://docs.anthropic.com/en/docs/claude-code/corporate-proxy

---

Claude Code supports standard HTTP/HTTPS proxy configurations through environment variables. This allows you to route all Claude Code traffic through your organization’s proxy servers for security, compliance, and monitoring purposes.

## Basic proxy configuration

### Environment variables

Claude Code respects standard proxy environment variables:
[code]
    # HTTPS proxy (recommended)
    export HTTPS_PROXY=https://proxy.example.com:8080

    # HTTP proxy (if HTTPS not available)
    export HTTP_PROXY=http://proxy.example.com:8080

    # Bypass proxy for specific requests - space-separated format
    export NO_PROXY="localhost 192.168.1.1 example.com .example.com"
    # Bypass proxy for specific requests - comma-separated format
    export NO_PROXY="localhost,192.168.1.1,example.com,.example.com"
    # Bypass proxy for all requests
    export NO_PROXY="*"

[/code]

Claude Code does not support SOCKS proxies.

## Authentication

### Basic authentication

If your proxy requires basic authentication, include credentials in the proxy URL:
[code]
    export HTTPS_PROXY=http://username:password@proxy.example.com:8080

[/code]

Avoid hardcoding passwords in scripts. Use environment variables or secure credential storage instead.

For proxies requiring advanced authentication \(NTLM, Kerberos, etc.\), consider using an LLM Gateway service that supports your authentication method.

### SSL certificate issues

If your proxy uses custom SSL certificates, you may encounter certificate errors.

Ensure that you set the correct certificate bundle path:
[code]
    export SSL_CERT_FILE=/path/to/certificate-bundle.crt
    export NODE_EXTRA_CA_CERTS=/path/to/certificate-bundle.crt

[/code]

## Network access requirements

Claude Code requires access to the following URLs:

  * `api.anthropic.com` \- Claude API endpoints
  * `statsig.anthropic.com` \- Telemetry and metrics
  * `sentry.io` \- Error reporting

Ensure these URLs are allowlisted in your proxy configuration and firewall rules. This is especially important when using Claude Code in containerized or restricted network environments.

## Additional resources

  * [Claude Code settings](/en/docs/claude-code/settings)
  * [Environment variables reference](/en/docs/claude-code/settings#environment-variables)
  * [Troubleshooting guide](/en/docs/claude-code/troubleshooting)

Was this page helpful?

YesNo

[Google Vertex AI](/en/docs/claude-code/google-vertex-ai)[LLM gateway](/en/docs/claude-code/llm-gateway)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
