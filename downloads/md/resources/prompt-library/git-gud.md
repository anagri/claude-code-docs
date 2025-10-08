url: https://docs.claude.com/en/resources/prompt-library/git-gud

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

Role| Content
---|---
User| I have made some changes to my local files and I want to save them in my local Git repository. What Git command should I use?

## Example Output

To save the changes you’ve made to your local files in your local Git repository, you should use the following Git commands:

  1. `git add .` or `git add <file>`
     * This command stages the changes you’ve made, preparing them to be committed. The `.` adds all changes in the current directory and its subdirectories. If you only want to stage specific files, replace `.` with the file name or path.
  2. `git commit -m "Your commit message"`
     * This command commits the staged changes to your local Git repository. The `-m` flag allows you to provide a commit message describing the changes you’ve made. Replace `"Your commit message"` with a brief, descriptive summary of your changes.

For example, if you’ve made changes to a file named `example.txt`, you would run:

Copy
[code]
    git add example.txt
    git commit -m "Update example.txt with new content"

[/code]

These commands will save your changes in your local Git repository, creating a new commit with the provided message. You can later push these changes to a remote repository or continue working on your local branch. Remember to run these commands from within your Git repository directory in your terminal or command prompt.

* * *

## API Request

  * Python
  * TypeScript
  * AWS Bedrock Python
  * AWS Bedrock TypeScript
  * Vertex AI Python
  * Vertex AI TypeScript

Copy
[code]
    import anthropic

    client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key="my_api_key",
    )
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "I have made some changes to my local files and I want to save them in my local Git repository. What Git command should I use?",
                    }
                ],
            }
        ],
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Mood colorizer](/en/resources/prompt-library/mood-colorizer)[Simile savant](/en/resources/prompt-library/simile-savant)
