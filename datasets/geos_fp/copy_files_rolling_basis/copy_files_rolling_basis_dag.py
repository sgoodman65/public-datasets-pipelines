# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from airflow import DAG
from airflow.contrib.operators import gcs_delete_operator, kubernetes_pod_operator

default_args = {
    "owner": "Google",
    "depends_on_past": False,
    "start_date": "2021-06-01",
}


with DAG(
    dag_id="geos_fp.copy_files_rolling_basis",
    default_args=default_args,
    max_active_runs=1,
    schedule_interval="0 2 * * *",
    catchup=False,
    default_view="graph",
) as dag:

    # Copy files to GCS on the specified date
    copy_files_dated_today = kubernetes_pod_operator.KubernetesPodOperator(
        task_id="copy_files_dated_today",
        name="geosfp",
        namespace="default",
        image="{{ var.json.geos_fp.container_registry.rolling_copy }}",
        image_pull_policy="Always",
        env_vars={
            "BASE_URL": "https://portal.nccs.nasa.gov/datashare/gmao/geos-fp/das",
            "TODAY_DIFF": "0",
            "DOWNLOAD_DIR": "/geos_fp/data",
            "TARGET_BUCKET": "{{ var.json.geos_fp.destination_bucket }}",
            "BATCH_SIZE": "10",
        },
        resources={"request_memory": "1G", "request_cpu": "1"},
        retries=3,
        retry_delay=300,
        retry_exponential_backoff=True,
        startup_timeout_seconds=600,
    )

    # Copy files to GCS on the specified date
    copy_files_dated_today_minus_1_day = kubernetes_pod_operator.KubernetesPodOperator(
        task_id="copy_files_dated_today_minus_1_day",
        name="geosfp",
        namespace="default",
        image="{{ var.json.geos_fp.container_registry.rolling_copy }}",
        image_pull_policy="Always",
        env_vars={
            "BASE_URL": "https://portal.nccs.nasa.gov/datashare/gmao/geos-fp/das",
            "TODAY_DIFF": "1",
            "DOWNLOAD_DIR": "/geos_fp/data",
            "TARGET_BUCKET": "{{ var.json.geos_fp.destination_bucket }}",
            "BATCH_SIZE": "10",
        },
        resources={"request_memory": "1G", "request_cpu": "1"},
        retries=3,
        retry_delay=300,
        retry_exponential_backoff=True,
        startup_timeout_seconds=600,
    )

    # Copy files to GCS on the specified date
    copy_files_dated_today_minus_2_days = kubernetes_pod_operator.KubernetesPodOperator(
        task_id="copy_files_dated_today_minus_2_days",
        name="geosfp",
        namespace="default",
        image="{{ var.json.geos_fp.container_registry.rolling_copy }}",
        image_pull_policy="Always",
        env_vars={
            "BASE_URL": "https://portal.nccs.nasa.gov/datashare/gmao/geos-fp/das",
            "TODAY_DIFF": "2",
            "DOWNLOAD_DIR": "/geos_fp/data",
            "TARGET_BUCKET": "{{ var.json.geos_fp.destination_bucket }}",
            "BATCH_SIZE": "10",
        },
        resources={"request_memory": "1G", "request_cpu": "1"},
        retries=3,
        retry_delay=300,
        retry_exponential_backoff=True,
        startup_timeout_seconds=600,
    )

    # Copy files to GCS on a 10-day rolling basis
    copy_files_dated_today_minus_3_days = kubernetes_pod_operator.KubernetesPodOperator(
        task_id="copy_files_dated_today_minus_3_days",
        name="geosfp",
        namespace="default",
        image="{{ var.json.geos_fp.container_registry.rolling_copy }}",
        image_pull_policy="Always",
        env_vars={
            "BASE_URL": "https://portal.nccs.nasa.gov/datashare/gmao/geos-fp/das",
            "TODAY_DIFF": "3",
            "DOWNLOAD_DIR": "/geos_fp/data",
            "TARGET_BUCKET": "{{ var.json.geos_fp.destination_bucket }}",
            "BATCH_SIZE": "10",
        },
        resources={"request_memory": "1G", "request_cpu": "1"},
        retries=3,
        retry_delay=300,
        retry_exponential_backoff=True,
        startup_timeout_seconds=600,
    )

    # Copy files to GCS on a 10-day rolling basis
    copy_files_dated_today_minus_4_days = kubernetes_pod_operator.KubernetesPodOperator(
        task_id="copy_files_dated_today_minus_4_days",
        name="geosfp",
        namespace="default",
        image="{{ var.json.geos_fp.container_registry.rolling_copy }}",
        image_pull_policy="Always",
        env_vars={
            "BASE_URL": "https://portal.nccs.nasa.gov/datashare/gmao/geos-fp/das",
            "TODAY_DIFF": "4",
            "DOWNLOAD_DIR": "/geos_fp/data",
            "TARGET_BUCKET": "{{ var.json.geos_fp.destination_bucket }}",
            "BATCH_SIZE": "10",
        },
        resources={"request_memory": "1G", "request_cpu": "1"},
        retries=3,
        retry_delay=300,
        retry_exponential_backoff=True,
        startup_timeout_seconds=600,
    )

    # Copy files to GCS on a 10-day rolling basis
    copy_files_dated_today_minus_5_days = kubernetes_pod_operator.KubernetesPodOperator(
        task_id="copy_files_dated_today_minus_5_days",
        name="geosfp",
        namespace="default",
        image="{{ var.json.geos_fp.container_registry.rolling_copy }}",
        image_pull_policy="Always",
        env_vars={
            "BASE_URL": "https://portal.nccs.nasa.gov/datashare/gmao/geos-fp/das",
            "TODAY_DIFF": "5",
            "DOWNLOAD_DIR": "/geos_fp/data",
            "TARGET_BUCKET": "{{ var.json.geos_fp.destination_bucket }}",
            "BATCH_SIZE": "10",
        },
        resources={"request_memory": "1G", "request_cpu": "1"},
        retries=3,
        retry_delay=300,
        retry_exponential_backoff=True,
        startup_timeout_seconds=600,
    )

    # Copy files to GCS on a 10-day rolling basis
    copy_files_dated_today_minus_6_days = kubernetes_pod_operator.KubernetesPodOperator(
        task_id="copy_files_dated_today_minus_6_days",
        name="geosfp",
        namespace="default",
        image="{{ var.json.geos_fp.container_registry.rolling_copy }}",
        image_pull_policy="Always",
        env_vars={
            "BASE_URL": "https://portal.nccs.nasa.gov/datashare/gmao/geos-fp/das",
            "TODAY_DIFF": "6",
            "DOWNLOAD_DIR": "/geos_fp/data",
            "TARGET_BUCKET": "{{ var.json.geos_fp.destination_bucket }}",
            "BATCH_SIZE": "10",
        },
        resources={"request_memory": "1G", "request_cpu": "1"},
        retries=3,
        retry_delay=300,
        retry_exponential_backoff=True,
        startup_timeout_seconds=600,
    )

    # Copy files to GCS on a 10-day rolling basis
    copy_files_dated_today_minus_7_days = kubernetes_pod_operator.KubernetesPodOperator(
        task_id="copy_files_dated_today_minus_7_days",
        name="geosfp",
        namespace="default",
        image="{{ var.json.geos_fp.container_registry.rolling_copy }}",
        image_pull_policy="Always",
        env_vars={
            "BASE_URL": "https://portal.nccs.nasa.gov/datashare/gmao/geos-fp/das",
            "TODAY_DIFF": "7",
            "DOWNLOAD_DIR": "/geos_fp/data",
            "TARGET_BUCKET": "{{ var.json.geos_fp.destination_bucket }}",
            "BATCH_SIZE": "10",
        },
        resources={"request_memory": "1G", "request_cpu": "1"},
        retries=3,
        retry_delay=300,
        retry_exponential_backoff=True,
        startup_timeout_seconds=600,
    )

    # Deletes GCS data more than 7 days ago
    delete_old_data = gcs_delete_operator.GoogleCloudStorageDeleteOperator(
        task_id="delete_old_data",
        bucket_name="{{ var.json.geos_fp.destination_bucket }}",
        prefix="{{ macros.ds_format(macros.ds_add(ds, -8), \u0027%Y-%m-%d\u0027, \u0027Y%Y/M%m/D%d\u0027) }}",
    )

    delete_old_data
    copy_files_dated_today
    copy_files_dated_today_minus_1_day
    copy_files_dated_today_minus_2_days
    copy_files_dated_today_minus_3_days
    copy_files_dated_today_minus_4_days
    copy_files_dated_today_minus_5_days
    copy_files_dated_today_minus_6_days
    copy_files_dated_today_minus_7_days
