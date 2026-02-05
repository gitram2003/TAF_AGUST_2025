# read_db
import yaml
import os
from src.utility.general_lib import *

def read_db(config, spark, dir_path):
    import os, yaml

    # Path to credentials
    tests_path = os.path.dirname(dir_path)
    cred_file = os.path.join(tests_path, 'cred_file', 'cred_config.yml')
    print("cred_file_location:", cred_file)

    with open(cred_file, 'r') as file:
        creds = yaml.safe_load(file)[config['cred_lookup']] #convetrt to dict format
        print("credentials:", creds)

    # SQL Transformation ON
    if config['transaction'][0].lower() == "y":
        print("this is if condition(SQL transaction is on)")
        query = read_sql(dir_path = dir_path)
        df =(
            spark.read.format("jdbc")
            .option("url", creds['url'])
            .option("user", creds['user'])
            .option("password", creds['password'])
            .option("query", query)
            .option("driver", creds['driver'])
            .load())
        return df
    else:
        print("this is else condition(read full table)")
        df = (
            spark.read.format("jdbc")
            .option('url', creds['url'])
            .option('user', creds['user'])
            .option("password", creds['password'])
            .option("dbtable", config['table'])
            .option("driver", creds['driver'])
            .load()
        )
        return df
