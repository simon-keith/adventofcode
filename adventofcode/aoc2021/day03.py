from functools import reduce
from typing import Generator, Iterable, List, Tuple

from adventofcode.utils.input import read_puzzle_input


def _parse(puzzle_input: List[str]) -> Generator[Iterable[bool], None, None]:
    for row in puzzle_input:
        yield (bool(int(c)) for c in row)


def _ratio(iterable: Iterable[bool]) -> float:
    n, a = 0, 0
    for x in iterable:
        n += 1
        a += x
    return a / n


def _is_most_common(column: Iterable[bool]) -> bool:
    return _ratio(column) >= 0.5


def _bool_array_to_int(x: Iterable[bool]) -> int:
    return reduce(lambda a, b: (a << 1) | b, x)


def _decode_power_consumption(iterable: Iterable[Tuple[bool, ...]]) -> Tuple[int, int]:
    columns = zip(*iterable)
    column_most_common = tuple(_is_most_common(c) for c in columns)
    gamma = _bool_array_to_int(column_most_common)
    epsilon = _bool_array_to_int((not m for m in column_most_common))
    return gamma, epsilon


def _compress_grid(
    grid: Tuple[Tuple[int, ...], ...],
    most_common: bool,
) -> Tuple[int, ...]:
    if len(grid) == 0:
        raise ValueError("empty grid")
    column_count = len(grid[0])
    for i in range(column_count):
        mc = _is_most_common((row[i] for row in grid))
        mc = mc if most_common else not mc
        grid = tuple(row for row in grid if row[i] == mc)
        if len(grid) == 1:
            return grid[0]
    raise ValueError("could not compress grid")


def _decode_life_support(iterable: Iterable[Tuple[bool, ...]]) -> Tuple[int, int]:
    grid = tuple(tuple(r for r in row) for row in iterable)
    o2 = _bool_array_to_int(_compress_grid(grid, True))
    co2 = _bool_array_to_int(_compress_grid(grid, False))
    return o2, co2


def solve_part1(puzzle_input: List[str]) -> int:
    gamma, epsilon = _decode_power_consumption(_parse(puzzle_input))
    return gamma * epsilon


def solve_part2(puzzle_input: List[str]) -> int:
    o2, co2 = _decode_life_support(_parse(puzzle_input))
    return o2 * co2


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 3)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
