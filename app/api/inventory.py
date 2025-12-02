from fastapi import APIRouter
from db.connection import get_db

router = APIRouter(prefix="/inventory")

@router.get("/{store_id}")
def get_inventory(store_id: int):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT product_id, quantity, last_updated 
        FROM store_inventory WHERE store_id = ?
    """, (store_id,))
    rows = cursor.fetchall()
    return [{"product_id": r[0], "quantity": r[1], "last_updated": str(r[2])} for r in rows]

@router.post("/{store_id}")
def update_inventory(store_id: int, product_id: int, quantity: int):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        UPDATE store_inventory
        SET quantity = ?, last_updated = GETDATE()
        WHERE store_id = ? AND product_id = ?
    """, (quantity, store_id, product_id))
    db.commit()
    return {"message": "Inventory updated successfully"}
