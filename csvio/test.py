from itertools import chain
from pathlib import Path
from uuid import uuid4

from .dictio import csv2dict, dict2csv


def main() -> None:
    source = Path("files/csv").glob("*.csv")
    target = Path("files/result.csv")

    # Try to combind all CSV files into a single CSV while add a new UUID column
    data = chain.from_iterable(csv2dict(file, "utf-8-sig") for file in source)
    data = ({**row, "uuid": uuid4()} for row in data)
    dict2csv(target, data, "utf-8")


if __name__ == "__main__":
    main()
