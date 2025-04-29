from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def dummy_function():
    print("Hello from Airflow DAG!")

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    dag_id='hello_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['example']
) as dag:
    task = PythonOperator(
        task_id='dummy_task',
        python_callable=dummy_function
    )
