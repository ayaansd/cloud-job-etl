
# NOTE: This is a DAG skeleton illustrating tasks and BigQuery ops usage.
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def extract_to_gcs(**context):
    print("Download CSV to GCS bucket...")

def bq_load_raw(**context):
    print("Load into BigQuery raw table...")

def bq_run_transforms(**context):
    print("Run 40+ SQL transforms in BigQuery...")

with DAG("cloud_job_etl", start_date=datetime(2024,1,1), schedule="@daily", catchup=False) as dag:
    t1 = PythonOperator(task_id="extract_to_gcs", python_callable=extract_to_gcs)
    t2 = PythonOperator(task_id="bq_load_raw", python_callable=bq_load_raw)
    t3 = PythonOperator(task_id="bq_run_transforms", python_callable=bq_run_transforms)
    t1 >> t2 >> t3
