from pandas.core.common import not_none

from src.utility.report_lib import *
from data_validations.records_only_in_source import *
from data_validations.records_only_in_target import *


def count_check(source_df,target_df,key_columns):
    source_count = source_df.count()
    target_count = target_df.count()

    if source_count == target_count:
        status = "PASS"
        print(f"count is matching between source and target source_count is ==> {source_count} and target_count is ==> {target_count}")
        records_only_in_source(source_df= source_df, target_df=target_df, key_columns=key_columns)
        records_only_in_target(source_df= source_df,target_df=target_df,key_columns=key_columns)
        write_output("count_validations",status,f"count is matching between source and target source_count is ==> {source_count} and target_count is ==> {target_count}",table=source_df)
    else:
        status = "FAIL"
        records_only_in_source(source_df=source_df, target_df=target_df, key_columns=key_columns)
        records_only_in_target(source_df=source_df, target_df=target_df, key_columns=key_columns)
        write_output("count_validation",status,f"count is not matching between source and target source_count is ==> {source_count} and target_count is ==> {target_count} difference is ==> "f"{source_count-target_count}",target_df)

    return status