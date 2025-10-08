url: https://docs.claude.com/en/resources/prompt-library/csv-converter

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| As a data conversion expert, your task is to convert data from different formats \(JSON, XML, etc.\) into properly formatted CSV files. The user will provide the input data in the original format, along with any specific requirements or preferences for the CSV output \(e.g., column order, delimiter, encoding\). Ensure that you have a clear understanding of the data structure and the desired CSV format, asking any clarifying questions as needed. Once you have the necessary information, generate the CSV output by following the appropriate formatting rules, such as using commas as delimiters, enclosing values in quotes if necessary, and handling special characters or line breaks correctly. Finally, provide any additional instructions or tips for saving or using the CSV file.
User| Please convert the following JSON data into a CSV file:

\[
\{
“name”: “John Doe”,
“age”: 30,
“city”: “New York”,
“email”: “[\[email protected\]](/cdn-cgi/l/email-protection#1973767177377d767c597c61787469757c377a7674)”
\},
\{
“name”: “Jane Smith”,
“age”: 25,
“city”: “London”,
“email”: “[\[email protected\]](/cdn-cgi/l/email-protection#e288838c87cc918f8b968aa2879a838f928e87cc818d8f)”
\},
\{
“name”: “Bob Johnson”,
“age”: 35,
“city”: “Paris”,
“email”: “[\[email protected\]](/cdn-cgi/l/email-protection#11737e733f7b7e797f627e7f517469707c617d743f727e7c)”
\}
\]
Requirements:
\- Columns in the CSV should be in the order: name, age, city, email
\- Use semicolons \(;\) as delimiters
\- Enclose all values in double quotes \(“\)

## Example Output

Based on the provided JSON data and requirements, here’s the converted CSV file:

csv

Copy
[code]
    "name";"age";"city";"email"
    "John Doe";"30";"New York";"[email protected]"
    "Jane Smith";"25";"London";"[email protected]"
    "Bob Johnson";"35";"Paris";"[email protected]"

[/code]

Explanation:

  * The first line of the CSV file contains the column headers: “name”, “age”, “city”, and “email”, separated by semicolons \(;\) and enclosed in double quotes \(”\).
  * Each subsequent line represents a row of data, with values separated by semicolons \(;\) and enclosed in double quotes \(”\).
  * The order of the values in each row corresponds to the specified column order: name, age, city, and email.
  * Special characters, if present in the values, are preserved within the double quotes.

To save the CSV file:

  1. Copy the CSV data provided above.
  2. Open a text editor \(e.g., Notepad, TextEdit, or any other plain text editor\).
  3. Paste the CSV data into the text editor.
  4. Save the file with a .csv extension \(e.g., data.csv\).

Note: When opening the CSV file in a spreadsheet application \(e.g., Microsoft Excel, Google Sheets\), make sure to specify the correct delimiter \(semicolon\) and the presence of double quotes around the values to ensure proper formatting.

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
        system="As a data conversion expert, your task is to convert data from different formats (JSON, XML, etc.) into properly formatted CSV files. The user will provide the input data in the original format, along with any specific requirements or preferences for the CSV output (e.g., column order, delimiter, encoding). Ensure that you have a clear understanding of the data structure and the desired CSV format, asking any clarifying questions as needed. Once you have the necessary information, generate the CSV output by following the appropriate formatting rules, such as using commas as delimiters, enclosing values in quotes if necessary, and handling special characters or line breaks correctly. Finally, provide any additional instructions or tips for saving or using the CSV file.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": 'Please convert the following JSON data into a CSV file: \n \n[ \n { \n "name": "John Doe", \n "age": 30, \n "city": "New York", \n "email": "[email protected]" \n }, \n { \n "name": "Jane Smith", \n "age": 25, \n "city": "London", \n "email": "[email protected]" \n }, \n { \n "name": "Bob Johnson", \n "age": 35, \n "city": "Paris", \n "email": "[email protected]" \n } \n] \n \nRequirements: \n- Columns in the CSV should be in the order: name, age, city, email \n- Use semicolons (;) as delimiters \n- Enclose all values in double quotes (")',
                    }
                ],
            }
        ],
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Neologism creator](/en/resources/prompt-library/neologism-creator)[Emoji encoder](/en/resources/prompt-library/emoji-encoder)
