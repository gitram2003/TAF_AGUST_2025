import great_expectations as ge

from data_validations.count_check import *
from data_validations.duplicate_check import duplicate_check
from data_validations.duplicate_check import duplicate_check
from data_validations.null_value_check import null_values_check
from data_validations.uniqueness_check import uniqueness_check
from data_validations.data_compare_check import data_compare
from data_validations.schema_check import schema_compare
from data_validations.data_quality_check import *
import pytest

@pytest.mark.regression
def test_table1_count(read_data):
    print('\n<<<<<<<<<<<<<<test_table1_counting start>>>>>>>>>>>>>>>')
    source_df,target_df,validation_config = read_data
    source_df.show()
    target_df.show()
    key_columns = validation_config['count_check']['key_columns']
    status = count_check(source_df,target_df,key_columns=key_columns)
    assert status.upper() == "PASS"


def test_table1_duplicates(read_data):
    print('\n<<<<<<<<<<<<<<test_table1_duplicates checking start>>>>>>>>>>>>>>>')
    source_df,target_df,validation_config = read_data
    target_df.show()
    key_columns = validation_config['duplicate_check']['key_columns']
    status = duplicate_check(df=target_df,key_cols=key_columns)
    assert status.upper() == "PASS"

def test_table1_unique_ness(read_data):
    print('\n<<<<<<<<<<<<<<test_table1_uniqueness checking start>>>>>>>>>>>>>>>')
    source_df,target_df,validation_config = read_data
    target_df.show()
    unique_cols = validation_config['uniqueness_check']['unique_columns']
    status = uniqueness_check(df=target_df,unique_cols=unique_cols)
    assert status == "PASS"

def test_table1_nulls_check(read_data):
    print('\n<<<<<<<<<<<<<<test_table1_null_values checking start>>>>>>>>>>>>>>>')
    source_df,target_df,validation_config = read_data
    target_df.show()
    nulls_check = validation_config['null_check']['null_columns']
    num_records = validation_config['null_check']['num_records']
    status = null_values_check(df=target_df,null_cols=nulls_check,num_records=num_records)
    assert status == "PASS"

def test_table1_data_compare(read_data):
    print('\n<<<<<<<<<<<<<<test_table1_data_compare checking start>>>>>>>>>>>>>>>')
    source_df,target_df,validation_config = read_data
    source_df.show()
    target_df.show()
    key_columns = validation_config['data_compare_check']['key_column']
    num_records = validation_config['data_compare_check']['num_records']
    status = data_compare(source_df,target_df,key_columns,num_records)
    assert status == "PASS"

def test_table1_schema_check(read_data,spark_session):
    print('\n<<<<<<<<<<<<<<test_table1_schema_compare checking start>>>>>>>>>>>>>>>')
    source_df,target_df,validation_config = read_data
    spark = spark_session
    source_df.show()
    target_df.show()
    status = schema_compare(source_df,target_df,spark)
    assert status == "PASS"

def test_table_name_check(read_data):
    print('\n<<<<<<<<<<<<<<test_table1_name checking start>>>>>>>>>>>>>>>')
    source_df,target_df,validation_config = read_data
    target_df.show()
    column = validation_config['dq_check']['name_check']
    status = name_check(target_df,column)
    assert status == "PASS"


# def test_table1_name_check_GE(read_data):
    # print('\n<<<<<<<<<<<<<<test_table1_name_GE checking start>>>>>>>>>>>>>>>')
    # source_df,target_df,validation_config = read_data
    # dataset = ge.SparkDFDataset(target_df)
    # col_name = validation_config['dq_check']['name_check']
    # result = dataset.expect_column_values_to_match_regex(col_name,r"^[a-zA-Z ]+$")
    # print(result)



