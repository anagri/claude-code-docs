url: https://docs.claude.com/en/resources/prompt-library/sql-sorcerer

---

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself\!

| Content
---|---
System| Transform the following natural language requests into valid SQL queries. Assume a database with the following tables and columns exists:

Customers:
\- customer\_id \(INT, PRIMARY KEY\)
\- first\_name \(VARCHAR\)
\- last\_name \(VARCHAR\)
\- email \(VARCHAR\)
\- phone \(VARCHAR\)
\- address \(VARCHAR\)
\- city \(VARCHAR\)
\- state \(VARCHAR\)
\- zip\_code \(VARCHAR\)

Products:
\- product\_id \(INT, PRIMARY KEY\)
\- product\_name \(VARCHAR\)
\- description \(TEXT\)
\- category \(VARCHAR\)
\- price \(DECIMAL\)
\- stock\_quantity \(INT\)

Orders:
\- order\_id \(INT, PRIMARY KEY\)
\- customer\_id \(INT, FOREIGN KEY REFERENCES Customers\)
\- order\_date \(DATE\)
\- total\_amount \(DECIMAL\)
\- status \(VARCHAR\)

Order\_Items:
\- order\_item\_id \(INT, PRIMARY KEY\)
\- order\_id \(INT, FOREIGN KEY REFERENCES Orders\)
\- product\_id \(INT, FOREIGN KEY REFERENCES Products\)
\- quantity \(INT\)
\- price \(DECIMAL\)

Reviews:
\- review\_id \(INT, PRIMARY KEY\)
\- product\_id \(INT, FOREIGN KEY REFERENCES Products\)
\- customer\_id \(INT, FOREIGN KEY REFERENCES Customers\)
\- rating \(INT\)
\- comment \(TEXT\)
\- review\_date \(DATE\)

Employees:
\- employee\_id \(INT, PRIMARY KEY\)
\- first\_name \(VARCHAR\)
\- last\_name \(VARCHAR\)
\- email \(VARCHAR\)
\- phone \(VARCHAR\)
\- hire\_date \(DATE\)
\- job\_title \(VARCHAR\)
\- department \(VARCHAR\)
\- salary \(DECIMAL\)

Provide the SQL query that would retrieve the data based on the natural language request.
User| Get the list of customers who have placed orders but have not provided any reviews, along with the total amount they have spent on orders.

## Example output

Copy
[code]
    SELECT c.first_name, c.last_name, SUM(o.total_amount) AS total_spent
    FROM Customers c
    INNER JOIN Orders o ON c.customer_id = o.customer_id
    LEFT JOIN Reviews r ON c.customer_id = r.customer_id
    WHERE r.review_id IS NULL
    GROUP BY c.customer_id, c.first_name, c.last_name;

[/code]

## API Request

* * *

  * Python
  * TypeScript
  * AWS Bedrock Python
  * AWS Bedrock TypeScript
  * Vertex AI Python
  * Vertex AI TypeScript

Copy
[code]
    import anthropic

    client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=0,
      system="Transform the following natural language requests into valid SQL queries. Assume a database with the following tables and columns exists: \n \nCustomers: \n- customer_id (INT, PRIMARY KEY) \n- first_name (VARCHAR) \n- last_name (VARCHAR) \n- email (VARCHAR) \n- phone (VARCHAR) \n- address (VARCHAR) \n- city (VARCHAR) \n- state (VARCHAR) \n- zip_code (VARCHAR) \n \nProducts: \n- product_id (INT, PRIMARY KEY) \n- product_name (VARCHAR) \n- description (TEXT) \n- category (VARCHAR) \n- price (DECIMAL) \n- stock_quantity (INT) \n \nOrders: \n- order_id (INT, PRIMARY KEY) \n- customer_id (INT, FOREIGN KEY REFERENCES Customers) \n- order_date (DATE) \n- total_amount (DECIMAL) \n- status (VARCHAR) \n \nOrder_Items: \n- order_item_id (INT, PRIMARY KEY) \n- order_id (INT, FOREIGN KEY REFERENCES Orders) \n- product_id (INT, FOREIGN KEY REFERENCES Products) \n- quantity (INT) \n- price (DECIMAL) \n \nReviews: \n- review_id (INT, PRIMARY KEY) \n- product_id (INT, FOREIGN KEY REFERENCES Products) \n- customer_id (INT, FOREIGN KEY REFERENCES Customers) \n- rating (INT) \n- comment (TEXT) \n- review_date (DATE) \n \nEmployees: \n- employee_id (INT, PRIMARY KEY) \n- first_name (VARCHAR) \n- last_name (VARCHAR) \n- email (VARCHAR) \n- phone (VARCHAR) \n- hire_date (DATE) \n- job_title (VARCHAR) \n- department (VARCHAR) \n- salary (DECIMAL) \n \nProvide the SQL query that would retrieve the data based on the natural language request.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Get the list of customers who have placed orders but have not provided any reviews, along with the total amount they have spent on orders."
            }
          ]
        }
      ]
    )
    print(message.content)

[/code]

Was this page helpful?

YesNo

[Cite your sources](/en/resources/prompt-library/cite-your-sources)[Dream interpreter](/en/resources/prompt-library/dream-interpreter)
