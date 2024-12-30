import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from _2k6socvpprzo1acwwr_vcg_.tasks import Model_0_1
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "2K6socvPPrZO1ACwWr_VCg_", 
    schedule_interval = None, 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "7MBClQP5"}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2024, 12, 27, tz = "UTC"), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    Model_0_1_op = Model_0_1()
