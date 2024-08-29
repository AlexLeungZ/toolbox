import csv
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Any


def csv2dict(path: Path, enc: str | None = None) -> Iterator[dict[str | Any, str | Any]]:
    with path.open(encoding=enc) as file:
        yield from csv.DictReader(file)


def dict2csv(path: Path, data: Iterable[dict[str | Any, str | Any]], enc: str | None = None) -> None:
    _iter = iter(data)
    first = next(_iter)  # Get first row for headers

    with path.open("w", encoding=enc) as file:
        writer = csv.DictWriter(file, first.keys())
        writer.writeheader()

        writer.writerow(first)
        writer.writerows(_iter)
