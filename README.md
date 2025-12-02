# Retail Inventory Management Service

This is a FastAPI-based service for managing retail store inventory. The service includes:
- API endpoints for fetching and updating inventory.
- Synchronization of inventory data from warehouse to stores every 10 minutes.
- Connection to an Azure SQL Database to store inventory and store details.

## Setup

1. Clone the repository.
2. Create a `.env` file with your Azure SQL database credentials:
    ```
    DB_SERVER=yourserver.database.windows.net
    DB_NAME=RetailDB
    DB_USER=dbadmin
    DB_PASSWORD=YourPassword123
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run the FastAPI app:
    ```
    uvicorn app.main:app --reload
    ```

## API Endpoints

- `GET /stores/` - Fetch all stores
- `GET /inventory/{store_id}` - Get inventory details for a specific store
- `POST /inventory/{store_id}` - Update inventory for a store
