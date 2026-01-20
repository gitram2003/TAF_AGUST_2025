from src.utility.general_lib import *
from schema_prep import *

def read_file(config,spark,dir_path):  #once config dir_path done coming to read_data fun
    path = config['path']
    types = config['type']
    schema= config['schema']
    options = config['options']


    if types == 'csv':
        if schema == 'Y':  # you give N then directly pass to else block
            schema_json = read_schema(dir_path) #after read_data to check path of dir_path and go to read_schema in general_lib fun
            df = spark.read.schema(schema_json).csv(path,header = True,sep = options['delimiter'])
        else:
            df = spark.read.csv(path, header =options['header'],sep= options['delimiter'],inferSchema = options['inferSchema'])

    elif types == 'json':
        df = spark.read.json(path=path,multiLine=options['multiline'])
        if options['flatten'] == 'Y':
            df = flatten(df)

    elif types == 'parquet':
        df = spark.read.parquet(path)

    elif types == 'avro':
        df = spark.read.format('avro').load(path)

    elif types == 'txt':
        df = spark.read.csv(path = path, header =options['header'],sep= options['delimiter'],inferSchema = options['inferSchema'])
    return df

