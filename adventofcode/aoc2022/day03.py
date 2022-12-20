import string
from collections import defaultdict
from functools import reduce
from typing import DefaultDict
from typing import Iterator
from typing import List
from typing import Set
from typing import Tuple

from adventofcode.library.iter import iter_chunks
from adventofcode.tools.input import read_puzzle_input

_priority = {letter: i + 1 for i, letter in enumerate(string.ascii_letters)}


def parse_puzzle_input(
    puzzle_input: List[str],
) -> Iterator[Tuple[DefaultDict[str, int], DefaultDict[str, int]]]:
    for rucksack in puzzle_input:
        center = len(rucksack) // 2
        compartments = rucksack[:center], rucksack[center:]
        counters: Tuple[DefaultDict[str, int], DefaultDict[str, int]] = (
            defaultdict(int),
            defaultdict(int),
        )
        for items, cnt in zip(compartments, counters):
            for item in items:
                cnt[item] += 1
        yield counters


def _extract_priority(common: Set[str]) -> int:
    if len(common) != 1:
        raise ValueError("expecting one common item")
    return _priority[common.pop()]


def solve_part1(puzzle_input: List[str]) -> int:
    total = 0
    for left, right in parse_puzzle_input(puzzle_input):
        common = left.keys() & right.keys()
        total += _extract_priority(common)
    return total


def solve_part2(puzzle_input: List[str]) -> int:
    total = 0
    for grp in iter_chunks(parse_puzzle_input(puzzle_input), 3):
        rucksacks = list(left.keys() | right.keys() for left, right in grp)
        common = reduce(lambda a, b: a & b, rucksacks)
        total += _extract_priority(common)
    return total


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2022, 3)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
