url: https://docs.claude.com/en/docs/agents-and-tools/tool-use/text-editor-tool

---

Claude can use an Anthropic-defined text editor tool to view and modify text files, helping you debug, fix, and improve your code or other text documents. This allows Claude to directly interact with your files, providing hands-on assistance rather than just suggesting changes.

## Model compatibility

Model| Tool Version
---|---
Claude Sonnet 4, Sonnet 4.5, Opus 4, and Opus 4.1| `text_editor_20250728`
Claude Sonnet 3.7| `text_editor_20250124`
Claude Sonnet 3.5 \([deprecated](/en/docs/about-claude/model-deprecations)\)| `text_editor_20241022`

Claude Sonnet 3.5 \([deprecated](/en/docs/about-claude/model-deprecations)\) requires the `computer-use-2024-10-22` beta header when using the text editor tool.The text editor tool is generally available in Claude 4 models and Claude Sonnet 3.7.

The `text_editor_20250728` tool for Claude 4 models does not include the `undo_edit` command. If you require this functionality, you’ll need to use Claude Sonnet 3.7 or Sonnet 3.5 with their respective tool versions.

Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.

## When to use the text editor tool

Some examples of when to use the text editor tool are:

  * **Code debugging** : Have Claude identify and fix bugs in your code, from syntax errors to logic issues.
  * **Code refactoring** : Let Claude improve your code structure, readability, and performance through targeted edits.
  * **Documentation generation** : Ask Claude to add docstrings, comments, or README files to your codebase.
  * **Test creation** : Have Claude create unit tests for your code based on its understanding of the implementation.

## Use the text editor tool

  * Claude 4
  * Claude Sonnet 3.7
  * Claude Sonnet 3.5 \(deprecated\)

Provide the text editor tool \(named `str_replace_based_edit_tool`\) to Claude using the Messages API.You can optionally specify a `max_characters` parameter to control truncation when viewing large files.

`max_characters` is only compatible with `text_editor_20250728` and later versions of the text editor tool.

Shell

Python

TypeScript

Java

Copy
[code]
    curl https://api.anthropic.com/v1/messages \
      -H "content-type: application/json" \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -d '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "tools": [
          {
            "type": "text_editor_20250728",
            "name": "str_replace_based_edit_tool",
            "max_characters": 10000
          }
        ],
        "messages": [
          {
            "role": "user",
            "content": "There'\''s a syntax error in my primes.py file. Can you help me fix it?"
          }
        ]
      }'

[/code]

The text editor tool can be used in the following way:

1

Provide Claude with the text editor tool and a user prompt

  * Include the text editor tool in your API request
  * Provide a user prompt that may require examining or modifying files, such as “Can you fix the syntax error in my code?”

2

Claude uses the tool to examine files or directories

  * Claude assesses what it needs to look at and uses the `view` command to examine file contents or list directory contents
  * The API response will contain a `tool_use` content block with the `view` command

3

Execute the view command and return results

  * Extract the file or directory path from Claude’s tool use request
  * Read the file’s contents or list the directory contents
  * If a `max_characters` parameter was specified in the tool configuration, truncate the file contents to that length
  * Return the results to Claude by continuing the conversation with a new `user` message containing a `tool_result` content block

4

Claude uses the tool to modify files

  * After examining the file or directory, Claude may use a command such as `str_replace` to make changes or `insert` to add text at a specific line number.
  * If Claude uses the `str_replace` command, Claude constructs a properly formatted tool use request with the old text and new text to replace it with

5

Execute the edit and return results

  * Extract the file path, old text, and new text from Claude’s tool use request
  * Perform the text replacement in the file
  * Return the results to Claude

6

Claude provides its analysis and explanation

  * After examining and possibly editing the files, Claude provides a complete explanation of what it found and what changes it made

### Text editor tool commands

The text editor tool supports several commands for viewing and modifying files:

#### view

The `view` command allows Claude to examine the contents of a file or list the contents of a directory. It can read the entire file or a specific range of lines. Parameters:

  * `command`: Must be “view”
  * `path`: The path to the file or directory to view
  * `view_range` \(optional\): An array of two integers specifying the start and end line numbers to view. Line numbers are 1-indexed, and -1 for the end line means read to the end of the file. This parameter only applies when viewing files, not directories.

Example view commands

Copy
[code]
    // Example for viewing a file
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "str_replace_editor",
      "input": {
        "command": "view",
        "path": "primes.py"
      }
    }

    // Example for viewing a directory
    {
      "type": "tool_use",
      "id": "toolu_02B19r91rw91mr917835mr9",
      "name": "str_replace_editor",
      "input": {
        "command": "view",
        "path": "src/"
      }
    }

[/code]

#### str\_replace

The `str_replace` command allows Claude to replace a specific string in a file with a new string. This is used for making precise edits. Parameters:

  * `command`: Must be “str\_replace”
  * `path`: The path to the file to modify
  * `old_str`: The text to replace \(must match exactly, including whitespace and indentation\)
  * `new_str`: The new text to insert in place of the old text

Example str\_replace command

Copy
[code]
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "str_replace_editor",
      "input": {
        "command": "str_replace",
        "path": "primes.py",
        "old_str": "for num in range(2, limit + 1)",
        "new_str": "for num in range(2, limit + 1):"
      }
    }

[/code]

#### create

The `create` command allows Claude to create a new file with specified content. Parameters:

  * `command`: Must be “create”
  * `path`: The path where the new file should be created
  * `file_text`: The content to write to the new file

Example create command

Copy
[code]
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "str_replace_editor",
      "input": {
        "command": "create",
        "path": "test_primes.py",
        "file_text": "import unittest\nimport primes\n\nclass TestPrimes(unittest.TestCase):\n    def test_is_prime(self):\n        self.assertTrue(primes.is_prime(2))\n        self.assertTrue(primes.is_prime(3))\n        self.assertFalse(primes.is_prime(4))\n\nif __name__ == '__main__':\n    unittest.main()"
      }
    }

[/code]

#### insert

The `insert` command allows Claude to insert text at a specific location in a file. Parameters:

  * `command`: Must be “insert”
  * `path`: The path to the file to modify
  * `insert_line`: The line number after which to insert the text \(0 for beginning of file\)
  * `new_str`: The text to insert

Example insert command

Copy
[code]
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "str_replace_editor",
      "input": {
        "command": "insert",
        "path": "primes.py",
        "insert_line": 0,
        "new_str": "\"\"\"Module for working with prime numbers.\n\nThis module provides functions to check if a number is prime\nand to generate a list of prime numbers up to a given limit.\n\"\"\"\n"
      }
    }

[/code]

#### undo\_edit

The `undo_edit` command allows Claude to revert the last edit made to a file.

This command is only available in Claude Sonnet 3.7 and Claude Sonnet 3.5 \([deprecated](/en/docs/about-claude/model-deprecations)\). It is not supported in Claude 4 models using the `text_editor_20250728`.

Parameters:

  * `command`: Must be “undo\_edit”
  * `path`: The path to the file whose last edit should be undone

Example undo\_edit command

Copy
[code]
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "str_replace_editor",
      "input": {
        "command": "undo_edit",
        "path": "primes.py"
      }
    }

[/code]

### Example: Fixing a syntax error with the text editor tool

  * Claude 4
  * Claude Sonnet 3.7

This example demonstrates how Claude 4 models use the text editor tool to fix a syntax error in a Python file.First, your application provides Claude with the text editor tool and a prompt to fix a syntax error:

Shell

Python

TypeScript

Java

Copy
[code]
    curl https://api.anthropic.com/v1/messages \
      -H "content-type: application/json" \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -d '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "tools": [
          {
            "type": "text_editor_20250728",
            "name": "str_replace_based_edit_tool"
          }
        ],
        "messages": [
          {
            "role": "user",
            "content": "There'\''s a syntax error in my primes.py file. Can you help me fix it?"
          }
        ]
      }'

[/code]

Claude will use the text editor tool first to view the file:

Copy
[code]
    {
      "id": "msg_01XAbCDeFgHiJkLmNoPQrStU",
      "model": "claude-sonnet-4-5",
      "stop_reason": "tool_use",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue."
        },
        {
          "type": "tool_use",
          "id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
          "name": "str_replace_based_edit_tool",
          "input": {
            "command": "view",
            "path": "primes.py"
          }
        }
      ]
    }

[/code]

Your application should then read the file and return its contents to Claude:

Shell

Python

TypeScript

Java

Copy
[code]
    curl https://api.anthropic.com/v1/messages \
      -H "content-type: application/json" \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -d '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "tools": [
          {
            "type": "text_editor_20250728",
            "name": "str_replace_based_edit_tool"
          }
        ],
        "messages": [
          {
            "role": "user",
            "content": "There'\''s a syntax error in my primes.py file. Can you help me fix it?"
          },
          {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "I'\''ll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue."
                    },
                    {
                        "type": "tool_use",
                        "id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
                        "name": "str_replace_based_edit_tool",
                        "input": {
                            "command": "view",
                            "path": "primes.py"
                        }
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
                        "content": "1: def is_prime(n):\n2:     \"\"\"Check if a number is prime.\"\"\"\n3:     if n <= 1:\n4:         return False\n5:     if n <= 3:\n6:         return True\n7:     if n % 2 == 0 or n % 3 == 0:\n8:         return False\n9:     i = 5\n10:     while i * i <= n:\n11:         if n % i == 0 or n % (i + 2) == 0:\n12:             return False\n13:         i += 6\n14:     return True\n15: \n16: def get_primes(limit):\n17:     \"\"\"Generate a list of prime numbers up to the given limit.\"\"\"\n18:     primes = []\n19:     for num in range(2, limit + 1)\n20:         if is_prime(num):\n21:             primes.append(num)\n22:     return primes\n23: \n24: def main():\n25:     \"\"\"Main function to demonstrate prime number generation.\"\"\"\n26:     limit = 100\n27:     prime_list = get_primes(limit)\n28:     print(f\"Prime numbers up to {limit}:\")\n29:     print(prime_list)\n30:     print(f\"Found {len(prime_list)} prime numbers.\")\n31: \n32: if __name__ == \"__main__\":\n33:     main()"
                    }
                ]
            }
        ]
      }'

[/code]

**Line numbers** In the example above, the `view` tool result includes file contents with line numbers prepended to each line \(e.g., “1: def is\_prime\(n\):”\). Line numbers are not required, but they are essential for successfully using the `view_range` parameter to examine specific sections of files and the `insert_line` parameter to add content at precise locations.

Claude will identify the syntax error and use the `str_replace` command to fix it:

Copy
[code]
    {
      "id": "msg_01VwXyZAbCdEfGhIjKlMnO",
      "model": "claude-sonnet-4-5",
      "stop_reason": "tool_use",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you."
        },
        {
          "type": "tool_use",
          "id": "toolu_01PqRsTuVwXyZAbCdEfGh",
          "name": "str_replace_based_edit_tool",
          "input": {
            "command": "str_replace",
            "path": "primes.py",
            "old_str": "    for num in range(2, limit + 1)",
            "new_str": "    for num in range(2, limit + 1):"
          }
        }
      ]
    }

[/code]

Your application should then make the edit and return the result:

Python

TypeScript

Java

Copy
[code]
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        tools=[
            {
                "type": "text_editor_20250728",
                "name": "str_replace_based_edit_tool"
            }
        ],
        messages=[
            # Previous messages...
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you."
                    },
                    {
                        "type": "tool_use",
                        "id": "toolu_01PqRsTuVwXyZAbCdEfGh",
                        "name": "str_replace_based_edit_tool",
                        "input": {
                            "command": "str_replace",
                            "path": "primes.py",
                            "old_str": "    for num in range(2, limit + 1)",
                            "new_str": "    for num in range(2, limit + 1):"
                        }
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": "toolu_01PqRsTuVwXyZAbCdEfGh",
                        "content": "Successfully replaced text at exactly one location."
                    }
                ]
            }
        ]
    )

[/code]

Finally, Claude will provide a complete explanation of the fix:

Copy
[code]
    {
      "id": "msg_01IjKlMnOpQrStUvWxYzAb",
      "model": "claude-sonnet-4-5",
      "stop_reason": "end_turn",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "I've fixed the syntax error in your primes.py file. The issue was in the `get_primes` function at line 19. There was a missing colon (:) at the end of the for loop line.\n\nHere's what I changed:\n\nFrom:\n```python\nfor num in range(2, limit + 1)\n```\n\nTo:\n```python\nfor num in range(2, limit + 1):\n```\n\nIn Python, a colon is required at the end of statements that start a new code block, such as for loops, if statements, function definitions, etc. Without the colon, Python raises a syntax error because it doesn't know where the code block begins.\n\nYour code should now run correctly. The function will properly generate a list of prime numbers up to the specified limit."
        }
      ]
    }

[/code]

* * *

## Implement the text editor tool

The text editor tool is implemented as a schema-less tool. When using this tool, you don’t need to provide an input schema as with other tools; the schema is built into Claude’s model and can’t be modified. The tool type depends on the model version:

  * **Claude 4** : `type: "text_editor_20250728"`
  * **Claude Sonnet 3.7** : `type: "text_editor_20250124"`
  * **Claude Sonnet 3.5 \([deprecated](/en/docs/about-claude/model-deprecations)\)**: `type: "text_editor_20241022"`

1

Initialize your editor implementation

Create helper functions to handle file operations like reading, writing, and modifying files. Consider implementing backup functionality to recover from mistakes.

2

Handle editor tool calls

Create a function that processes tool calls from Claude based on the command type:

Copy
[code]
    def handle_editor_tool(tool_call, model_version):
        input_params = tool_call.input
        command = input_params.get('command', '')
        file_path = input_params.get('path', '')

        if command == 'view':
            # Read and return file contents
            pass
        elif command == 'str_replace':
            # Replace text in file
            pass
        elif command == 'create':
            # Create new file
            pass
        elif command == 'insert':
            # Insert text at location
            pass
        elif command == 'undo_edit':
            # Check if it's a Claude 4 model
            if 'str_replace_based_edit_tool' in model_version:
                return {"error": "undo_edit command is not supported in Claude 4"}
            # Restore from backup for Claude 3.7/3.5
            pass

[/code]

3

Implement security measures

Add validation and security checks:

  * Validate file paths to prevent directory traversal
  * Create backups before making changes
  * Handle errors gracefully
  * Implement permissions checks

4

Process Claude's responses

Extract and handle tool calls from Claude’s responses:

Copy
[code]
    # Process tool use in Claude's response
    for content in response.content:
        if content.type == "tool_use":
            # Execute the tool based on command
            result = handle_editor_tool(content)

            # Return result to Claude
            tool_result = {
                "type": "tool_result",
                "tool_use_id": content.id,
                "content": result
            }

[/code]

When implementing the text editor tool, keep in mind:

  1. **Security** : The tool has access to your local filesystem, so implement proper security measures.
  2. **Backup** : Always create backups before allowing edits to important files.
  3. **Validation** : Validate all inputs to prevent unintended changes.
  4. **Unique matching** : Make sure replacements match exactly one location to avoid unintended edits.

### Handle errors

When using the text editor tool, various errors may occur. Here is guidance on how to handle them:

File not found

If Claude tries to view or modify a file that doesn’t exist, return an appropriate error message in the `tool_result`:

Copy
[code]
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: File not found",
          "is_error": true
        }
      ]
    }

[/code]

Multiple matches for replacement

If Claude’s `str_replace` command matches multiple locations in the file, return an appropriate error message:

Copy
[code]
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Found 3 matches for replacement text. Please provide more context to make a unique match.",
          "is_error": true
        }
      ]
    }

[/code]

No matches for replacement

If Claude’s `str_replace` command doesn’t match any text in the file, return an appropriate error message:

Copy
[code]
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: No match found for replacement. Please check your text and try again.",
          "is_error": true
        }
      ]
    }

[/code]

Permission errors

If there are permission issues with creating, reading, or modifying files, return an appropriate error message:

Copy
[code]
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Permission denied. Cannot write to file.",
          "is_error": true
        }
      ]
    }

[/code]

### Follow implementation best practices

Provide clear context

When asking Claude to fix or modify code, be specific about what files need to be examined or what issues need to be addressed. Clear context helps Claude identify the right files and make appropriate changes.**Less helpful prompt** : “Can you fix my code?”**Better prompt** : “There’s a syntax error in my primes.py file that prevents it from running. Can you fix it?”

Be explicit about file paths

Specify file paths clearly when needed, especially if you’re working with multiple files or files in different directories.**Less helpful prompt** : “Review my helper file”**Better prompt** : “Can you check my utils/helpers.py file for any performance issues?”

Create backups before editing

Implement a backup system in your application that creates copies of files before allowing Claude to edit them, especially for important or production code.

Copy
[code]
    def backup_file(file_path):
        """Create a backup of a file before editing."""
        backup_path = f"{file_path}.backup"
        if os.path.exists(file_path):
            with open(file_path, 'r') as src, open(backup_path, 'w') as dst:
                dst.write(src.read())

[/code]

Handle unique text replacement carefully

The `str_replace` command requires an exact match for the text to be replaced. Your application should ensure that there is exactly one match for the old text or provide appropriate error messages.

Copy
[code]
    def safe_replace(file_path, old_text, new_text):
        """Replace text only if there's exactly one match."""
        with open(file_path, 'r') as f:
            content = f.read()

        count = content.count(old_text)
        if count == 0:
            return "Error: No match found"
        elif count > 1:
            return f"Error: Found {count} matches"
        else:
            new_content = content.replace(old_text, new_text)
            with open(file_path, 'w') as f:
                f.write(new_content)
            return "Successfully replaced text"

[/code]

Verify changes

After Claude makes changes to a file, verify the changes by running tests or checking that the code still works as expected.

Copy
[code]
    def verify_changes(file_path):
        """Run tests or checks after making changes."""
        try:
            # For Python files, check for syntax errors
            if file_path.endswith('.py'):
                import ast
                with open(file_path, 'r') as f:
                    ast.parse(f.read())
                return "Syntax check passed"
        except Exception as e:
            return f"Verification failed: {str(e)}"

[/code]

* * *

## Pricing and token usage

The text editor tool uses the same pricing structure as other tools used with Claude. It follows the standard input and output token pricing based on the Claude model you’re using. In addition to the base tokens, the following additional input tokens are needed for the text editor tool: Tool| Additional input tokens
---|---
`text_editor_20250429` \(Claude 4\)| 700 tokens
`text_editor_20250124` \(Claude Sonnet 3.7\)| 700 tokens
`text_editor_20241022` \(Claude Sonnet 3.5 \([deprecated](/en/docs/about-claude/model-deprecations)\)\)| 700 tokens
For more detailed information about tool pricing, see [Tool use pricing](/en/docs/agents-and-tools/tool-use/overview#pricing).

## Integrate the text editor tool with other tools

The text editor tool can be used alongside other Claude tools. When combining tools, ensure you:

  * Match the tool version with the model you’re using
  * Account for the additional token usage for all tools included in your request

## Change log

Date| Version| Changes
---|---|---
July 28, 2025| `text_editor_20250728`| Release of an updated text editor Tool that fixes some issues and adds an optional `max_characters` parameter. It is otherwise identical to `text_editor_20250429`.
April 29, 2025| `text_editor_20250429`| Release of the text editor Tool for Claude 4. This version removes the `undo_edit` command but maintains all other capabilities. The tool name has been updated to reflect its str\_replace-based architecture.
March 13, 2025| `text_editor_20250124`| Introduction of standalone text editor Tool documentation. This version is optimized for Claude Sonnet 3.7 but has identical capabilities to the previous version.
October 22, 2024| `text_editor_20241022`| Initial release of the text editor Tool with Claude Sonnet 3.5 \([deprecated](/en/docs/about-claude/model-deprecations)\). Provides capabilities for viewing, creating, and editing files through the `view`, `create`, `str_replace`, `insert`, and `undo_edit` commands.

## Next steps

Here are some ideas for how to use the text editor tool in more convenient and powerful ways:

  * **Integrate with your development workflow** : Build the text editor tool into your development tools or IDE
  * **Create a code review system** : Have Claude review your code and make improvements
  * **Build a debugging assistant** : Create a system where Claude can help you diagnose and fix issues in your code
  * **Implement file format conversion** : Let Claude help you convert files from one format to another
  * **Automate documentation** : Set up workflows for Claude to automatically document your code

As you build applications with the text editor tool, we’re excited to see how you leverage Claude’s capabilities to enhance your development workflow and productivity.

## [Tool use overviewLearn how to implement tool workflows for use with Claude.](/en/docs/agents-and-tools/tool-use/overview)## [Token-efficient tool useReduce latency and costs when using tools with Claude Sonnet 3.7.](/en/docs/agents-and-tools/tool-use/token-efficient-tool-use)## [Bash toolExecute shell commands with Claude.](/en/docs/agents-and-tools/tool-use/bash-tool)

Was this page helpful?

YesNo

[Computer use tool](/en/docs/agents-and-tools/tool-use/computer-use-tool)[Web fetch tool](/en/docs/agents-and-tools/tool-use/web-fetch-tool)
