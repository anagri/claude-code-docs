url: https://docs.claude.com/en/docs/agents-and-tools/tool-use/bash-tool

---

The bash tool enables Claude to execute shell commands in a persistent bash session, allowing system operations, script execution, and command-line automation.

## Overview

The bash tool provides Claude with:

  * Persistent bash session that maintains state
  * Ability to run any shell command
  * Access to environment variables and working directory
  * Command chaining and scripting capabilities

## Model compatibility

Model| Tool Version
---|---
Claude 4 models and Sonnet 3.7| `bash_20250124`
Claude Sonnet 3.5 \([deprecated](/en/docs/about-claude/model-deprecations)\)| `bash_20241022`

Claude Sonnet 3.5 \([deprecated](/en/docs/about-claude/model-deprecations)\) requires the `computer-use-2024-10-22` beta header when using the bash tool.The bash tool is generally available in Claude 4 models and Sonnet 3.7.

Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.

## Use cases

  * **Development workflows** : Run build commands, tests, and development tools
  * **System automation** : Execute scripts, manage files, automate tasks
  * **Data processing** : Process files, run analysis scripts, manage datasets
  * **Environment setup** : Install packages, configure environments

## Quick start

Python

Shell

Copy
[code]
    import anthropic

    client = anthropic.Anthropic()

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        tools=[
            {
                "type": "bash_20250124",
                "name": "bash"
            }
        ],
        messages=[
            {"role": "user", "content": "List all Python files in the current directory."}
        ]
    )

[/code]

## How it works

The bash tool maintains a persistent session:

  1. Claude determines what command to run
  2. You execute the command in a bash shell
  3. Return the output \(stdout and stderr\) to Claude
  4. Session state persists between commands \(environment variables, working directory\)

## Parameters

Parameter| Required| Description
---|---|---
`command`| Yes\*| The bash command to run
`restart`| No| Set to `true` to restart the bash session
\*Required unless using `restart`

Example usage

Copy
[code]
    // Run a command
    {
      "command": "ls -la *.py"
    }

    // Restart the session
    {
      "restart": true
    }

[/code]

## Example: Multi-step automation

Claude can chain commands to complete complex tasks:

Copy
[code]
    # User request
    "Install the requests library and create a simple Python script that fetches a joke from an API, then run it."

    # Claude's tool uses:
    # 1. Install package
    {"command": "pip install requests"}

    # 2. Create script
    {"command": "cat > fetch_joke.py << 'EOF'\nimport requests\nresponse = requests.get('https://official-joke-api.appspot.com/random_joke')\njoke = response.json()\nprint(f\"Setup: {joke['setup']}\")\nprint(f\"Punchline: {joke['punchline']}\")\nEOF"}

    # 3. Run script
    {"command": "python fetch_joke.py"}

[/code]

The session maintains state between commands, so files created in step 2 are available in step 3.

* * *

## Implement the bash tool

The bash tool is implemented as a schema-less tool. When using this tool, you don’t need to provide an input schema as with other tools; the schema is built into Claude’s model and can’t be modified.

1

Set up a bash environment

Create a persistent bash session that Claude can interact with:

Copy
[code]
    import subprocess
    import threading
    import queue

    class BashSession:
        def __init__(self):
            self.process = subprocess.Popen(
                ['/bin/bash'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=0
            )
            self.output_queue = queue.Queue()
            self.error_queue = queue.Queue()
            self._start_readers()

[/code]

2

Handle command execution

Create a function to execute commands and capture output:

Copy
[code]
    def execute_command(self, command):
        # Send command to bash
        self.process.stdin.write(command + '\n')
        self.process.stdin.flush()

        # Capture output with timeout
        output = self._read_output(timeout=10)
        return output

[/code]

3

Process Claude's tool calls

Extract and execute commands from Claude’s responses:

Copy
[code]
    for content in response.content:
        if content.type == "tool_use" and content.name == "bash":
            if content.input.get("restart"):
                bash_session.restart()
                result = "Bash session restarted"
            else:
                command = content.input.get("command")
                result = bash_session.execute_command(command)

            # Return result to Claude
            tool_result = {
                "type": "tool_result",
                "tool_use_id": content.id,
                "content": result
            }

[/code]

4

Implement safety measures

Add validation and restrictions:

Copy
[code]
    def validate_command(command):
        # Block dangerous commands
        dangerous_patterns = ['rm -rf /', 'format', ':(){:|:&};:']
        for pattern in dangerous_patterns:
            if pattern in command:
                return False, f"Command contains dangerous pattern: {pattern}"

        # Add more validation as needed
        return True, None

[/code]

### Handle errors

When implementing the bash tool, handle various error scenarios:

Command execution timeout

If a command takes too long to execute:

Copy
[code]
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Command timed out after 30 seconds",
          "is_error": true
        }
      ]
    }

[/code]

Command not found

If a command doesn’t exist:

Copy
[code]
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "bash: nonexistentcommand: command not found",
          "is_error": true
        }
      ]
    }

[/code]

Permission denied

If there are permission issues:

Copy
[code]
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "bash: /root/sensitive-file: Permission denied",
          "is_error": true
        }
      ]
    }

[/code]

### Follow implementation best practices

Use command timeouts

Implement timeouts to prevent hanging commands:

Copy
[code]
    def execute_with_timeout(command, timeout=30):
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return f"Command timed out after {timeout} seconds"

[/code]

Maintain session state

Keep the bash session persistent to maintain environment variables and working directory:

Copy
[code]
    # Commands run in the same session maintain state
    commands = [
        "cd /tmp",
        "echo 'Hello' > test.txt",
        "cat test.txt"  # This works because we're still in /tmp
    ]

[/code]

Handle large outputs

Truncate very large outputs to prevent token limit issues:

Copy
[code]
    def truncate_output(output, max_lines=100):
        lines = output.split('\n')
        if len(lines) > max_lines:
            truncated = '\n'.join(lines[:max_lines])
            return f"{truncated}\n\n... Output truncated ({len(lines)} total lines) ..."
        return output

[/code]

Log all commands

Keep an audit trail of executed commands:

Copy
[code]
    import logging

    def log_command(command, output, user_id):
        logging.info(f"User {user_id} executed: {command}")
        logging.info(f"Output: {output[:200]}...")  # Log first 200 chars

[/code]

Sanitize outputs

Remove sensitive information from command outputs:

Copy
[code]
    def sanitize_output(output):
        # Remove potential secrets or credentials
        import re
        # Example: Remove AWS credentials
        output = re.sub(r'aws_access_key_id\s*=\s*\S+', 'aws_access_key_id=***', output)
        output = re.sub(r'aws_secret_access_key\s*=\s*\S+', 'aws_secret_access_key=***', output)
        return output

[/code]

## Security

The bash tool provides direct system access. Implement these essential safety measures:

  * Running in isolated environments \(Docker/VM\)
  * Implementing command filtering and allowlists
  * Setting resource limits \(CPU, memory, disk\)
  * Logging all executed commands

### Key recommendations

  * Use `ulimit` to set resource constraints
  * Filter dangerous commands \(`sudo`, `rm -rf`, etc.\)
  * Run with minimal user permissions
  * Monitor and log all command execution

## Pricing

The bash tool adds **245 input tokens** to your API calls. Additional tokens are consumed by:

  * Command outputs \(stdout/stderr\)
  * Error messages
  * Large file contents

See [tool use pricing](/en/docs/agents-and-tools/tool-use/overview#pricing) for complete pricing details.

## Common patterns

### Development workflows

  * Running tests: `pytest && coverage report`
  * Building projects: `npm install && npm run build`
  * Git operations: `git status && git add . && git commit -m "message"`

### File operations

  * Processing data: `wc -l *.csv && ls -lh *.csv`
  * Searching files: `find . -name "*.py" | xargs grep "pattern"`
  * Creating backups: `tar -czf backup.tar.gz ./data`

### System tasks

  * Checking resources: `df -h && free -m`
  * Process management: `ps aux | grep python`
  * Environment setup: `export PATH=$PATH:/new/path && echo $PATH`

## Limitations

  * **No interactive commands** : Cannot handle `vim`, `less`, or password prompts
  * **No GUI applications** : Command-line only
  * **Session scope** : Persists within conversation, lost between API calls
  * **Output limits** : Large outputs may be truncated
  * **No streaming** : Results returned after completion

## Combining with other tools

The bash tool is most powerful when combined with the [text editor](/en/docs/agents-and-tools/tool-use/text-editor-tool) and other tools.

## Next steps

## [Tool use overviewLearn about tool use with Claude](/en/docs/agents-and-tools/tool-use/overview)## [Text editor toolView and edit text files with Claude](/en/docs/agents-and-tools/tool-use/text-editor-tool)

Was this page helpful?

YesNo

[Fine-grained tool streaming](/en/docs/agents-and-tools/tool-use/fine-grained-tool-streaming)[Code execution tool](/en/docs/agents-and-tools/tool-use/code-execution-tool)
