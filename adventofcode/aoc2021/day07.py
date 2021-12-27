import math
from statistics import mean, median_high
from typing import List, Tuple

from adventofcode.tools.input import read_puzzle_input


def _parse(puzzle_input: List[str]) -> Tuple[int, ...]:
    (data,) = puzzle_input
    return tuple(int(x) for x in data.split(","))


def _compute_consumption(distance: int) -> int:
    return int(distance * (distance + 1) / 2)


def solve_part1(puzzle_input: List[str]) -> int:
    positions = _parse(puzzle_input=puzzle_input)
    target = median_high(positions)
    return sum(abs(p - target) for p in positions)


def solve_part2(puzzle_input: List[str]) -> int:
    positions = _parse(puzzle_input=puzzle_input)
    target_raw = mean(positions)
    target_choices = math.floor(target_raw), math.ceil(target_raw)
    solution_choices = (
        sum(_compute_consumption(abs(p - t)) for p in positions) for t in target_choices
    )
    return min(solution_choices)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 7)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
