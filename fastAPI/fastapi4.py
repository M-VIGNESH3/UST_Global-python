from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
 
# Initialize FastAPI app
app = FastAPI()
 
# Pydantic model for input validation
class Sales(BaseModel):
    product: str
    quantity: int
    price: float
 
# Initialize the database and table
def init_db():
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            quantity INTEGER,
            price REAL
        )
    """)
    conn.commit()
    conn.close()
 
# Run database initialization
init_db()
 
# POST API: Add a new sale
@app.post("/sales/")
def create_sales(sale: Sales):
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()
 
    cursor.execute(
        "INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)",
        (sale.product, sale.quantity, sale.price)
    )
 
    conn.commit()
    conn.close()
 
    total = sale.quantity * sale.price
    return {"product": sale.product, "total_amount": total}
 
# GET API: Fetch all sales
@app.get("/sales/")
def get_sales():
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()
 
    cursor.execute("SELECT product, quantity, price FROM sales")
    rows = cursor.fetchall()
    conn.close()
 
    # Convert tuples to dictionary for better JSON response
    sales_list = [{"product": row[0], "quantity": row[1], "price": row[2]} for row in rows]
    return sales_list
 