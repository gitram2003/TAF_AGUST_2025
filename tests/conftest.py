#conftest.py
import sys
import os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

import pytest
from pyspark.sql import SparkSession
import yaml
from src.utility.read_file_lib import *
from src.utility.general_lib import *
from src.utility.read_db_lib import *


@pytest.fixture(scope='session')
def spark_session():
    print("This is spark session")

    taf_agust = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("taf_agust", taf_agust)
    #sql server jar_path
    jar_path = os.path.join(taf_agust,"jars_file","mssql-jdbc-12.2.1.jre11.jar")
    print("jar_azure", jar_path)
    #
    # #postgresql jar path
    # postgres_path = os.path.join(taf_agust,"jars_file","mssql-jdbc-12.2.1.jar")
    # print("postgres_path",postgres_path)
    # jars_path = ss_path+','+postgres_path

    #jar_path = 'file:/C:/Users/Devak/PycharmProjects/taf_agust/TAF_AGUST_2025/jars_file/mssql-jdbc-12.2.1.jre11.jar'

    spark = (SparkSession.builder \
        .master('local[1]')
        .config("spark.jars",jar_path) \
        .config('spark.driver.extraClassPath',jar_path) \
        .config('spark.excutor.extraClassPath',jar_path)
        .appName("taf_agust")
        .getOrCreate())
    return spark

@pytest.fixture(scope='module')
def read_config(request):
    dir_path = request.node.fspath.dirname
    conf_path = os.path.join(dir_path, 'config.yml')
    with open(conf_path, 'r') as f:
        config_data = yaml.safe_load(f)
    return config_data

@pytest.fixture(scope='module')
def read_data(spark_session,read_config,request):
    spark = spark_session
    config = read_config
    #table1 or table2 ect... path read
    dir_path =request.node.fspath.dirname
    print(f"dir_path {dir_path}")

    # print("spark", spark)
    # print("config", config)
    #
    # print("="*50)

    source_data = config['source']
    # print("source_path", source_data)
    # print('='*50)

    target_data= config['target']
    #print("target_path", target_data)

    validation_config = config['validations']

    # print('source_path is' ,source_data['path'])
    # print('target_path is',target_data['path'])

    if source_data['type'] == 'database':
        source_df = read_db(config = source_data,spark=spark , dir_path=dir_path)
    else:
        #read table1 or table2 path read and go to read_data
        source_df = read_file(config=source_data,spark = spark,dir_path=dir_path)
        print(source_df)

    if target_data['type'] == 'database':
        target_df = read_db(config = target_data,spark =  spark,dir_path=dir_path)
    else:
        #this is load local file dir_path
        target_df = read_file(config=target_data,spark=spark,dir_path=dir_path)
        print(target_df)

    return source_df.drop(*source_data['exclude_cols']),target_df.drop(*target_data['exclude_cols']),validation_config

