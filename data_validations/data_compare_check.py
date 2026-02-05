from src.utility.report_lib import *
from pyspark.sql.functions import lit,col,when

def data_compare(source,target,key_columns,num_records):
    smt = source.exceptAll(target).withColumn("data_from",lit("source"))
    tms = target.exceptAll(source).withColumn("data_from",lit("target"))
    failed = smt.union(tms)

    failed_count = failed.count()

    if failed_count > 0 :
        failed_records = failed.limit(num_records).collect()
        failed_preview = "\n".join(str(row.asDict()) for row in failed_records)
        write_output("datacompare","FAIL",f"data mismatched\n{failed_preview}",target)
    else:
        write_output('data_compare','PASS',f'no data mismatched',target)

    global comparison_data
    if failed_count > 0:
        column_list = source.columns
        print("column_list",column_list)
        print("key_columns",key_columns)
        for column in column_list:
            print(column.lower())
            if column not in key_columns:
                key_columns.append(column)
                temp_source = source.select(key_columns).withColumnRenamed(column,"source_"+column)
                temp_target = target.select(key_columns).withColumnRenamed(column,"target_"+column)
                key_columns.remove(column)
                temp_join = temp_source.join(temp_target,key_columns,"full_outer")
                comparison_data=(temp_join.withColumn("comparison", when(col("source_" + column) == col("target_" + column),
                                                               True).otherwise(False)).
                      filter("comparison == False").show())

        status = "FAIL"
        write_output("costly data compare operation",status,f"data_mismatched\n{comparison_data}",target)
        return status
    else:
        status = "PASS"
        write_output("costly data compare operation",status,"data_mismatched",target)

        return status
