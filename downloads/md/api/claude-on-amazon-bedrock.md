url: https://docs.claude.com/en/api/claude-on-amazon-bedrock

---

Calling Claude through Bedrock slightly differs from how you would call Claude when using Anthropic’s client SDK’s. This guide will walk you through the process of completing an API call to Claude on Bedrock in either Python or TypeScript. Note that this guide assumes you have already signed up for an [AWS account](https://portal.aws.amazon.com/billing/signup) and configured programmatic access.

## Install and configure the AWS CLI

  1. [Install a version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) at or newer than version `2.13.23`
  2. Configure your AWS credentials using the AWS configure command \(see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)\) or find your credentials by navigating to “Command line or programmatic access” within your AWS dashboard and following the directions in the popup modal.
  3. Verify that your credentials are working:

Shell

Copy
[code]
    aws sts get-caller-identity

[/code]

## Install an SDK for accessing Bedrock

Anthropic’s [client SDKs](/en/api/client-sdks) support Bedrock. You can also use an AWS SDK like `boto3` directly.

Python

TypeScript

Boto3 \(Python\)

Copy
[code]
    pip install -U "anthropic[bedrock]"

[/code]

## Accessing Bedrock

### Subscribe to Anthropic models

Go to the [AWS Console > Bedrock > Model Access](https://console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess) and request access to Anthropic models. Note that Anthropic model availability varies by region. See [AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) for latest information.

#### API model IDs

Model| Base Bedrock model ID| `global`| `us`| `eu`| `jp`| `apac`
---|---|---|---|---|---|---
Claude Sonnet 4.5| anthropic.claude-sonnet-4-5-20250929-v1:0| Yes| Yes| Yes| Yes| No
Claude Sonnet 4| anthropic.claude-sonnet-4-20250514-v1:0| Yes| Yes| Yes| No| Yes
Claude Sonnet 3.7| anthropic.claude-3-7-sonnet-20250219-v1:0| No| Yes| Yes| No| Yes
Claude Sonnet 3.5 ⚠️| anthropic.claude-3-5-sonnet-20241022-v2:0| No| Yes| No| No| Yes
Claude Opus 4.1| anthropic.claude-opus-4-1-20250805-v1:0| No| Yes| No| No| No
Claude Opus 4| anthropic.claude-opus-4-20250514-v1:0| No| Yes| No| No| No
Claude Opus 3 ⚠️| anthropic.claude-3-opus-20240229-v1:0| No| Yes| No| No| No
Claude Haiku 3.5| anthropic.claude-3-5-haiku-20241022-v1:0| No| Yes| No| No| No
Claude Haiku 3| anthropic.claude-3-haiku-20240307-v1:0| No| Yes| Yes| No| Yes
For more information about regional vs global model IDs, see the Global vs regional endpoints section below.

### List available models

The following examples show how to print a list of all the Claude models available through Bedrock:

AWS CLI

Boto3 \(Python\)

Copy
[code]
    aws bedrock list-foundation-models --region=us-west-2 --by-provider anthropic --query "modelSummaries[*].modelId"

[/code]

### Making requests

The following examples show how to generate text from Claude on Bedrock:

Python

TypeScript

Boto3 \(Python\)

Copy
[code]
    from anthropic import AnthropicBedrock

    client = AnthropicBedrock(
        # Authenticate by either providing the keys below or use the default AWS credential providers, such as
        # using ~/.aws/credentials or the "AWS_SECRET_ACCESS_KEY" and "AWS_ACCESS_KEY_ID" environment variables.
        aws_access_key="<access key>",
        aws_secret_key="<secret key>",
        # Temporary credentials can be used with aws_session_token.
        # Read more at https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html.
        aws_session_token="<session_token>",
        # aws_region changes the aws region to which the request is made. By default, we read AWS_REGION,
        # and if that's not present, we default to us-east-1. Note that we do not read ~/.aws/config for the region.
        aws_region="us-west-2",
    )

    message = client.messages.create(
        model="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
        max_tokens=256,
        messages=[{"role": "user", "content": "Hello, world"}]
    )
    print(message.content)

[/code]

See our [client SDKs](/en/api/client-sdks) for more details, and the official Bedrock docs [here](https://docs.aws.amazon.com/bedrock/).

## Activity logging

Bedrock provides an [invocation logging service](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) that allows customers to log the prompts and completions associated with your usage. Anthropic recommends that you log your activity on at least a 30-day rolling basis in order to understand your activity and investigate any potential misuse.

Turning on this service does not give AWS or Anthropic any access to your content.

## Feature support

You can find all the features currently supported on Bedrock [here](/en/docs/build-with-claude/overview).

### PDF Support on Bedrock

PDF support is available on Amazon Bedrock through both the Converse API and InvokeModel API. For detailed information about PDF processing capabilities and limitations, see the [PDF support documentation](/en/docs/build-with-claude/pdf-support#amazon-bedrock-pdf-support). **Important considerations for Converse API users:**

  * Visual PDF analysis \(charts, images, layouts\) requires citations to be enabled
  * Without citations, only basic text extraction is available
  * For full control without forced citations, use the InvokeModel API

For more details on the two document processing modes and their limitations, refer to the [PDF support guide](/en/docs/build-with-claude/pdf-support#amazon-bedrock-pdf-support).

### 1M token context window

Claude Sonnet 4 and 4.5 support the [1M token context window](/en/docs/build-with-claude/context-windows#1m-token-context-window) on Amazon Bedrock.

The 1M token context window is currently in beta. To use the extended context window, include the `context-1m-2025-08-07` beta header in your [Bedrock API requests](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-request-response.html).

## Global vs regional endpoints

Starting with **Claude Sonnet 4.5 and all future models** , Amazon Bedrock offers two endpoint types:

  * **Global endpoints** : Dynamic routing for maximum availability
  * **Regional endpoints** : Guaranteed data routing through specific geographic regions

Regional endpoints include a 10% pricing premium over global endpoints.

This applies to Claude Sonnet 4.5 and future models only. Older models \(Claude Sonnet 4, Opus 4, and earlier\) maintain their existing pricing structures.

### When to use each option

**Global endpoints \(recommended\):**

  * Provide maximum availability and uptime
  * Dynamically route requests to regions with available capacity
  * No pricing premium
  * Best for applications where data residency is flexible

**Regional endpoints \(CRIS\):**

  * Route traffic through specific geographic regions
  * Required for data residency and compliance requirements
  * Available for US, EU, Japan, and Australia
  * 10% pricing premium reflects infrastructure costs for dedicated regional capacity

### Implementation

**Using global endpoints \(default for Sonnet 4.5 and 4\):** The model IDs for Claude Sonnet 4.5 and 4 already include the `global.` prefix:

Python

TypeScript

Copy
[code]
    from anthropic import AnthropicBedrock

    client = AnthropicBedrock(aws_region="us-west-2")

    message = client.messages.create(
        model="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
        max_tokens=256,
        messages=[{"role": "user", "content": "Hello, world"}]
    )

[/code]

**Using regional endpoints \(CRIS\):** To use regional endpoints, remove the `global.` prefix from the model ID:

Python

TypeScript

Copy
[code]
    from anthropic import AnthropicBedrock

    client = AnthropicBedrock(aws_region="us-west-2")

    # Using US regional endpoint (CRIS)
    message = client.messages.create(
        model="anthropic.claude-sonnet-4-5-20250929-v1:0",  # No global. prefix
        max_tokens=256,
        messages=[{"role": "user", "content": "Hello, world"}]
    )

[/code]

### Additional resources

  * **AWS Bedrock pricing:** [aws.amazon.com/bedrock/pricing](https://aws.amazon.com/bedrock/pricing/)
  * **AWS pricing documentation:** [Bedrock pricing guide](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-pricing.html)
  * **AWS blog post:** [Introducing Claude Sonnet 4.5 in Amazon Bedrock](https://aws.amazon.com/blogs/aws/introducing-claude-sonnet-4-5-in-amazon-bedrock-anthropics-most-intelligent-model-best-for-coding-and-complex-agents/)
  * **Anthropic pricing details:** [Pricing documentation](/en/docs/about-claude/pricing#third-party-platform-pricing)

Was this page helpful?

YesNo

[Message Batches examples](/en/api/messages-batch-examples)[Vertex AI API](/en/api/claude-on-vertex-ai)
