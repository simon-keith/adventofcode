from itertools import chain
from typing import Callable
from typing import Dict
from typing import Iterator
from typing import List
from typing import Tuple
from typing import TypeVar

_T = TypeVar("_T")


def gridify(
    puzzle_input: List[str],
    parse: Callable[[str], _T],
) -> Dict[Tuple[int, int], _T]:
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
    coordinates: Tuple[int, int],
    diagonal: bool = True,
) -> Iterator[Tuple[int, int]]:
    if diagonal:
        offsets = chain(_ADJ_ORTH, _ADJ_DIAG)
    else:
        offsets = chain(_ADJ_ORTH)
    return ((coordinates[0] + o[0], coordinates[1] + o[1]) for o in offsets)
