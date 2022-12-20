import heapq
from itertools import product
from typing import Dict
from typing import List
from typing import Tuple

from adventofcode.library.grid import gridify
from adventofcode.library.grid import iter_adjacent_coordinates
from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(puzzle_input: List[str]) -> Dict[Tuple[int, int], int]:
    return gridify(puzzle_input, int)


def minimize_risk(
    grid: Dict[Tuple[int, int], int],
    start: Tuple[int, int],
    target: Tuple[int, int],
) -> int:
    risks = {start: 0}
    priority_queue = [(0, start)]
    while len(priority_queue) > 0:
        _, origin = heapq.heappop(priority_queue)
        if origin == target:
            return risks[origin]
        for destination in iter_adjacent_coordinates(origin, False):
            if destination not in risks and (r := grid.get(destination)) is not None:
                risks[destination] = priority = risks[origin] + r
                heapq.heappush(priority_queue, (priority, destination))
    raise ValueError("did not reach the target")


def extend_grid(
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
    grid = parse_puzzle_input(puzzle_input)
    start, target = (0, 0), max(grid)
    return minimize_risk(grid, start, target)


def solve_part2(puzzle_input: List[str]) -> int:
    grid = extend_grid(parse_puzzle_input(puzzle_input), 5, 5)
    start, target = (0, 0), max(grid)
    return minimize_risk(grid, start, target)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 15)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
