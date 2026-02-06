import datetime

from pyspark.sql.functions import regexp_extract,col
from pyspark.sql.types import BooleanType
from pyspark.sql import DataFrame

def name_check(target,column):
    pattern = "^[A-Za-z ]+$"
    # add a new column "is_valid" indicating if the contains only alphabets characters
    df =target.withColumn("is_valid",regexp_extract(col(column),pattern,0) != "")
    df.show()

    failed = df.filter("is_valid= False")
    failed.show()
    status = "FAIL" if failed.count()>0 else "PASS"
    return status
