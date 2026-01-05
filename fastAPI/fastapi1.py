from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/sales")
def get_sales():
    return {"total_sales": 50000}