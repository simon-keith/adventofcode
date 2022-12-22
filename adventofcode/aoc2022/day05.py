import re
import string
from collections import OrderedDict
from itertools import takewhile
from typing import Callable
from typing import Iterator
from typing import List
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input

_PROCEDURE_PATTERN = re.compile(r"move (\d+) from (\d+) to (\d+)")
_CRATE_MARKS = set(string.ascii_uppercase)


def _iter_level(level: str) -> Iterator[Tuple[int, str]]:
    for i, mark in enumerate(level):
        if mark in _CRATE_MARKS:
            yield i, mark


def _parse_procedure(step: str) -> Tuple[int, int, int]:
    m = _PROCEDURE_PATTERN.match(step)
    if m is None:
        raise ValueError("invalid input")
    quantity, origin, destination = (int(c) for c in m.groups())
    return quantity, origin, destination


def parse_puzzle_input(
    puzzle_input: List[str],
) -> Tuple[Tuple[List[str], ...], Iterator[Tuple[int, int, int]]]:
    puzzle_iter = iter(puzzle_input)
    crates = list(takewhile(lambda x: x != "", puzzle_iter))
    crates.pop()  # drop useless indices at the bottom
    stack_dict = OrderedDict([(i, [m]) for i, m in _iter_level(crates[-1])])
    for level in crates[-2::-1]:
        for i, mark in _iter_level(level):
            stack_dict[i].append(mark)
    stack_tuple = tuple(stack_dict.values())
    procedure_iter = (_parse_procedure(step) for step in puzzle_iter)
    return stack_tuple, procedure_iter


def operate_crane_9000(
    stack_tuple: Tuple[List[str], ...],
    step: Tuple[int, int, int],
):
    quantity, origin, destination = step
    for _ in range(quantity):
        crate = stack_tuple[origin - 1].pop()
        stack_tuple[destination - 1].append(crate)


def operate_crane_9001(
    stack_tuple: Tuple[List[str], ...],
    step: Tuple[int, int, int],
):
    quantity, origin, destination = step
    origin_strack = stack_tuple[origin - 1]
    destination_stack = stack_tuple[destination - 1]
    crates = origin_strack[-quantity:]
    del origin_strack[-quantity:]
    destination_stack.extend(crates)


def _solve(
    puzzle_input: List[str],
    operate: Callable[[Tuple[List[str], ...], Tuple[int, int, int]], None],
) -> str:
    stack_tuple, procedure_iter = parse_puzzle_input(puzzle_input)
    for step in procedure_iter:
        operate(stack_tuple, step)
    message = "".join(stack[-1] for stack in stack_tuple)
    return message


def solve_part1(puzzle_input: List[str]) -> str:
    return _solve(puzzle_input, operate_crane_9000)


def solve_part2(puzzle_input: List[str]) -> str:
    return _solve(puzzle_input, operate_crane_9001)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2022, 5)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
