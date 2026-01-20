# read_db
import yaml
import os
from src.utility.general_lib import *
#
def read_db(config,spark,dir_path):
    test_path = os.path.dirname(dir_path)
    cred_file = os.path.join(test_path,'cred_file','cred_config.yml')
    print("cred_file_location",cred_file)
    with open(cred_file,'r') as file:
        creds = yaml.safe_load(file)[config['cred_lookup']]
        print("credentials",creds)
    if ['transformation'][0].lower() == "y":
        query = read_sql(dir_path)
        df = (spark.read.format("jdbc")
              .option('url',creds['url'])
              .option('user',creds['user'])
              .option("password",creds['password'])
              .option("query",query)
              #.option("dbtable",config['table'])
              .option("driver",creds['driver'])
              .load())

    else:
        df = (spark.read.format("jdbc")
              .option('url', creds['url'])
              .option('user', creds['user'])
              .option("password", creds['password'])
              .option("dbtable",config['table'])
              .option("driver", creds['driver'])
              .load())

    return df


