from importlib import resources
from typing import Generator, List, Tuple


def _get_package_and_resource(year: int, day: int) -> Tuple[str, str]:
    package = f"adventofcode.aoc{year:d}.data"
    resource = f"day{day:02d}.txt"
    return package, resource


def read_puzzle_input(year: int, day: int) -> List[str]:
    package, resource = _get_package_and_resource(year, day)
    with resources.open_text(package, resource) as f:
        return f.read().strip().split("\n")


def iter_puzzle_input(year: int, day: int) -> Generator[str, None, None]:
    package, resource = _get_package_and_resource(year, day)
    with resources.open_text(package, resource) as f:
        newlines = 0
        for line in f:
            if line == "\n":
                newlines += 1
            else:
                for _ in range(newlines):
                    yield "\n"
                newlines = 0
                yield line.strip()
