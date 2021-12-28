from typing import Dict, List, Set, Tuple

from adventofcode.library.grid import gridify, iter_adjacent_coordinates
from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(puzzle_input: List[str]) -> Dict[Tuple[int, int], int]:
    return gridify(puzzle_input, int)


def increment(
    grid: Dict[Tuple[int, int], int],
    coords: Tuple[int, int],
    flashing: Set[int],
):
    grid[coords] += 1
    if grid[coords] > 9:
        flashing.add(coords)


def update(grid: Dict[Tuple[int, int], int]) -> int:
    flashing = set()
    for coords in grid:
        increment(grid, coords, flashing)
    flash_count = 0
    while len(flashing) > 0:
        coords = flashing.pop()
        flash_count += 1
        grid[coords] = 0
        for adj in filter(
            lambda x: grid.get(x, 0) > 0,
            iter_adjacent_coordinates(coords),
        ):
            increment(grid, adj, flashing)
    return flash_count


def solve_part1(puzzle_input: List[str]) -> int:
    grid = parse_puzzle_input(puzzle_input)
    total_flash = 0
    for _ in range(100):
        total_flash += update(grid)
    return total_flash


def solve_part2(puzzle_input: List[str]) -> int:
    grid = parse_puzzle_input(puzzle_input)
    for i in range(10000):
        flashes = update(grid)
        if flashes == len(grid):
            return i + 1
    raise ValueError("reached maximum number of iterations")


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 11)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
