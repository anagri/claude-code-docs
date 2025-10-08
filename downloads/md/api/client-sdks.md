url: https://docs.claude.com/en/api/client-sdks

---

> Additional configuration is needed to use Anthropic’s Client SDKs through a partner platform. If you are using Amazon Bedrock, see [this guide](/en/api/claude-on-amazon-bedrock); if you are using Google Cloud Vertex AI, see [this guide](/en/api/claude-on-vertex-ai).

## Python

[Python library GitHub repo](https://github.com/anthropics/anthropic-sdk-python) Example:

Python

Copy
[code]
    import anthropic

    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key="my_api_key",
    )
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hello, Claude"}
        ]
    )
    print(message.content)

[/code]

Accepted `model` strings:

Copy
[code]
    # Claude 4 Models
    "claude-opus-4-1-20250805"
    "claude-opus-4-1"  # alias
    "claude-opus-4-20250514"
    "claude-opus-4-0"  # alias
    "claude-sonnet-4-5-20250929"
    "claude-sonnet-4-5"  # alias
    "claude-sonnet-4-20250514"
    "claude-sonnet-4-0"  # alias

    # Claude 3.7 Models
    "claude-3-7-sonnet-20250219"
    "claude-3-7-sonnet-latest"  # alias

    # Claude 3.5 Models
    "claude-3-5-haiku-20241022"
    "claude-3-5-haiku-latest"  # alias
    "claude-3-5-sonnet-20241022"  # deprecated
    "claude-3-5-sonnet-latest"  # alias
    "claude-3-5-sonnet-20240620"  # deprecated, previous version

    # Claude 3 Models
    "claude-3-opus-20240229"  # deprecated
    "claude-3-opus-latest"  # alias
    "claude-3-haiku-20240307"

[/code]

* * *

## TypeScript

[TypeScript library GitHub repo](https://github.com/anthropics/anthropic-sdk-typescript)

While this library is in TypeScript, it can also be used in JavaScript libraries.

Example:

TypeScript

Copy
[code]
    import Anthropic from '@anthropic-ai/sdk';

    const anthropic = new Anthropic({
      apiKey: 'my_api_key', // defaults to process.env["ANTHROPIC_API_KEY"]
    });

    const msg = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1024,
      messages: [{ role: "user", content: "Hello, Claude" }],
    });
    console.log(msg);

[/code]

Accepted `model` strings:

Copy
[code]
    // Claude 4 Models
    "claude-opus-4-1-20250805"
    "claude-opus-4-1"  // alias
    "claude-opus-4-20250514"
    "claude-opus-4-0"  // alias
    "claude-sonnet-4-5-20250929"
    "claude-sonnet-4-5"  // alias
    "claude-sonnet-4-20250514"
    "claude-sonnet-4-0"  // alias

    // Claude 3.7 Models
    "claude-3-7-sonnet-20250219"
    "claude-3-7-sonnet-latest"  // alias

    // Claude 3.5 Models
    "claude-3-5-haiku-20241022"
    "claude-3-5-haiku-latest"  // alias
    "claude-3-5-sonnet-20241022"  // deprecated
    "claude-3-5-sonnet-latest"  // alias
    "claude-3-5-sonnet-20240620"  // deprecated, previous version

    // Claude 3 Models
    "claude-3-opus-20240229"  // deprecated
    "claude-3-opus-latest"  // alias
    "claude-3-haiku-20240307"

[/code]

* * *

## Java

[Java library GitHub repo](https://github.com/anthropics/anthropic-sdk-java) Example:

Java

Copy
[code]
    import com.anthropic.models.Message;
    import com.anthropic.models.MessageCreateParams;
    import com.anthropic.models.Model;

    MessageCreateParams params = MessageCreateParams.builder()
        .maxTokens(1024L)
        .addUserMessage("Hello, Claude")
        .model(Model.CLAUDE_SONNET_4_0)
        .build();
    Message message = client.messages().create(params);

[/code]

`model` enum values:

Copy
[code]
    // Claude 4 Models
    Model.CLAUDE_OPUS_4_1
    Model.CLAUDE_OPUS_4_1_20250805
    Model.CLAUDE_OPUS_4_0
    Model.CLAUDE_OPUS_4_20250514
    Model.CLAUDE_SONNET_4_5_20250929
    Model.CLAUDE_SONNET_4_5
    Model.CLAUDE_SONNET_4_20250514
    Model.CLAUDE_SONNET_4_0

    // Claude 3.7 Models
    Model.CLAUDE_3_7_SONNET_LATEST
    Model.CLAUDE_3_7_SONNET_20250219

    // Claude 3.5 Models
    Model.CLAUDE_3_5_HAIKU_LATEST
    Model.CLAUDE_3_5_HAIKU_20241022
    Model.CLAUDE_3_5_SONNET_LATEST
    Model.CLAUDE_3_5_SONNET_20241022  // deprecated
    Model.CLAUDE_3_5_SONNET_20240620  // deprecated

    // Claude 3 Models
    Model.CLAUDE_3_OPUS_LATEST
    Model.CLAUDE_3_OPUS_20240229  // deprecated
    Model.CLAUDE_3_HAIKU_20240307

[/code]

* * *

## Go

[Go library GitHub repo](https://github.com/anthropics/anthropic-sdk-go) Example:

Go

Copy
[code]
    package main

    import (
    	"context"
    	"fmt"
    	"github.com/anthropics/anthropic-sdk-go/option"

    	"github.com/anthropics/anthropic-sdk-go"
    )

    func main() {
    	client := anthropic.NewClient(
    		option.WithAPIKey("my-anthropic-api-key"),
    	)

    	message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
    		Model:     anthropic.ModelClaudeSonnet4_0,
    		MaxTokens: 1024,
    		Messages: []anthropic.MessageParam{
    			anthropic.NewUserMessage(anthropic.NewTextBlock("What is a quaternion?")),
    		},
    	})
    	if err != nil {
    		fmt.Printf("Error creating message: %v\n", err)
    		return
    	}

    	fmt.Printf("%+v\n", message.Content)
    }

[/code]

`Model` constants:

Copy
[code]
    // Claude 4 Models
    anthropic.ModelClaudeOpus4_1
    anthropic.ModelClaudeOpus4_1_20250805
    anthropic.ModelClaudeOpus4_0
    anthropic.ModelClaudeOpus4_20250514
    anthropic.ModelClaudeSonnet4_5_20250929
    anthropic.ModelClaudeSonnet4_5
    anthropic.ModelClaudeSonnet4_20250514
    anthropic.ModelClaudeSonnet4_0

    // Claude 3.7 Models
    anthropic.ModelClaude3_7SonnetLatest
    anthropic.ModelClaude3_7Sonnet20250219

    // Claude 3.5 Models
    anthropic.ModelClaude3_5HaikuLatest
    anthropic.ModelClaude3_5Haiku20241022
    anthropic.ModelClaude3_5SonnetLatest
    anthropic.ModelClaude3_5Sonnet20241022  // deprecated
    anthropic.ModelClaude_3_5_Sonnet_20240620  // deprecated

    // Claude 3 Models
    anthropic.ModelClaude3OpusLatest
    anthropic.ModelClaude_3_Opus_20240229  // deprecated
    anthropic.ModelClaude_3_Haiku_20240307

[/code]

* * *

## C\#

[C\# library GitHub repo](https://github.com/anthropics/anthropic-sdk-csharp)

The C\# SDK is currently in beta.

Example:

C\#

Copy
[code]
    using System;
    using Anthropic;
    using Anthropic.Models.Messages;
    using Anthropic.Models.Messages.MessageParamProperties;

    // Uses ANTHROPIC_API_KEY environment variable by default
    AnthropicClient client = new();

    MessageCreateParams parameters = new()
    {
        MaxTokens = 1024,
        Messages =
        [
            new()
            {
                Role = Role.User,
                Content = "Hello, Claude",
            },
        ],
        Model = Model.ClaudeSonnet4_0,
    };

    var message = await client.Messages.Create(parameters);

    Console.WriteLine(message);

[/code]

`Model` values:

Copy
[code]
    // Claude 4 Models
    Model.ClaudeOpus4_1_20250805
    Model.ClaudeOpus4_0  // alias
    Model.ClaudeOpus4_20250514
    Model.Claude4Opus20250514  // alias
    Model.ClaudeSonnet4_5_20250929
    Model.ClaudeSonnet4_5  // alias
    Model.ClaudeSonnet4_20250514
    Model.ClaudeSonnet4_0  // alias
    Model.Claude4Sonnet20250514  // alias

    // Claude 3.7 Models
    Model.Claude3_7SonnetLatest  // alias
    Model.Claude3_7Sonnet20250219

    // Claude 3.5 Models
    Model.Claude3_5HaikuLatest  // alias
    Model.Claude3_5Haiku20241022
    Model.Claude3_5SonnetLatest  // alias
    Model.Claude3_5Sonnet20241022  // deprecated
    Model.Claude_3_5_Sonnet_20240620  // deprecated

    // Claude 3 Models
    Model.Claude3OpusLatest  // alias
    Model.Claude_3_Opus_20240229  // deprecated
    Model.Claude_3_Haiku_20240307

[/code]

* * *

## Ruby

[Ruby library GitHub repo](https://github.com/anthropics/anthropic-sdk-ruby) Example:

ruby

Copy
[code]
    require "bundler/setup"
    require "anthropic"

    anthropic = Anthropic::Client.new(
      api_key: "my_api_key" # defaults to ENV["ANTHROPIC_API_KEY"]
    )

    message =
      anthropic.messages.create(
        max_tokens: 1024,
        messages: [{
          role: "user",
          content: "Hello, Claude"
        }],
        model: "claude-sonnet-4-5"
      )

    puts(message.content)

[/code]

Accepted `model` strings:

Copy
[code]
    # Claude 4 Models
    :"claude-opus-4-1-20250805"
    :"claude-opus-4-1"  # alias
    :"claude-opus-4-20250514"
    :"claude-opus-4-0"  # alias
    :"claude-sonnet-4-5-20250929"
    :"claude-sonnet-4-5"  # alias
    :"claude-sonnet-4-20250514"
    :"claude-sonnet-4-0"  # alias

    # Claude 3.7 Models
    :"claude-3-7-sonnet-20250219"
    :"claude-3-7-sonnet-latest"  # alias

    # Claude 3.5 Models
    :"claude-3-5-haiku-20241022"
    :"claude-3-5-haiku-latest"  # alias
    :"claude-3-5-sonnet-20241022"  # deprecated
    :"claude-3-5-sonnet-latest"  # alias
    :"claude-3-5-sonnet-20240620"  # deprecated, previous version

    # Claude 3 Models
    :"claude-3-opus-20240229"  # deprecated
    :"claude-3-opus-latest"  # alias
    :"claude-3-haiku-20240307"

[/code]

* * *

## PHP

[PHP library GitHub repo](https://github.com/anthropics/anthropic-sdk-php)

The PHP SDK is currently in beta.

Example:

PHP

Copy
[code]
    <?php

    use Anthropic\Client;
    use Anthropic\Messages\MessageParam;

    $client = new Client(
      apiKey: getenv("ANTHROPIC_API_KEY") ?: "my-anthropic-api-key"
    );

    $message = $client->messages->create(
      maxTokens: 1024,
      messages: [MessageParam::with(role: "user", content: "Hello, Claude")],
      model: "claude-sonnet-4-5",
    );
    var_dump($message->content);

[/code]

Accepted `model` strings:

Copy
[code]
    // Claude 4 Models
    "claude-opus-4-1-20250805"
    "claude-opus-4-1"  // alias
    "claude-opus-4-20250514"
    "claude-opus-4-0"  // alias
    "claude-sonnet-4-5-20250929"
    "claude-sonnet-4-5"  // alias
    "claude-sonnet-4-20250514"
    "claude-sonnet-4-0"  // alias

    // Claude 3.7 Models
    "claude-3-7-sonnet-20250219"
    "claude-3-7-sonnet-latest"  // alias

    // Claude 3.5 Models
    "claude-3-5-haiku-20241022"
    "claude-3-5-haiku-latest"  // alias
    "claude-3-5-sonnet-20241022"  // deprecated
    "claude-3-5-sonnet-latest"  // alias
    "claude-3-5-sonnet-20240620"  // deprecated, previous version

    // Claude 3 Models
    "claude-3-opus-20240229"  // deprecated
    "claude-3-opus-latest"  // alias
    "claude-3-haiku-20240307"

[/code]

`Model` constants:

Copy
[code]
    // Claude 4 Models
    Model::CLAUDE_OPUS_4_1_20250805
    Model::CLAUDE_OPUS_4_0  // alias
    Model::CLAUDE_OPUS_4_20250514
    Model::CLAUDE_SONNET_4_5_20250929
    Model::CLAUDE_SONNET_4_5  // alias
    Model::CLAUDE_SONNET_4_20250514
    Model::CLAUDE_SONNET_4_0  // alias

    // Claude 3.7 Models
    Model::CLAUDE_3_7_SONNET_LATEST  // alias
    Model::CLAUDE_3_7_SONNET_20250219

    // Claude 3.5 Models
    Model::CLAUDE_3_5_HAIKU_LATEST  // alias
    Model::CLAUDE_3_5_HAIKU_20241022
    Model::CLAUDE_3_5_SONNET_LATEST  // alias
    Model::CLAUDE_3_5_SONNET_20241022  // deprecated
    Model::CLAUDE_3_5_SONNET_20240620  // deprecated, previous version

    // Claude 3 Models
    Model::CLAUDE_3_OPUS_LATEST  // alias
    Model::CLAUDE_3_OPUS_20240229  // deprecated
    Model::CLAUDE_3_HAIKU_20240307

[/code]

* * *

## Beta namespace in client SDKs

Every SDK has a `beta` namespace that is available. This is used for new features Anthropic releases in a beta version. Use this in conjunction with [beta headers](/en/api/beta-headers) to use these features.

Python

TypeScript

Java

Go

Ruby

PHP

C\#

Copy
[code]
    import anthropic

    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key="my_api_key",
    )
    message = client.beta.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hello, Claude"}
        ],
        betas=["beta-feature-name"]
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Migrating from Text Completions](/en/api/migrating-from-text-completions-to-messages)[OpenAI SDK compatibility](/en/api/openai-sdk)
