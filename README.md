# 📊 E-Commerce Data Platform

## 🚀 Project Overview
This project demonstrates an end-to-end data pipeline that transforms raw e-commerce data into actionable business insights.

It simulates a real-world data workflow including:
- Data ingestion (CSV files)
- Data transformation (Python & SQL)
- Data warehousing (PostgreSQL - Star Schema)
- Business intelligence (Power BI Dashboard)

---

## 🧱 Architecture

Raw Data (CSV)  
⬇  
Python ETL Pipeline  
⬇  
PostgreSQL Database  
⬇  
SQL Data Warehouse (Fact & Dimension Tables)  
⬇  
Power BI Dashboard  

---

## ⚙️ Tech Stack

- Python (Pandas, SQLAlchemy)
- PostgreSQL
- Power BI
- SQL
- Git & GitHub

---
---

## 📂 Project Structure

ecommerce-data-platform/
│
├── scripts/ # ETL pipeline
├── sql/ # Warehouse SQL scripts
├── dashboard/ # Power BI dashboard
├── data/ # Raw data (excluded from GitHub)
├── requirements.txt
└── README.md


---

## 🔄 ETL Pipeline

The ETL pipeline:
- Reads raw CSV files
- Loads data into PostgreSQL tables
- Automates table creation and data ingestion

Run:
python scripts/etl_pipeline.py


---

## 🧠 Data Modeling

Implemented a **Star Schema**:

- Fact Table:
  - fact_sales

- Dimension Tables:
  - dim_customers
  - dim_products

---

## 📊 Dashboard

### Key Insights:
- São Paulo contributes ~40% of total revenue
- Revenue is concentrated in top product categories
- Average Order Value (~205) indicates mid-range purchasing
- Repeat Rate (~12%) highlights low customer retention
- Profit margin (~30%) shows healthy profitability

---

## 🖼️ Dashboard Preview

(Add screenshot here)

---

## 🔐 Environment Setup

Create a `.env` file:
DB_PASSWORD=your_password


---

## 📦 Installation
pip install -r requirements.txt

---

## 📌 Dataset

Dataset sourced from:
Brazilian E-Commerce Public Dataset (Olist) - Kaggle

---

## 🎯 Key Learnings

- End-to-end data pipeline development
- Data warehouse modeling
- Business intelligence dashboarding
- Data-driven decision making

---

## 👤 Author
Samrud Shetty