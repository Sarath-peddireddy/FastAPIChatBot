from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from loguru import logger
import uvicorn

from .models import get_db
from .database import seed_database, get_customers_by_query
from .utils import generate_sql_query, format_query_results

app = FastAPI(title="LLM-Powered Chatbot API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logger.add("app.log", rotation="500 MB")

class QueryRequest(BaseModel):
    query: str

@app.on_event("startup")
async def startup_event():
    """Initialize database and seed data on startup"""
    db = next(get_db())
    seed_database(db)
    logger.info("Database initialized and seeded")

@app.post("/api/query")
async def process_query(request: QueryRequest, db: Session = Depends(get_db)):
    """
    Process natural language query and return results
    """
    try:
        # Generate SQL query from natural language
        sql_query = generate_sql_query(request.query)
        
        # Execute query and get results
        results = get_customers_by_query(db, sql_query)
        
        # Format results
        formatted_results = format_query_results(results)
        
        return {
            "status": "success",
            "query": request.query,
            "sql_query": sql_query,
            "results": formatted_results
        }
        
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/customers")
async def get_customers(db: Session = Depends(get_db)):
    """
    Get all customers
    """
    try:
        results = db.execute("SELECT * FROM customers").fetchall()
        return format_query_results(results)
    except Exception as e:
        logger.error(f"Error fetching customers: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 