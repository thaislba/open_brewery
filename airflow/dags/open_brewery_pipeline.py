import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id='open_brewery_pipeline',
    schedule='0 0 * * *',
    start_date=pendulum.datetime(2023, 6, 6, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=['open_brewery'],
) as dag:
	extraction = BashOperator(
    	task_id="data_extraction",
		bash_command=f"python3 /opt/scripts/extraction.py "
	)

	load = BashOperator(
		task_id="data_load",
		bash_command=f"python3 /opt/scripts/load.py "
	)

extraction >> load
