import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

# Azure SQL Database connection details
DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Connection string
connection_string = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={DB_SERVER};"
    f"DATABASE={DB_NAME};"
    f"UID={DB_USER};"
    f"PWD={DB_PASSWORD};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
    f"Connection Timeout=30;"
)

db_connection = None

def get_db():
    """
    Returns a live DB connection. Reconnects automatically if connection is closed.
    """
    global db_connection

    try:
        if db_connection is None or not is_connection_alive(db_connection):
            db_connection = pyodbc.connect(connection_string)
        return db_connection

    except Exception as e:
        print(f"Error connecting to database: {e}")
        db_connection = pyodbc.connect(connection_string)
        return db_connection

def is_connection_alive(connection):
    """Returns True if the connection is valid and alive."""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        return True
    except:
        return False
