import time
from db.connection import get_db

def sync_inventory():
    """
    Syncs inventory data from warehouse to stores.
    This is triggered every 10 minutes to ensure stock levels are up-to-date.
    """
    while True:
        db = get_db()
        print("Syncing inventory from warehouse to stores...")
        
        # Dummy logic for syncing: just an example
        cursor = db.cursor()
        cursor.execute("SELECT store_id, product_id, quantity FROM warehouse_inventory")
        warehouse_data = cursor.fetchall()

        for store_id, product_id, quantity in warehouse_data:
            # Update each store's inventory
            cursor.execute("""
                INSERT INTO store_inventory (store_id, product_id, quantity, last_updated)
                VALUES (?, ?, ?, GETDATE())
                ON DUPLICATE KEY UPDATE quantity = ?, last_updated = GETDATE()
            """, (store_id, product_id, quantity, quantity))
        
        db.commit()
        time.sleep(600)  # Sleep for 10 minutes before syncing again
