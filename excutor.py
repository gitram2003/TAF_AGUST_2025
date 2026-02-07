import pytest
import sys

def main():
    pytest_args = [
        "tests/table1",
        "tests/table2",
        '-v',
        '-s',
        "-m","regression",
        "-k", "count"
            ]
    #Exit with pytest code exits
    sys.exit(pytest.main(pytest_args))

if __name__ == "__main__":
    main()