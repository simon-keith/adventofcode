from typing import Dict, List, Tuple

from adventofcode.utils.input import read_puzzle_input


def _parse(puzzle_input: List[str]) -> Dict[Tuple[int, int], int]:
    grid = {}
    for i, row in enumerate(puzzle_input):
        for j, c in enumerate(row):
            grid[(i, j)] = int(c)
    return grid


def _is_lower_than_adjacent(
    grid: Dict[Tuple[int, int], int],
    i: int,
    j: int,
) -> Tuple[int, bool]:
    value = grid[(i, j)]
    adjacent = (
        grid.get((i + di, j + dj), float("inf"))
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0))
    )
    return value, all(value < a for a in adjacent)


def solve_part1(puzzle_input: List[str]) -> int:
    grid = _parse(puzzle_input)
    risk_level = 0
    for i, j in grid:
        value, lower = _is_lower_than_adjacent(grid, i, j)
        if lower:
            risk_level += value + 1
    return risk_level


def solve_part2(puzzle_input: List[str]) -> int:
    pass


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 9)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
