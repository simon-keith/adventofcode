import math
from collections import deque
from typing import Dict, Generator, List, Tuple

from adventofcode.library.grid import gridify, iter_adjacent_coordinates
from adventofcode.tools.input import read_puzzle_input


def _parse(puzzle_input: List[str]) -> Dict[Tuple[int, int], int]:
    return gridify(puzzle_input, int)


def _is_lower_than_adjacent(
    grid: Dict[Tuple[int, int], int],
    coordinates: Tuple[int, int],
) -> Tuple[int, bool]:
    height = grid[coordinates]
    adjacent = (
        grid.get(coords, float("inf"))
        for coords in iter_adjacent_coordinates(coordinates, False)
    )
    return height, all(height < a for a in adjacent)


def _find_minima(grid: Dict[Tuple[int, int], int]) -> Generator[int, None, None]:
    for coords in grid:
        height, lower = _is_lower_than_adjacent(grid, coords)
        if lower:
            yield height


def _find_basin_sizes(grid: Dict[Tuple[int, int], int]) -> List[int]:
    # the assumption is that all basins are delimited by 9s or by the border of the grid
    visited = set()
    basin_sizes = []
    for coords, height in grid.items():
        # check if we are in a new basin
        if coords not in visited and height != 9:
            # breadth-first search
            size = 0
            fifo = deque([coords])
            while len(fifo) > 0:
                coords = fifo.popleft()
                if coords not in visited:
                    visited.add(coords)
                    size += 1
                    for coords in iter_adjacent_coordinates(coords, False):
                        if grid.get(coords, 9) != 9:
                            fifo.append(coords)
            basin_sizes.append(size)
    return basin_sizes


def solve_part1(puzzle_input: List[str]) -> int:
    grid = _parse(puzzle_input)
    risk_level = 0
    for value in _find_minima(grid):
        risk_level += value + 1
    return risk_level


def solve_part2(puzzle_input: List[str]) -> int:
    grid = _parse(puzzle_input)
    basins = _find_basin_sizes(grid)
    basins.sort()
    if len(basins) < 3:
        raise ValueError("less than 3 basins")
    return math.prod(basins[-3:])


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 9)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
