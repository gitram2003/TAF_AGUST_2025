
import json
from pyspark.sql.types import StructType
import os
from pyspark.sql.functions import explode_outer,col,ArrayType

def read_schema(dir_path):
    schema_path = os.path.join(dir_path,r'C:\Users\Devak\PycharmProjects\taf_agust\TAF_AGUST_2025\tests\table1\schema.json')      # append the data schema.json read StructType then it give to table1
    print('schema_path is :',schema_path)
    with open(schema_path,"r")as f:
        schema = StructType.fromJson(json.load(f))
    return schema

def read_sql(dir_path):
    query_path = os.path.join(dir_path,'transaction.sql')      # append the data schema.json read StructType then it give to table1
    print('query_path:',query_path)
    with open(query_path,"r")as f:
        query = f.read()
    return query


def flatten(df):  #df is table, schema is Y or N
    complex_field = dict([(field.name,field.dataType) for field in df.schema.fields
                    if type(field.dataType)==ArrayType or type(field.dataType)==StructType])
    while len(complex_field)!=0:
        col_name = list(complex_field.keys())[0]
        print("processing:"+col_name+"type:"+str(type(complex_field[col_name])))

        # if struct type then convert all the sub elements columns
        # that is flattened structs
        if type(complex_field[col_name])==StructType:
            expand = [col(col_name + '.' + k).alias(col_name+'_'+k) for k in
                      [n.name for n in complex_field[col_name]]]
            df = df.select("*",*expand).drop(col_name)

        #if ArrayType the add the array elements as row using the explodes function
        #that is Array explode
        elif type(complex_field[col_name])==ArrayType:
            df = df.withColumn(col_name,explode_outer(col_name))
        complex_field = dict([(field.name,field.dataType) for field in df.schema.fields
                             if type(field.dataType)== ArrayType or type(field.dataType)==StructType])

    return df