import math
from collections import deque
from typing import Dict, Generator, Iterable, List, Tuple

from adventofcode.utils.input import read_puzzle_input


def _parse(puzzle_input: List[str]) -> Dict[Tuple[int, int], int]:
    grid = {}
    for i, row in enumerate(puzzle_input):
        for j, c in enumerate(row):
            grid[(i, j)] = int(c)
    return grid


def _get_adjacent(i: int, j: int) -> Iterable[Tuple[int, int]]:
    return ((i + di, j + dj) for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)))


def _is_lower_than_adjacent(
    grid: Dict[Tuple[int, int], int],
    i: int,
    j: int,
) -> Tuple[int, bool]:
    height = grid[(i, j)]
    adjacent = (grid.get(coords, float("inf")) for coords in _get_adjacent(i, j))
    return height, all(height < a for a in adjacent)


def _find_minima(
    grid: Dict[Tuple[int, int], int]
) -> Generator[Tuple[int, int, int], None, None]:
    for i, j in grid:
        height, lower = _is_lower_than_adjacent(grid, i, j)
        if lower:
            yield i, j, height


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
                    for coords in _get_adjacent(*coords):
                        if grid.get(coords, 9) != 9:
                            fifo.append(coords)
            basin_sizes.append(size)
    return basin_sizes


def solve_part1(puzzle_input: List[str]) -> int:
    grid = _parse(puzzle_input)
    risk_level = 0
    for _, _, value in _find_minima(grid):
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
