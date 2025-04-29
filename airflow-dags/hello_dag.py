from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging

default_args = {
    'start_date': datetime(2023, 1, 1),
}

def log_task(task_name):
    logging.info(f"🔥 Hello from task: {task_name}")
    print(f"✅ Task '{task_name}' completed.")

with DAG(
    dag_id='multi_task_logging_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['example']
) as dag:

    task1 = PythonOperator(
        task_id='log_step_1',
        python_callable=lambda: log_task('Step 1')
    )

    task2 = PythonOperator(
        task_id='log_step_2',
        python_callable=lambda: log_task('Step 2')
    )

    task3 = PythonOperator(
        task_id='log_step_3',
        python_callable=lambda: log_task('Step 3')
    )

    task1 >> task2 >> task3  # 순차 실행
