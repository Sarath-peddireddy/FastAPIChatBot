import os
from groq import Groq
from loguru import logger
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def clean_sql_query(query: str) -> str:
    """
    Clean the SQL query by removing markdown formatting and extra whitespace
    """
    # Remove markdown code block syntax
    query = query.replace('```sql', '').replace('```', '')
    # Remove extra whitespace and newlines
    query = ' '.join(query.split())
    return query.strip()

def generate_sql_query(natural_query: str) -> str:
    """
    Use Groq LLM to convert natural language query to SQL
    """
    try:
        prompt = f"""
        Convert the following natural language query into a SQL query for a SQLite database.
        The database has a 'customers' table with columns: customer_id, name, gender, location.
        
        Natural Language Query: {natural_query}
        
        Return only the SQL query without any explanation or markdown formatting.
        """
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a SQL expert that converts natural language to SQL queries. Return only the SQL query without any markdown formatting or explanation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
            max_tokens=150
        )
        
        sql_query = response.choices[0].message.content.strip()
        # Clean the SQL query
        sql_query = clean_sql_query(sql_query)
        logger.info(f"Generated SQL query: {sql_query}")
        return sql_query
        
    except Exception as e:
        logger.error(f"Error generating SQL query: {str(e)}")
        raise Exception(f"Failed to generate SQL query: {str(e)}")

def format_query_results(results):
    """
    Format the query results into a list of dictionaries
    """
    if not results:
        return []
    
    # Get column names from the result keys
    if hasattr(results[0], '_mapping'):
        # For SQLAlchemy 2.0 style results
        columns = results[0]._mapping.keys()
        formatted_results = [dict(row._mapping) for row in results]
    else:
        # For older SQLAlchemy versions
        columns = results[0].keys()
        formatted_results = [dict(zip(columns, row)) for row in results]
    
    return formatted_results 