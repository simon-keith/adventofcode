from collections import deque
from itertools import takewhile
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Set
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input

DIM_TO_INDEX = {"x": 1, "y": 0}


def parse_puzzle_input(
    puzzle_input: List[str],
) -> Tuple[Set[Tuple[int, int]], Tuple[Tuple[int, int], ...]]:
    iterator = iter(puzzle_input)
    dots = set(
        (int(i), int(j)) for j, i in (c.split(",") for c in takewhile(len, iterator))
    )
    fold_along = "fold along "
    instructions = tuple(
        (DIM_TO_INDEX[dim], int(pos))
        for dim, pos in (f.lstrip(fold_along).split("=") for f in iterator)
    )
    return dots, instructions


def fold(
    dots: Set[Tuple[int, int]],
    instructions: Iterable[Tuple[int, int]],
) -> Iterator[None]:
    for idx, pos in instructions:
        for coords in tuple(dots):
            if coords[idx] >= pos:
                dots.remove(coords)
                if coords[idx] > pos:
                    new_coords = list(coords)
                    new_coords[idx] = coords[idx] - (coords[idx] - pos) * 2
                    x, y = new_coords
                    dots.add((x, y))
        yield


def generate(dots: Set[Tuple[int, int]]) -> str:
    mini, maxi, minj, maxj = 0, 0, 0, 0
    for i, j in dots:
        mini = min(i, mini)
        minj = min(j, minj)
        maxi = max(i, maxi)
        maxj = max(j, maxj)
    return "\n".join(
        "".join("#" if (i, j) in dots else "." for j in range(minj, maxj + 1))
        for i in range(mini, maxi + 1)
    )


def solve_part1(puzzle_input: List[str]) -> int:
    dots, instructions = parse_puzzle_input(puzzle_input)
    next(fold(dots, instructions))
    return len(dots)


def solve_part2(puzzle_input: List[str]) -> str:
    dots, instructions = parse_puzzle_input(puzzle_input)
    deque(fold(dots, instructions), maxlen=0)
    return generate(dots)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 13)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
