from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Felipe Allegretti',
    'start_date': days_ago(0),
    'email': ['felipe@allegretti.me'],
}

dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='Process Web Log',
    schedule_interval=timedelta(days=1),
)

extract_data = BashOperator(
    task_id='extract_data',
    bash_command='cut -f1 -d" " $AIRFLOW_HOME/dags/capstone/accesslog.txt > $AIRFLOW_HOME/dags/capstone/extracted-data.txt',
    dag=dag,
)

transform_data = BashOperator(
    task_id='transform_data',
    bash_command='grep -v ' + '\'^198\.46\.149\.143\'' + ' $AIRFLOW_HOME/dags/capstone/extracted-data.txt > $AIRFLOW_HOME/dags/capstone/transformed-data.csv',
    dag=dag,
)

load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -czvf $AIRFLOW_HOME/dags/capstone/weblog.tar.gz $AIRFLOW_HOME/dags/capstone/transformed-data.csv',
    dag=dag,
)

extract_data >> transform_data >> load_data