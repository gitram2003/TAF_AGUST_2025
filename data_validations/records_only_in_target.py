
from src.utility.report_lib import *

def records_only_in_target(source_df,target_df,key_columns):
    print("_______________ this is records only target ________________")
    """validate records only in the target table"""
    # this is minus operation
    only_target_columns = target_df.select(key_columns).exceptAll(source_df.select(key_columns))

    only_target_columns.show()
    count_only_in_target = only_target_columns.count()
    if count_only_in_target > 0:
        failed_records = only_target_columns.limit(5).collect() #limit 5 records,  collect is convert spark into normal columns
        print("failed_records",failed_records)
        failed_preview = [row.asDict() for row in failed_records]
        print("failed_preview",failed_preview)
        status = "FAIL"
        write_output(validation_type="records_in_target",status=status,details=f"Extra records in target  : {failed_preview}",table = target_df)

    else:
        status = "PASS"
        write_output(validation_type="records_in_target",status=status,details=f"No extra records in target: {source_df.count()}",table = target_df)

    return status

