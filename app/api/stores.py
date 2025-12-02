from fastapi import APIRouter
from db.connection import get_db

router = APIRouter(prefix="/stores")

@router.get("/")
def get_all_stores():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT store_id, store_name, region, status FROM stores")
    data = cursor.fetchall()
    return [{"store_id": row[0], "store_name": row[1], "region": row[2], "status": row[3]} for row in data]
