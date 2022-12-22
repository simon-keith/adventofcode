import re
from typing import Iterator
from typing import List
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input

_PATTERN = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")


def parse_puzzle_input(
    puzzle_input: List[str],
) -> Iterator[Tuple[Tuple[int, int], Tuple[int, int]]]:
    for assignments in puzzle_input:
        match = _PATTERN.match(assignments)
        if not match:
            raise ValueError("invalid input")
        min_1, max_1, min_2, max_2 = (int(c) for c in match.groups())
        yield (min_1, max_1), (min_2, max_2)


def solve_part1(puzzle_input: List[str]) -> int:
    total = 0
    for (min_1, max_1), (min_2, max_2) in parse_puzzle_input(puzzle_input):
        if (max_1 - min_1) < (max_2 - min_2):
            (min_1, max_1), (min_2, max_2) = (min_2, max_2), (min_1, max_1)
        fully_contains = min_2 >= min_1 and max_2 <= max_1
        total += fully_contains
    return total


def solve_part2(puzzle_input: List[str]) -> int:
    total = 0
    for (min_1, max_1), (min_2, max_2) in parse_puzzle_input(puzzle_input):
        overlaps = min_1 <= max_2 and max_1 >= min_2
        total += overlaps
    return total


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2022, 4)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
