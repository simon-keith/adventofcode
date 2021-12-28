from collections import defaultdict
from itertools import chain
from typing import Generator, List, Tuple

from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(
    puzzle_input: List[str],
) -> Generator[Tuple[int, int, int, int], None, None]:
    return (
        chain.from_iterable(((int(c) for c in p.split(",")) for p in row.split(" -> ")))
        for row in puzzle_input
    )


def sign(a: int, b: int) -> int:
    if a == b:
        return 0
    return 1 if b > a else -1


def iter_coords(
    segment: Tuple[int, int, int, int],
    allow_diag: bool,
) -> Generator[Tuple[int, int], None, None]:
    x1, y1, x2, y2 = segment
    dx = sign(x1, x2)
    dy = sign(y1, y2)
    if allow_diag or dx == 0 or dy == 0:
        yield x1, y1
        while x1 != x2 or y1 != y2:
            x1 += dx
            y1 += dy
            yield x1, y1


def solve(puzzle_input: List[str], allow_diag: bool) -> int:
    coords_counter = defaultdict(int)
    for segment in parse_puzzle_input(puzzle_input):
        for coords in iter_coords(segment, allow_diag):
            coords_counter[coords] += 1
    return sum(c > 1 for c in coords_counter.values())


def solve_part1(puzzle_input: List[str]) -> int:
    return solve(puzzle_input, False)


def solve_part2(puzzle_input: List[str]) -> int:
    return solve(puzzle_input, True)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 5)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
