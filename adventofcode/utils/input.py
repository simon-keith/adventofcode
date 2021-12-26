from importlib import resources
from typing import Generator, List, Tuple

from adventofcode.utils.skeleton import format_module, format_solution


def _get_package_and_resource(year: int, day: int) -> Tuple[str, str]:
    module = format_module(year)
    solution = format_solution(day)
    package = f"adventofcode.{module}.data"
    resource = f"{solution}.txt"
    return package, resource


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
                yield line.strip("\n")


def read_puzzle_input(year: int, day: int) -> List[str]:
    package, resource = _get_package_and_resource(year, day)
    with resources.open_text(package, resource) as f:
        return f.read().strip("\n").split("\n")
