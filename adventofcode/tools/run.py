import importlib
from functools import partial
from timeit import Timer
from types import ModuleType
from typing import Any
from typing import List
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input
from adventofcode.tools.skeleton import PACKAGE
from adventofcode.tools.skeleton import format_module
from adventofcode.tools.skeleton import format_solution


def _get_module(year: int, day: int) -> ModuleType:
    module = format_module(year)
    solution = format_solution(day)
    package = f"{PACKAGE}.{module}.{solution}"
    return importlib.import_module(package)


def _init(year: int, day: int) -> Tuple[ModuleType, List[str]]:
    module = _get_module(year, day)
    puzzle_input = read_puzzle_input(year, day)
    return module, puzzle_input


def solve(year: int, day: int) -> Tuple[Any, Any]:
    module, puzzle_input = _init(year, day)
    part1 = module.solve_part1(puzzle_input)
    part2 = module.solve_part2(puzzle_input)
    return part1, part2


def timeit(year: int, day: int) -> Tuple[float, float]:
    module, puzzle_input = _init(year, day)
    p1 = partial(module.solve_part1, puzzle_input)
    p2 = partial(module.solve_part2, puzzle_input)
    t1, t2 = (t[1] / t[0] for t in (Timer(p).autorange() for p in (p1, p2)))
    return t1, t2
