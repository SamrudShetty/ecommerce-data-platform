from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def run_etl():
    os.system("python /opt/airflow/scripts/etl_pipeline.py")

with DAG(
    dag_id='ecommerce_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id='run_etl_pipeline',
        python_callable=run_etl
    )