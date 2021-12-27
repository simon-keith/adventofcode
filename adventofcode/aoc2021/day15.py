import heapq
from itertools import product
from typing import Dict, Generator, List, Tuple

from adventofcode.utils.helpers.grid import gridify, iter_adjacent_coordinates
from adventofcode.utils.input import read_puzzle_input


def _parse(puzzle_input: List[str]) -> Dict[Tuple[int, int], int]:
    return gridify(puzzle_input, int)


def _iter_neighbors(
    grid: Dict[Tuple[int, int], int],
    coordinates: Tuple[int, int],
) -> Generator[Tuple[Tuple[int, int], int], None, None]:
    adj = iter_adjacent_coordinates(coordinates, False)
    for coords in adj:
        try:
            yield coords, grid[coords]
        except KeyError:
            pass


def _dijkstra_risk(
    grid: Dict[Tuple[int, int], int],
    start: Tuple[int, int],
    target: Tuple[int, int],
) -> Dict[Tuple[int, int], Tuple[Tuple[int, int], int]]:
    risks = {start: 0}
    priority_queue = [(0, start)]
    while len(priority_queue) > 0:
        _, origin = heapq.heappop(priority_queue)
        if origin == target:
            return risks[origin]
        for destination, r in _iter_neighbors(grid, origin):
            new_risk = risks[origin] + r
            if new_risk < risks.get(destination, float("inf")):
                risks[destination] = new_risk
                heapq.heappush(priority_queue, (new_risk, destination))
    raise ValueError("did not reach the target")


def _extend_grid(
    grid: Dict[Tuple[int, int], int],
    down: int,
    right: int,
) -> Dict[Tuple[int, int], int]:
    target = max(grid)
    len_i, len_j = (c + 1 for c in target)
    offsets = tuple(c for c in product(range(down), range(right)) if c != (0, 0))
    for (i, j), risk in tuple(grid.items()):
        for d, r in offsets:
            grid[(i + d * len_i, j + r * len_j)] = (risk + d + r - 1) % 9 + 1
    return grid


def solve_part1(puzzle_input: List[str]) -> int:
    grid = _parse(puzzle_input)
    start, target = (0, 0), max(grid)
    return _dijkstra_risk(grid, start, target)


def solve_part2(puzzle_input: List[str]) -> int:
    grid = _extend_grid(_parse(puzzle_input), 5, 5)
    start, target = (0, 0), max(grid)
    return _dijkstra_risk(grid, start, target)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 15)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
