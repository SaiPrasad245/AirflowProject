from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 5),
}

with DAG('snowflake_test_dag', default_args=default_args, schedule_interval=None) as dag:
    snowflake_query = SnowflakeOperator(
        task_id='run_query',
        snowflake_conn_id='snow_conn',
        sql='SELECT CURRENT_TIMESTAMP();'
    )
