from fastapi import FastAPI
from api.inventory import router as inventory_router
from api.stores import router as stores_router

app = FastAPI(title="Retail Inventory Management Service")

app.include_router(inventory_router)
app.include_router(stores_router)

@app.get("/")
def home():
    return {"message": "Retail Inventory Management Service is running"}
