import collections
from itertools import islice, pairwise
from typing import Any, Generator, Iterable, List, Tuple

from adventofcode.library.iter import iter_sliding_windows
from adventofcode.tools.input import read_puzzle_input


def _parse(puzzle_input: List[str]) -> Generator[int, None, None]:
    return (int(line) for line in puzzle_input)


def _count_positive_diffs(iterable: Iterable[int]) -> int:
    return sum(current > previous for previous, current in pairwise(iterable))


def solve_part1(puzzle_input: List[str]) -> int:
    iterable = _parse(puzzle_input)
    return _count_positive_diffs(iterable)


def solve_part2(puzzle_input: List[str]) -> int:
    iterable = (sum(w) for w in iter_sliding_windows(_parse(puzzle_input), 3))
    return _count_positive_diffs(iterable)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 1)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
