from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "defog/sqlcoder-7b"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    offload_folder="offload",  
)

def build_prompt(question):

    schema = """
    Database Schema:

    customers(id, name, country)
    orders(id, customer_id, amount, order_date)
    """

    prompt = f"""
    You are a SQL expert.

    {schema}

    Write a SQL query for the following question:
    {question}

    Only return SQL.
    """

    return prompt

def generate_sql(question):

    prompt = build_prompt(question)

    inputs = tokenizer(prompt, return_tensors="pt")

    output = model.generate(
        **inputs,
        max_new_tokens=200
    )

    sql = tokenizer.decode(output[0], skip_special_tokens=True)

    return sql

if __name__=="main":
    print("Loaded model successfully")
