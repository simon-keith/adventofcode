from itertools import chain
from typing import Callable, Dict, Iterable, List, Tuple, TypeVar

T = TypeVar("T")


def gridify(
    puzzle_input: List[str],
    parse: Callable[[str], T] = str,
) -> Dict[Tuple[int, int], T]:
    grid = {}
    for i, row in enumerate(puzzle_input):
        for j, c in enumerate(row):
            grid[(i, j)] = parse(c)
    return grid


_ADJ_ORTH = (
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0),
)
_ADJ_DIAG = (
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
)


def iter_adjacent_coordinates(
    i: int,
    j: int,
    diagonal: bool = True,
) -> Iterable[Tuple[int, int]]:
    if diagonal:
        offsets = chain(_ADJ_ORTH, _ADJ_DIAG)
    else:
        offsets = _ADJ_ORTH
    return ((i + di, j + dj) for di, dj in offsets)
