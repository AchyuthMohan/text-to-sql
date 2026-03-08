# SQL Generator

## Description

This project is a SQL query generator that uses a pre-trained language model (defog/sqlcoder-7b) to convert natural language questions into SQL queries. It is based on the Hugging Face Transformers library and generates SQL for a predefined database schema consisting of `customers` and `orders` tables.

The schema includes:
- `customers(id, name, country)`
- `orders(id, customer_id, amount, order_date)`

## Features

- Loads a pre-trained SQL generation model
- Builds prompts with the database schema
- Generates SQL queries from natural language questions
- Uses GPU acceleration if available (via device_map="auto")

## Installation

1. Clone or download the project to your local machine.

2. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Currently, the script loads the model and prints a success message. To generate SQL queries, you can modify the script or extend it.

Example usage in code:
```python
from main import generate_sql

question = "What are the names of customers from the USA?"
sql = generate_sql(question)
print(sql)
```

## Requirements

- Python 3.7+
- Hugging Face Transformers library
- Sufficient RAM/VRAM for loading the 7B parameter model (consider using a machine with GPU)

## Notes

- The model is large (7B parameters), so loading may take time and require significant resources.
- The database schema is hardcoded in the `build_prompt` function. Modify it as needed for different schemas.
- Ensure you have internet access to download the model from Hugging Face on first run.

## License

This project does not specify a license. Please check with the original model providers for usage terms.