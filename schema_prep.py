from pyspark.sql import SparkSession
import json
from pyspark.sql.types import StructType


spark = (SparkSession.builder.master("local[1]").appName("automation FW").getOrCreate())

df = spark.read.csv(r"C:\Users\Devak\PycharmProjects\taf_agust\input_files\customer_data\customer_data_01.csv",header=True,inferSchema=True)
print(df.schema.json())

with open(r"C:\Users\Devak\PycharmProjects\taf_agust\tests\table1\schema.json",'r')as f:
    schema = StructType.fromJson(json.load(f))

print('shema is',schema)


df_schema =spark.read.schema(schema).csv(r"C:\Users\Devak\PycharmProjects\taf_agust\input_files\customer_data\customer_data_01.csv",header=True)

df_schema.printSchema()
df.show()
