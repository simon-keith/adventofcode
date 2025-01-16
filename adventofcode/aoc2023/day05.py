import re
from dataclasses import dataclass
from functools import reduce
from itertools import chain
from itertools import groupby
from typing import List
from typing import Set
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input

_RNG_PTRN = re.compile(r"(\d+) (\d+) (\d+)")
_SEED_PTRN = re.compile(r"(\d+) (\d+)")


@dataclass
class _Map:
    source: int
    destination: int
    length: int

    def is_in_source(self, seed: int) -> bool:
        return self.source <= seed < self.source + self.length

    def is_in_destination(self, seed: int) -> bool:
        return self.destination <= seed < self.destination + self.length


_MapSeq = Tuple[_Map, ...]


def _extract_map(map_match: re.Match) -> _Map:
    dst, src, lng = (int(g) for g in map_match.groups())
    return _Map(source=src, destination=dst, length=lng)


def _extract_map_seq(puzzle_map: List[str]) -> Tuple[_MapSeq, ...]:
    return tuple(
        tuple(_extract_map(m) for m in it if m is not None)
        for test, it in groupby((_RNG_PTRN.match(line) for line in puzzle_map), bool)
        if test
    )


def _extract_raw_seed_and_map_seq(
    puzzle_input: List[str],
) -> Tuple[str, Tuple[_MapSeq, ...]]:
    puzzle_seed, puzzle_map = puzzle_input[0], puzzle_input[1:]
    map_list = _extract_map_seq(puzzle_map)
    return puzzle_seed, map_list


def _parse_seed_range(range_match: re.Match) -> range:
    start, length = (int(g) for g in range_match.groups())
    return range(start, start + length)


def _lookup_seed(seed: int, map_seq: _MapSeq) -> int:
    for m in map_seq:
        if m.is_in_source(seed):
            return seed + m.destination - m.source
    return seed


def _inverse_lookup_seed(seed: int, map_seq: _MapSeq) -> int:
    for m in map_seq:
        if m.is_in_destination(seed):
            return seed + m.source - m.destination
    return seed


def _invert_map(map_info: _MapSeq, knots: Set[int]) -> Set[int]:
    map_knots = set(
        chain.from_iterable((m.source, m.source + m.length - 1) for m in map_info)
    )
    return map_knots | set(_inverse_lookup_seed(y, map_info) for y in knots)


def solve_part1(puzzle_input: List[str]) -> int:
    puzzle_seed, map_list = _extract_raw_seed_and_map_seq(puzzle_input)
    seed_list = tuple(int(s) for s in puzzle_seed.removeprefix("seeds: ").split())
    return min(reduce(_lookup_seed, map_list, seed) for seed in seed_list)


def solve_part2(puzzle_input: List[str]) -> int:
    puzzle_seed, map_list = _extract_raw_seed_and_map_seq(puzzle_input)
    seed_list = tuple(_parse_seed_range(m) for m in _SEED_PTRN.finditer(puzzle_seed))
    knots: Set[int] = set()
    knots = reduce(lambda acc, m: _invert_map(m, acc), reversed(map_list), knots)
    knots = set(filter(lambda s: any(s in seed for seed in seed_list), knots))
    knots |= set(chain.from_iterable((s.start, s.stop - 1) for s in seed_list))
    return min(reduce(_lookup_seed, map_list, seed) for seed in knots)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2023, 5)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
