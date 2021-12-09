from itertools import pairwise
from typing import Generator, Iterable, List

from adventofcode.utils.input import read_puzzle_input
from adventofcode.utils.iterable import sliding_window


def _parse(puzzle_input: List[str]) -> Generator[int, None, None]:
    return (int(line) for line in puzzle_input)


def _count_positive_diffs(iterable: Iterable[int]) -> int:
    return sum(current > previous for previous, current in pairwise(iterable))


def solve_part1(puzzle_input: List[str]) -> int:
    iterable = _parse(puzzle_input)
    return _count_positive_diffs(iterable)


def solve_part2(puzzle_input: List[str]) -> int:
    iterable = (sum(w) for w in sliding_window(_parse(puzzle_input), 3))
    return _count_positive_diffs(iterable)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 1)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
