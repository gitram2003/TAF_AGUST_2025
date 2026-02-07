from src.utility.report_lib import *
from pyspark.sql.functions import col,trim,upper


def null_values_check(df,null_cols,num_records):
    """validate that the SPECIFIED COLUMNS HAVE  NO NULL OR EMPTY COLUMNS """
    failures =[]
    for columns in null_cols:
        print("null_columns",columns)
        failing_rows = df.filter(
            (col(columns).isNull()) | (trim(col(columns)) == ""))
        null_count = failing_rows.count()
        print("null_count",null_count)
        if null_count>0:
            failed_records = failing_rows.limit(num_records).collect()#Get the first 5 records
            print("failed records",failed_records)
            failed_preview = [row.asDict() for row in failed_records]
            print("failed preview",failed_preview)
            failures.append({
                "columns":columns,
                "null_count":null_count,
                "failed_records":failed_records,
            })
            print("failures ",failures)
            if len(failures)>0:
                status ="FAIL"
                write_output("null_values_count",status,f"Failures : {failures}",df)
            else:
                status = "PASS"
                write_output("null_values_count",status,f"No Failures : {null_count}",df)
                return status