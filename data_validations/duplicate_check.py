from src.utility.report_lib import *


def duplicate_check(df,key_cols):      #duplicates check in target columns
    print("_______________ this is duplicate check______________")
    duplicates = df.groupBy(key_cols).count().filter('count>1')
    # df.createOrReplaceTempView("df")  # this is unnecessary code
    # duplicates = spark.sql("select key_cols,count(1) from df group by key_cols having count(1)>1")

    print("duplicate rows")
    duplicates.show()
    duplicates_count = duplicates.count()
    print("duplicate count: ",duplicates_count)

    if duplicates_count>0:
        failed_records = duplicates.limit(5).collect() #get 5 duplicate records then fail the test case
        duplicates_preview = [row.asDict() for row in failed_records]#convert to dictionary format.

        status = "FAIL"
        write_output(validation_type="duplicates_validation",status=status,details=f"In target table found the duplicates{duplicates_preview}",table=df)
    else:
        status = "PASS"
        write_output("duplicates_validation",status,f"No duplicates in the target table....",df)

    return status
