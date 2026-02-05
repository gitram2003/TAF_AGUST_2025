from src.utility.report_lib import *
from pyspark.sql.functions import col,when

def schema_compare(source,target,spark):
    source_schema_df = source.schema
    target_schema_df = target.schema

    source_schema_df = spark.createDataFrame ([(field.name.lower(),field.dataType.simpleString())
                            for field in source_schema_df],["column_name","source_data_type"])
    target_schema_df =  spark.createDataFrame([(field.name.lower(),field.dataType.simpleString())
                            for field in target_schema_df],["column_name","target_data_type"])

    #perform a full join on column names and compare data type
    schema_comparison = (source_schema_df.alias("src")
                         .join(target_schema_df.alias("tgt"),col("src.column_name") == col("tgt.column_name"),"full_outer")
                         .select(
                         col("src.column_name").alias("source_col_name"),
                         col("tgt.column_name").alias("target_col_name"),
                         col("src.source_data_type"),
                         col("tgt.target_data_type"),
                         when(col("src.source_data_type") == col("target_data_type"),"PASS").otherwise("FAIL").alias("status")
                         ))
    #filter only rows where the status is failed
    failed = schema_comparison.filter(col("status") == "FAIL")
    failed.show()
    failed_count = failed.count()

    if failed_count > 0:
        failed_records = failed.collect()
        failed_preview = [row.asDict() for row in failed_records]
        status ="FAIL"
        write_output("schema check",status,f"schema not compare{failed_preview}",target)
    else:
        status ="PASS"
        write_output("schema check",status,f"schema is correct in both source table and target table    ",target)

    return status