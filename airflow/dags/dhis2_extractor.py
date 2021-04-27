from datetime import timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.utils.dates import days_ago
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)

# Will be passed to all KubernetesPodOperator tasks
k8s_kwargs = {
    "image": "blsq/dhis2_extractor:0.1.1",
    "image_pull_policy": "Always",
    "namespace": "default",
    "is_delete_operator_pod": True,
    "get_logs": True,
}
cloud_storage_env_variables = {
    "AWS_ACCESS_KEY_ID": Variable.get("dhis2_extractor_aws_access_key_id"),
    "AWS_SECRET_ACCESS_KEY": Variable.get("dhis2_extractor_aws_secret_access_key"),
    "AWS_REGION": Variable.get("dhis2_extractor_aws_region"),
}

dag = DAG(
    "dhis2_extractor",
    default_args={
        "owner": "Airflow",
        "depends_on_past": False,
        "start_date": days_ago(0),
        "catchup": False,
        "email": ["pvanliefland@bluesquarehub.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "email_on_success": False,
        "retries": 0,
        "retry_delay": timedelta(minutes=5),
    },
    schedule_interval="0 3 1 * *",
    max_active_runs=10,
    concurrency=10,
)

# Download the Docker image (not necessary but illustrates task dependencies)
download_image = KubernetesPodOperator(
    **k8s_kwargs,
    cmds=["echo"],
    arguments=[
        '"Image downloaded!"',
    ],
    task_id="dhis2_extractor_download_image",
    name="dhis2_extractor_download_image",
    dag=dag,
)

# Launch the extraction itself
extract = KubernetesPodOperator(
    **k8s_kwargs,
    cmds=["python", "-m", "dhis2_extractor.cli"],
    arguments=[
        "extract",
        "{{ dag_run.conf['api_url'] }}",
        "--username={{ dag_run.conf['username'] }}",
        "--password={{ dag_run.conf['password'] }}",
        "--output-format=csv",
        "--output-path={{ dag_run.conf['output_path'] }}",
    ],
    env_vars=cloud_storage_env_variables,
    task_id="dhis2_extractor_extract",
    name="dhis2_extractor_extract",
    dag=dag,
)

# "Build" the DAG by specifying the dependencies between tasks
download_image >> extract
