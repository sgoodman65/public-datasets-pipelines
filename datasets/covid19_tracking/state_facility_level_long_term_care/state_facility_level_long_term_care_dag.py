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
from airflow.contrib.operators import gcs_to_bq, gcs_to_gcs
from airflow.operators import bash_operator

default_args = {
    "owner": "Google",
    "depends_on_past": False,
    "start_date": "2021-03-01",
}


with DAG(
    dag_id="covid19_tracking.state_facility_level_long_term_care",
    default_args=default_args,
    max_active_runs=1,
    schedule_interval="@once",
    catchup=False,
    default_view="graph",
) as dag:

    # Task to copy data from HTTP source to GCS or Airflow home dir
    download_raw_csv_files = bash_operator.BashOperator(
        task_id="download_raw_csv_files",
        env={
            "airflow_home": "{{ var.json.shared.airflow_home }}",
            "dataset": "covid19_tracking",
            "pipeline": "state_facility_level_long_term_care",
        },
        bash_command="mkdir -p $airflow_home/data/$dataset/$pipeline\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-ar.csv -L https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_ar.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-ga.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_ga.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-in.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_in.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-il.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_il.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-ks.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_ks.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-sc.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_sc.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-hi.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_hi.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-ny.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_ny.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-ok.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_ok.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-nm.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_nm.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-wy.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_wy.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-oh.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_oh.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-md.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_md.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-ms.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_ms.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-co.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_co.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-la.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_la.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-me.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_me.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-ar.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_ar.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-nj.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_nj.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-va.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_va.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-ca.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_ca.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-nd.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_nd.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-ct.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_ct.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-vt.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_vt.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-mi.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_mi.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-or.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_or.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-tx.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_tx.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-tn.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_tn.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-mn.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_mn.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-wv.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_wv.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-nc.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_nc.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-ia.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_ia.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-fl.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_fl.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-ri.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_ri.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-pa.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_pa.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-de.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_de.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-ky.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_ky.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-dc.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_dc.csv\ncurl -o $airflow_home/data/$dataset/$pipeline/raw-facilities-id.csv https://github.com/COVID19Tracking/long-term-care-data/raw/master/facilities_id.csv\n",
    )

    # Run the custom/csv_transform.py script to process the raw CSV contents into a BigQuery friendly format
    process_raw_csv_files = bash_operator.BashOperator(
        task_id="process_raw_csv_files",
        bash_command="WORKING_DIR=$airflow_home/data/covid19_tracking/state_facility_level_long_term_care python $airflow_home/dags/$dataset/$pipeline/custom/multi_csv_transform.py\n",
        env={
            "airflow_home": "{{ var.json.shared.airflow_home }}",
            "dataset": "covid19_tracking",
            "pipeline": "state_facility_level_long_term_care",
        },
    )

    # Task to load the CSV from the pipeline's data folder to BigQuery
    load_csv_files_to_bq_table = gcs_to_bq.GoogleCloudStorageToBigQueryOperator(
        task_id="load_csv_files_to_bq_table",
        bucket="{{ var.json.shared.composer_bucket }}",
        source_objects=[
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-ar.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-ga.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-in.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-il.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-ks.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-sc.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-hi.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-ny.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-ok.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-nm.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-wy.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-oh.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-md.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-ms.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-co.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-la.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-me.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-ar.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-nj.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-va.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-ca.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-nd.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-ct.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-vt.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-mi.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-or.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-tx.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-tn.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-mn.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-wv.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-nc.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-ia.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-fl.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-ri.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-pa.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-de.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-ky.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-dc.csv",
            "data/covid19_tracking/state_facility_level_long_term_care/facilities-id.csv",
        ],
        source_format="CSV",
        destination_project_dataset_table="covid19_tracking.state_facility_level_long_term_care",
        skip_leading_rows=1,
        write_disposition="WRITE_TRUNCATE",
        schema_fields=[
            {
                "name": "date",
                "type": "DATE",
                "mode": "REQUIRED",
                "description": "Date of the observations",
            },
            {
                "name": "state",
                "type": "STRING",
                "mode": "REQUIRED",
                "description": "2-letter postal abbreviation for the state",
            },
            {
                "name": "county",
                "type": "STRING",
                "mode": "NULLABLE",
                "description": "The name of the county in uppercase letters",
            },
            {
                "name": "city",
                "type": "STRING",
                "mode": "NULLABLE",
                "description": "The name of the city in uppercase letters",
            },
            {
                "name": "facility_name",
                "type": "STRING",
                "mode": "REQUIRED",
                "description": "The facility name in uppercase letters",
            },
            {"name": "facility_type_state", "type": "STRING", "mode": "NULLABLE"},
            {"name": "ctp_facility_category", "type": "STRING", "mode": "NULLABLE"},
            {"name": "state_fed_regulated", "type": "STRING", "mode": "NULLABLE"},
            {"name": "state_facility_id", "type": "STRING", "mode": "NULLABLE"},
            {"name": "facility_cms_id", "type": "STRING", "mode": "NULLABLE"},
            {"name": "date_outbreak_opened", "type": "STRING", "mode": "NULLABLE"},
            {"name": "date_outbreak_closed", "type": "STRING", "mode": "NULLABLE"},
            {"name": "outbreak_status", "type": "STRING", "mode": "NULLABLE"},
            {"name": "resident_census", "type": "STRING", "mode": "NULLABLE"},
            {"name": "resident_positives", "type": "STRING", "mode": "NULLABLE"},
            {"name": "resident_probable", "type": "STRING", "mode": "NULLABLE"},
            {"name": "resident_deaths", "type": "STRING", "mode": "NULLABLE"},
            {"name": "resident_probable_deaths", "type": "STRING", "mode": "NULLABLE"},
            {"name": "staff_positive", "type": "STRING", "mode": "NULLABLE"},
            {"name": "staff_probable", "type": "STRING", "mode": "NULLABLE"},
            {"name": "staff_deaths", "type": "STRING", "mode": "NULLABLE"},
            {"name": "staff_probable_deaths", "type": "STRING", "mode": "NULLABLE"},
            {"name": "resident_staff_positives", "type": "STRING", "mode": "NULLABLE"},
            {
                "name": "resident_staff_probable_positives",
                "type": "STRING",
                "mode": "NULLABLE",
            },
            {"name": "resident_staff_deaths", "type": "STRING", "mode": "NULLABLE"},
            {
                "name": "resident_staff_probable_deaths",
                "type": "STRING",
                "mode": "NULLABLE",
            },
            {
                "name": "outbreak_resident_positives",
                "type": "STRING",
                "mode": "NULLABLE",
            },
            {
                "name": "outbreak_resident_probable",
                "type": "STRING",
                "mode": "NULLABLE",
            },
            {"name": "outbreak_resident_deaths", "type": "STRING", "mode": "NULLABLE"},
            {
                "name": "outbreak_resident_probable_deaths",
                "type": "STRING",
                "mode": "NULLABLE",
            },
            {"name": "outbreak_staff_positive", "type": "STRING", "mode": "NULLABLE"},
            {"name": "outbreak_staff_probable", "type": "STRING", "mode": "NULLABLE"},
            {"name": "outbreak_staff_deaths", "type": "STRING", "mode": "NULLABLE"},
            {
                "name": "outbreak_staff_probable_deaths",
                "type": "STRING",
                "mode": "NULLABLE",
            },
            {
                "name": "outbreak_resident_staff_positives",
                "type": "STRING",
                "mode": "NULLABLE",
            },
            {
                "name": "outbreak_resident_staff_probable_positives",
                "type": "STRING",
                "mode": "NULLABLE",
            },
            {
                "name": "outbreak_resident_staff_deaths",
                "type": "STRING",
                "mode": "NULLABLE",
            },
            {
                "name": "outbreak_resident_staff_probable_deaths",
                "type": "STRING",
                "mode": "NULLABLE",
            },
            {"name": "outbreak_residents_tested", "type": "STRING", "mode": "NULLABLE"},
            {"name": "staff_tested", "type": "STRING", "mode": "NULLABLE"},
            {
                "name": "personal_protective_equipment",
                "type": "STRING",
                "mode": "NULLABLE",
            },
        ],
    )

    # Task to archive the CSV file in the destination bucket
    archive_csv_files_to_destination_bucket = gcs_to_gcs.GoogleCloudStorageToGoogleCloudStorageOperator(
        task_id="archive_csv_files_to_destination_bucket",
        source_bucket="{{ var.json.shared.composer_bucket }}",
        source_object="data/covid19_tracking/state_facility_level_long_term_care/*",
        destination_bucket="{{ var.json.covid19_tracking.destination_bucket }}",
        destination_object="datasets/covid19_tracking/state_facility_level_long_term_care/{{ ds }}/",
        move_object=True,
    )

    download_raw_csv_files >> process_raw_csv_files
    process_raw_csv_files >> load_csv_files_to_bq_table
    load_csv_files_to_bq_table >> archive_csv_files_to_destination_bucket
