from itertools import takewhile
from typing import Iterable
from typing import List
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(puzzle_input: List[str]) -> Iterable[Tuple[int, ...]]:
    puzzle_iter = iter(puzzle_input)
    while True:
        carrying = tuple(int(x) for x in takewhile(len, puzzle_iter))
        if len(carrying) == 0:
            break
        yield carrying


def solve_part1(puzzle_input: List[str]) -> int:
    return max(sum(x) for x in parse_puzzle_input(puzzle_input))


def solve_part2(puzzle_input: List[str]) -> int:
    a, b, c, *_ = sorted(
        (sum(x) for x in parse_puzzle_input(puzzle_input)),
        reverse=True,
    )
    return a + b + c


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2022, 1)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
