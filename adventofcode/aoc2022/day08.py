import math
from itertools import product
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(
    puzzle_input: List[str],
) -> Tuple[Tuple[Tuple[int, ...], ...], Tuple[int, int]]:
    grid = tuple(tuple(int(col) for col in row) for row in puzzle_input)
    height, width = len(grid), len(grid[0])
    return grid, (height, width)


def find_edge(it: Iterable[int], height: int) -> Tuple[bool, int]:
    tree_count = 0
    for i in it:
        tree_count += 1
        if i >= height:
            return False, tree_count
    return True, tree_count


def iter_around(
    grid: Tuple[Tuple[int, ...], ...],
    i: int,
    j: int,
    height: int,
    width: int,
) -> Tuple[int, Iterator[int], Iterator[int], Iterator[int], Iterator[int]]:
    down = (grid[x][j] for x in range(i + 1, height))
    right = (grid[i][x] for x in range(j + 1, width))
    up = (grid[x][j] for x in range(i - 1, -1, -1))
    left = (grid[i][x] for x in range(j - 1, -1, -1))
    return grid[i][j], down, right, up, left


def solve_part1(puzzle_input: List[str]) -> int:
    grid, (h, w) = parse_puzzle_input(puzzle_input)
    visible = 0
    for i, j in product(range(h), range(w)):
        tree_height, *tree_it = iter_around(grid, i, j, h, w)
        if any(find_edge(it, tree_height)[0] for it in tree_it):
            visible += 1
    return visible


def solve_part2(puzzle_input: List[str]) -> int:
    grid, (h, w) = parse_puzzle_input(puzzle_input)
    scenic_score = 0
    for i, j in product(range(h), range(w)):
        tree_height, *tree_it = iter_around(grid, i, j, h, w)
        scenic_score = max(
            scenic_score,
            math.prod(find_edge(it, tree_height)[1] for it in tree_it),
        )
    return scenic_score


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2022, 8)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
