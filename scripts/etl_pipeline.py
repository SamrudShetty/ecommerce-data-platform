# ==============================
# IMPORTS (ALWAYS FIRST)
# ==============================
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# ==============================
# LOAD ENV VARIABLES
# ==============================
load_dotenv()

# ==============================
# FILE PATH (ROBUST)
# ==============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_path = os.path.join(BASE_DIR, "data")

print("📁 Base Directory:", BASE_DIR)
print("📂 Data Path:", base_path)

# Check if data folder exists
if not os.path.exists(base_path):
    raise Exception(f"❌ Data folder not found at: {base_path}")

print("📄 Files inside data folder:", os.listdir(base_path))

# ==============================
# DATABASE CONFIG
# ==============================
DB_USER = "postgres"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ecommerce"

# ==============================
# CREATE DB ENGINE
# ==============================
engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
print("DB Password from env:", DB_PASSWORD)

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
# HELPER: CHECK IF TABLE EXISTS
# ==============================
def table_exists(table_name):
    query = f"""
    SELECT EXISTS (
        SELECT FROM information_schema.tables 
        WHERE table_name = '{table_name}'
    );
    """
    return pd.read_sql(query, engine).iloc[0, 0]

# ==============================
# HELPER: GET MAX DATE
# ==============================
def get_max_date(table, column):
    try:
        query = f"SELECT MAX({column}) FROM {table}"
        result = pd.read_sql(query, engine).iloc[0, 0]
        return result
    except:
        return None

# ==============================
# DATE COLUMN MAPPING
# ==============================
date_columns = {
    "orders": "order_purchase_timestamp",
    "order_items": "shipping_limit_date",
    "payments": None,
    "customers": None,
    "products": None,
    "sellers": None
}

# ==============================
# MAIN ETL LOOP
# ==============================
for table, file in datasets.items():

    file_path = os.path.join(base_path, file)

    print(f"\n📥 Loading {file}...")

    # Check file exists
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        continue

    df = pd.read_csv(file_path)

    date_col = date_columns.get(table)

    # Convert to datetime if applicable
    if date_col and date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col])

    # ==============================
    # LOAD LOGIC
    # ==============================
    exists = table_exists(table)

    if not exists:
        print(f"🆕 First load for {table} (FULL LOAD)")
        df.to_sql(table, engine, if_exists='replace', index=False)

    else:
        print(f"🔄 Incremental load for {table}")

        if date_col:
            last_date = get_max_date(table, date_col)

            if last_date:
                df = df[df[date_col] > last_date]
                print(f"📊 New rows to insert: {len(df)}")

        if not df.empty:
            df.to_sql(table, engine, if_exists='append', index=False)
            print(f"✅ {table} updated")
        else:
            print(f"⚠️ No new data for {table}")

print("\n🚀 ALL DATA LOADED SUCCESSFULLY")