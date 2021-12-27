from importlib import resources
from typing import Generator, List, Tuple

from adventofcode.tools.skeleton import PACKAGE, format_module, format_solution


def _get_package_and_resource(year: int, day: int) -> Tuple[str, str]:
    module = format_module(year)
    solution = format_solution(day)
    package = f"{PACKAGE}.{module}.data"
    resource = f"{solution}.txt"
    return package, resource


def read_puzzle_input(year: int, day: int) -> List[str]:
    package, resource = _get_package_and_resource(year, day)
    with resources.open_text(package, resource) as f:
        return f.read().strip("\n").split("\n")
