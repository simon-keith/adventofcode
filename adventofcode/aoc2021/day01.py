from itertools import pairwise
from typing import Iterable
from typing import Iterator
from typing import List

from adventofcode.library.iter import iter_sliding_windows
from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(puzzle_input: List[str]) -> Iterator[int]:
    return (int(line) for line in puzzle_input)


def count_positive_diffs(iterable: Iterable[int]) -> int:
    return sum(current > previous for previous, current in pairwise(iterable))


def solve_part1(puzzle_input: List[str]) -> int:
    iterable = parse_puzzle_input(puzzle_input)
    return count_positive_diffs(iterable)


def solve_part2(puzzle_input: List[str]) -> int:
    it = (sum(w) for w in iter_sliding_windows(parse_puzzle_input(puzzle_input), 3))
    return count_positive_diffs(it)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 1)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
