import math
import re
from typing import Dict
from typing import Iterator
from typing import List
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input

_NUM_PATTERN = re.compile(r"\d+")
_SYM_PATTERN = re.compile(r"[^0-9\.]")
_GEAR_PATTERN = re.compile(r"\*")


def iter_patterns(
    puzzle_input: List[str],
    pattern: re.Pattern,
) -> Iterator[Tuple[int, re.Match]]:
    for i, row in enumerate(puzzle_input):
        for m in pattern.finditer(row):
            yield i, m


def iter_adjacent(i: int, j_start: int, j_end: int) -> Iterator[Tuple[int, int]]:
    for j in range(j_start - 1, j_end + 1):
        yield (i - 1, j)
    yield (i, j_end)
    for j in range(j_end, j_start - 2, -1):
        yield (i + 1, j)
    yield (i, j_start - 1)


def _iter_gear_ratios(
    row_index: int,
    gear_match: re.Match,
    match_dict: Dict[Tuple[int, int], re.Match],
) -> int:
    unique_matches = {
        id(m): m
        for m in (
            match_dict.get((i, j))
            for i, j in iter_adjacent(row_index, gear_match.start(), gear_match.end())
        )
        if m
    }
    return (
        math.prod(int(m.group()) for m in unique_matches.values())
        if len(unique_matches) == 2
        else 0
    )


def solve_part1(puzzle_input: List[str]) -> int:
    sym_set = set((i, m.start()) for i, m in iter_patterns(puzzle_input, _SYM_PATTERN))
    return sum(
        (
            int(m.group())
            for i, m in iter_patterns(puzzle_input, _NUM_PATTERN)
            if any(coords in sym_set for coords in iter_adjacent(i, m.start(), m.end()))
        )
    )


def solve_part2(puzzle_input: List[str]) -> int:
    num_dict = {
        (i, j): m
        for i, m in iter_patterns(puzzle_input, _NUM_PATTERN)
        for j in range(m.start(), m.end())
    }
    return sum(
        _iter_gear_ratios(i, m, num_dict)
        for i, m in iter_patterns(puzzle_input, _GEAR_PATTERN)
    )


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2023, 3)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
