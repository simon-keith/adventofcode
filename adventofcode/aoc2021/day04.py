from itertools import islice
from typing import List, Optional, Tuple

from adventofcode.tools.input import read_puzzle_input


class _Grid:
    def __init__(self, grid: Tuple[Tuple[int, ...], ...]) -> None:
        self._grid = grid
        self._mask = [[False] * 5 for _ in range(5)]
        self._last_drawn = None

    def update(self, drawn: int):
        for i in range(5):
            for j in range(5):
                if self._grid[i][j] == drawn:
                    self._mask[i][j] = True
        self._last_drawn = drawn

    def check(self) -> bool:
        cols = zip(*self._mask)
        return any(sum(r) >= 5 for r in self._mask) or any(sum(r) >= 5 for r in cols)

    def score(self) -> Optional[int]:
        if not self._last_drawn:
            return
        unmarked_sum = 0
        for i in range(5):
            for j in range(5):
                if not self._mask[i][j]:
                    unmarked_sum += self._grid[i][j]
        return unmarked_sum * self._last_drawn


def _parse(
    puzzle_input: List[str],
) -> Tuple[Tuple[int, ...], List[_Grid]]:
    iterator = iter(puzzle_input)
    random_numbers = tuple(int(n) for n in next(iterator).split(","))
    no_blank = (line for line in iterator if line)
    grid_list = []
    while True:
        chunk = list(islice(no_blank, 5))
        if not chunk:
            break
        grid = tuple(tuple(int(x) for x in row.split()) for row in chunk)
        grid_list.append(_Grid(grid))
    return random_numbers, grid_list


def _score_first_winning(
    random_numbers: Tuple[int, ...],
    grid_list: List[_Grid],
) -> Optional[int]:
    for drawn in random_numbers:
        for grid in grid_list:
            grid.update(drawn)
            if grid.check():
                return grid.score()


def _score_last_winning(
    random_numbers: Tuple[int, ...],
    grid_list: List[_Grid],
) -> Optional[int]:
    grid_map = {i: g for i, g in enumerate(grid_list)}
    for drawn in random_numbers:
        for i in tuple(grid_map.keys()):
            grid = grid_map[i]
            grid.update(drawn)
            if grid.check():
                if len(grid_map) == 1:
                    return grid.score()
                del grid_map[i]


def solve_part1(puzzle_input: List[str]) -> int:
    random_numbers, grid_list = _parse(puzzle_input)
    score = _score_first_winning(random_numbers, grid_list)
    if score is None:
        raise ValueError("no winning grid")
    return score


def solve_part2(puzzle_input: List[str]) -> int:
    random_numbers, grid_list = _parse(puzzle_input)
    score = _score_last_winning(random_numbers, grid_list)
    if score is None:
        raise ValueError("no winning grid")
    return score


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 4)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
