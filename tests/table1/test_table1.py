def test_table1(read_data):
    source_df,target_df = read_data
    source_df.show()
    target_df.show()
    source_df.printSchema()
    assert source_df.count() == target_df.count(),'assert is true'


