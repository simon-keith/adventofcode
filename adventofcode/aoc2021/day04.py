from typing import List, Optional, Tuple

from adventofcode.library.iter import iter_chunks
from adventofcode.tools.input import read_puzzle_input


class Grid:
    def __init__(self, grid: Tuple[Tuple[int, ...], ...]) -> None:
        self.grid = grid
        self.mask = [[False] * 5 for _ in range(5)]
        self.last_drawn = None

    def update(self, drawn: int):
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == drawn:
                    self.mask[i][j] = True
        self.last_drawn = drawn

    def check(self) -> bool:
        cols = zip(*self.mask)
        return any(sum(r) >= 5 for r in self.mask) or any(sum(r) >= 5 for r in cols)

    def score(self) -> Optional[int]:
        if not self.last_drawn:
            return
        unmarked_sum = 0
        for i in range(5):
            for j in range(5):
                if not self.mask[i][j]:
                    unmarked_sum += self.grid[i][j]
        return unmarked_sum * self.last_drawn


def parse_puzzle_input(
    puzzle_input: List[str],
) -> Tuple[Tuple[int, ...], List[Grid]]:
    iterator = iter(puzzle_input)
    random_numbers = tuple(int(n) for n in next(iterator).split(","))
    no_blank = (line for line in iterator if line)
    grid_list = []
    for chunk in iter_chunks(no_blank, 5):
        grid = tuple(tuple(int(x) for x in row.split()) for row in chunk)
        grid_list.append(Grid(grid))
    return random_numbers, grid_list


def score_first_winning(
    random_numbers: Tuple[int, ...],
    grid_list: List[Grid],
) -> Optional[int]:
    for drawn in random_numbers:
        for grid in grid_list:
            grid.update(drawn)
            if grid.check():
                return grid.score()


def score_last_winning(
    random_numbers: Tuple[int, ...],
    grid_list: List[Grid],
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
    random_numbers, grid_list = parse_puzzle_input(puzzle_input)
    score = score_first_winning(random_numbers, grid_list)
    if score is None:
        raise ValueError("no winning grid")
    return score


def solve_part2(puzzle_input: List[str]) -> int:
    random_numbers, grid_list = parse_puzzle_input(puzzle_input)
    score = score_last_winning(random_numbers, grid_list)
    if score is None:
        raise ValueError("no winning grid")
    return score


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 4)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
