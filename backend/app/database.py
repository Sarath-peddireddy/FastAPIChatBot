from sqlalchemy.orm import Session
from sqlalchemy import text
from .models import Customer, Base, engine

def init_db():
    Base.metadata.create_all(bind=engine)

def seed_database(db: Session):
    
    if db.query(Customer).first():
        return

    # Sample customer data
    customers = [
        Customer(name="John Doe", gender="Male", location="New York"),
        Customer(name="Jane Smith", gender="Female", location="Mumbai"),
        Customer(name="Alice Johnson", gender="Female", location="London"),
        Customer(name="Bob Wilson", gender="Male", location="Tokyo"),
        Customer(name="Sarah Brown", gender="Female", location="Mumbai"),
    ]

    
    for customer in customers:
        db.add(customer)
    
    db.commit()

def get_all_customers(db: Session):
    return db.query(Customer).all()

def get_customers_by_query(db: Session, query: str):
    """
    Execute a raw SQL query using SQLAlchemy text()
    """
    try:
        
        sql_query = text(query)
        
        result = db.execute(sql_query)
        return result.fetchall()
    except Exception as e:
        raise Exception(f"Error executing query: {str(e)}") 