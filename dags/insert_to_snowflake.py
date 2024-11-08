from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.operators.python import PythonOperator
from airflow import DAG
from airflow.utils.dates import days_ago

# Define your DAG and task
with DAG(
    'snowflake_test_dag2',
    default_args={'retries': 1},
    schedule_interval=None,
    start_date=days_ago(1),
) as dag:
    
   run_insert_query = SnowflakeOperator(
    task_id="run_insert_query",
    sql="INSERT INTO test_table  (test_time_stamp) SELECT CURRENT_TIMESTAMP();",
    snowflake_conn_id="snow_conn",
    autocommit=True
    )

run_insert_query
