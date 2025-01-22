from datetime import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from twitter_etl import fetch_user_tweets

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='A simple twitter DAG',
    schedule_interval=timedelta(days=1)
)

# Task 1
fetch_tweets = PythonOperator(
    task_id='fetch_tweets',
    python_callable=fetch_user_tweets,
    op_args=['elonmusk', 'your-bucket-name'],
    dag=dag
)

fetch_tweets