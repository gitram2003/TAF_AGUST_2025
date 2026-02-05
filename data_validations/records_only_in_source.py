from src.utility.report_lib import *

def records_only_in_source(source_df,target_df,key_columns):
    print("_______________ this is records only source ________________")
    """validate records only in the source table"""
    # this is minus operation
    only_source_columns = source_df.select(key_columns).exceptAll(target_df.select(key_columns))

    only_source_columns.show()
    count_only_in_source = only_source_columns.count()

    if count_only_in_source > 0:
        failed_records = only_source_columns.limit(5).collect() #limit 5 records,  collect is convert spark into normal columns
        print("failed_records",failed_records)

        failed_preview = [row.asDict() for row in failed_records]
        print("failed_preview",failed_preview)

        status = "FAIL"
        write_output(validation_type="records_in_source",status=status,details=f"sample failed records : {failed_preview}",table=source_df)

    else:
        status = "PASS"
        write_output(validation_type="records_in_source",status=status,details=f"Extra records in target  : {source_df.count()}",table=source_df)
    return status

