from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
'uber_pipeline',
start_date=datetime(
2025,1,1),
schedule='@daily',
catchup=False
) as dag:

    ingest=BashOperator(
      task_id='ingest',
      bash_command='spark-submit spark/ingest.py'
    )

    transform=BashOperator(
      task_id='transform',
      bash_command='spark-submit spark/transform.py'
    )

    analytics=BashOperator(
      task_id='analytics',
      bash_command='spark-submit spark/analytics.py'
    )

ingest>>transform>>analytics
