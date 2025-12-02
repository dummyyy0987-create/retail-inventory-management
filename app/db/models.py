stores_table = """
CREATE TABLE stores (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(255),
    region VARCHAR(100),
    status VARCHAR(50)
);
"""

inventory_table = """
CREATE TABLE store_inventory (
    id INT IDENTITY PRIMARY KEY,
    store_id INT,
    product_id INT,
    quantity INT,
    last_updated DATETIME
);
"""
