from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="test_git_sync_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["git", "test"],
) as dag:

    start = BashOperator(
        task_id="start_task",
        bash_command="echo 'Starting DAG execution...'"
    )

    middle = BashOperator(
        task_id="middle_task",
        bash_command="echo 'Middle of DAG.'"
    )

    end = BashOperator(
        task_id="end_task",
        bash_command="echo 'DAG completed.'"
    )

    start >> middle >> end
