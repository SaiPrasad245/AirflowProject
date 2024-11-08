from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.operators.python import PythonOperator
from airflow import DAG
from airflow.utils.dates import days_ago

def run_snowflake_query(*args, **kwargs):
    from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
    
    # Initialize SnowflakeHook
    snowflake_hook = SnowflakeHook(snowflake_conn_id='snow_conn')
    
    # Execute query and fetch result
    result = snowflake_hook.get_first("SELECT CURRENT_TIMESTAMP();")
    
    # Log the result
    print(f"Query result: {result}")

# Define your DAG and task
with DAG(
    'snowflake_test_dag1',
    default_args={'retries': 1},
    schedule_interval=None,
    start_date=days_ago(1),
) as dag:
    
    run_query = PythonOperator(
        task_id='run_query',
        python_callable=run_snowflake_query,
    )

    run_query
