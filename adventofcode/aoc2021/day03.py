from functools import reduce
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(
    puzzle_input: List[str],
) -> Iterator[Iterable[bool]]:
    for row in puzzle_input:
        yield (bool(int(c)) for c in row)


def ratio(iterable: Iterable[bool]) -> float:
    n, a = 0, 0
    for x in iterable:
        n += 1
        a += x
    return a / n


def is_most_common(column: Iterable[bool]) -> bool:
    return ratio(column) >= 0.5


def bool_array_to_int(bool_iter: Iterable[bool]) -> int:
    int_iter = (int(x) for x in bool_iter)
    return reduce(lambda a, b: (a << 1) | b, int_iter)


def decode_power_consumption(iterable: Iterable[Iterable[bool]]) -> Tuple[int, int]:
    columns = zip(*iterable)
    column_most_common = tuple(is_most_common(c) for c in columns)
    gamma = bool_array_to_int(column_most_common)
    epsilon = bool_array_to_int((not m for m in column_most_common))
    return gamma, epsilon


def compress_grid(
    grid: Tuple[Tuple[bool, ...], ...],
    most_common: bool,
) -> Tuple[bool, ...]:
    if len(grid) == 0:
        raise ValueError("empty grid")
    column_count = len(grid[0])
    for i in range(column_count):
        mc = is_most_common((row[i] for row in grid))
        mc = mc if most_common else not mc
        grid = tuple(row for row in grid if row[i] == mc)
        if len(grid) == 1:
            return grid[0]
    raise ValueError("could not compress grid")


def decode_life_support(iterable: Iterable[Iterable[bool]]) -> Tuple[int, int]:
    grid = tuple(tuple(r for r in row) for row in iterable)
    o2 = bool_array_to_int(compress_grid(grid, True))
    co2 = bool_array_to_int(compress_grid(grid, False))
    return o2, co2


def solve_part1(puzzle_input: List[str]) -> int:
    gamma, epsilon = decode_power_consumption(parse_puzzle_input(puzzle_input))
    return gamma * epsilon


def solve_part2(puzzle_input: List[str]) -> int:
    o2, co2 = decode_life_support(parse_puzzle_input(puzzle_input))
    return o2 * co2


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 3)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
