from fastapi import FastAPI
from pydantic import BaseModel
 
app = FastAPI()
 
class Sales(BaseModel):
    product: str
    quantity: int
    price: float
 
@app.post("/sales/")
def create_sales(sales: Sales):
    total = sales.quantity * sales.price
    return {
        "product": sales.product,
        "total_amount": total
    }
 