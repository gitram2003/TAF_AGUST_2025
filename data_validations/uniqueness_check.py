from src.utility.report_lib import *


def uniqueness_check(df,unique_cols):
    print("_________________ this is uniqueness_check block ___________________")
    """validate that specified columns have unique values."""
    duplicate_counts ={}

    for col in unique_cols:
        dup_df = df.groupBy(col).count().filter("count >1")
        print('duplicate data frame',dup_df)
        count_duplicates = df.groupBy(col).count().filter("count >1").count()
        print('duplicate count data frame',col,count_duplicates)
        duplicate_counts[col] = count_duplicates
    print("duplicate_counts",duplicate_counts)
    status = "PASS" if all(count == 0 for count in duplicate_counts.values()) else "FAIL"
    write_output("uniqueness_check",status,
                     f"duplicates count per column: {duplicate_counts}",table = df)

    return status