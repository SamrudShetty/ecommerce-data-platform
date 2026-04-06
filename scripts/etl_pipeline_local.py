import pandas as pd
from sqlalchemy import create_engine

# ==============================
# FILE PATH
# ==============================
base_path = r"C:\Users\samru\Desktop\ecommerce-data-platform\data"

# ==============================
# DATABASE CONNECTION
# ==============================
engine = create_engine('postgresql://postgres:Samrud%40123@localhost:5432/ecommerce')
# ==============================
# DATASETS
# ==============================
datasets = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv"
}

# ==============================
# LOAD + PUSH TO DB
# ==============================
for table, file in datasets.items():
    file_path = f"{base_path}\\{file}"
    
    print(f"Loading {file}...")
    df = pd.read_csv(file_path)
    
    print(f"Pushing {table} to PostgreSQL...")
    df.to_sql(table, engine, if_exists='replace', index=False)

    print(f"{table} done ✅\n")

print("🚀 ALL DATA LOADED SUCCESSFULLY")