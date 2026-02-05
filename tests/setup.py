# from setuptools import setup, find_packages
#
# setup(
#     name='taf_august',
#     version='1.0.0',
#     author='ramanjaneyulu',
#     description='Test Automation Framework for Data Quality Validation',
#     packages=find_packages(where='src'),
#     package_dir={'': 'src'},
#     install_requires=[
#         'pytest',
#         'pyyaml',
#         'pandas',
#         'pyspark',
#         'snowflake-connector-python'
#     ],
# )
from pyspark.sql import SparkSession

# Create SparkSession
# from pyspark.sql import SparkSession
#
# spark = SparkSession.builder \
#     .master("local[1]") \
#     .appName("SparkByExamples.com") \
#     .getOrCreate()
#
# dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
# df = spark.createDataFrame(dataList, schema=['Language','fee'])
#
# df.show()
#
# spark.stop()


#
# from pyspark.sql import SparkSession
#
# spark = SparkSession.builder \
#     .config("spark.jars", "file:/C:/Users/Devak/PycharmProjects/taf_agust/TAF_AGUST_2025/jars_file/mssql-jdbc-12.2.1.jre11.jar") \
#     .getOrCreate()
#
#
# df = spark.read \
#     .format("jdbc") \
#     .option("url", "jdbc:sqlserver://slqdatabasedemo100001.database.windows.net:1433;database=test_db") \
#     .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
#     .option("dbtable", "dbo.cust_data_1") \
#     .option("user", "ram08082003") \
#     .option("password", "Rama08082003") \
#     .load()
#
# df.show()
#
# df1 = spark.read \
#     .format("jdbc") \
#     .option("url", "jdbc:sqlserver://slqdatabasedemo100001.database.windows.net:1433;database=test_db") \
#     .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
#     .option("dbtable", "dbo.cust_data_2") \
#     .option("user", "ram08082003") \
#     .option("password", "Rama08082003") \
#     .load()
#
# df1.show()
#
#
# df2 = spark.read \
#     .format("jdbc") \
#     .option("url", "jdbc:sqlserver://slqdatabasedemo100001.database.windows.net:1433;database=test_db") \
#     .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
#     .option("dbtable", "dbo.cust_data_2") \
#     .option("user", "ram08082003") \
#     .option("password", "Rama08082003") \
#     .load()
#
# df2.show()

import os

taf_agust = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("taf_agust", taf_agust)

jar = os.path.join(taf_agust,'jars_file','mssql-jdbc-12.2.1.jre11.jar')
print("jar", jar)
