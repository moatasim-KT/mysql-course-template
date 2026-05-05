import mysql.connector
import pandas as pd
import os
import glob

# Database configuration from environment variables
DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", "password"),
    "database": os.environ.get("DB_NAME", "employees_db")
}

def load_data():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # Define mapping of filename to table name
    files_to_tables = {
        'employees.csv': 'employees',
        'customers.csv': 'customers',
        'orders.csv': 'orders',
        'products.csv': 'products',
        'order_items.csv': 'order_items',
        'performance_reviews.csv': 'performance_reviews'
    }

    data_dir = os.path.join(os.getcwd(), 'data')
    
    # Process files based on mapping
    for filename, table in files_to_tables.items():
        filepath = os.path.join(data_dir, filename)
        if os.path.exists(filepath):
            print(f"Loading {filename} into {table}...")
            df = pd.read_csv(filepath)
            
            # Simple insertion logic
            for _, row in df.iterrows():
                columns = ", ".join(row.index)
                placeholders = ", ".join(["%s"] * len(row))
                sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
                cursor.execute(sql, tuple(row))
    
    conn.commit()
    cursor.close()
    conn.close()
    print("All data loaded successfully.")

if __name__ == "__main__":
    load_data()
