from collections import deque
from itertools import takewhile
from typing import Generator, Iterable, List, Set, Tuple

from adventofcode.utils.input import read_puzzle_input

_DIM_TO_INDEX = {"x": 1, "y": 0}


def _parse(
    puzzle_input: List[str],
) -> Tuple[Set[Tuple[int, int]], Tuple[Tuple[int, int], ...]]:
    iterator = iter(puzzle_input)
    dots = set(
        (int(i), int(j)) for j, i in (c.split(",") for c in takewhile(len, iterator))
    )
    instructions = tuple(
        (_DIM_TO_INDEX[dim], int(pos))
        for dim, pos in (f.strip("fold along ").split("=") for f in iterator)
    )
    return dots, instructions


def _fold(
    dots: Set[Tuple[int, int]],
    instructions: Iterable[Tuple[int, int]],
) -> Generator[None, None, None]:
    for idx, pos in instructions:
        for coords in tuple(dots):
            if coords[idx] >= pos:
                dots.remove(coords)
                if coords[idx] > pos:
                    new_coords = list(coords)
                    new_coords[idx] = coords[idx] - (coords[idx] - pos) * 2
                    dots.add(tuple(new_coords))
        yield


def _generate(dots: Set[Tuple[int, int]]) -> str:
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
    dots, instructions = _parse(puzzle_input)
    next(_fold(dots, instructions))
    return len(dots)


def solve_part2(puzzle_input: List[str]) -> str:
    dots, instructions = _parse(puzzle_input)
    deque(_fold(dots, instructions), maxlen=0)
    return _generate(dots)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 13)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
