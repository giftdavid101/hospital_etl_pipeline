from datetime import datetime

# from airflow import DAG
# from airflow.operators.python import PythonOperator
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

from scripts.clean_data import clean_hospital_data


def run_cleaning():
    clean_hospital_data(
        input_path="/opt/airflow/data/patients.csv",
        output_path="/opt/airflow/data/processed/hospital_analysis.csv"
    )


with DAG(
    dag_id="hospital_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["hospital", "data-engineering"],
) as dag:

    clean_hospital_data = BashOperator(
        task_id="clean_hospital_data",
        bash_command="python /opt/airflow/scripts/clean_data.py",
    )
