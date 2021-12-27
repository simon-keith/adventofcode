from collections import defaultdict
from itertools import dropwhile, pairwise
from typing import DefaultDict, Dict, List, Tuple

from adventofcode.tools.input import read_puzzle_input


def _parse(puzzle_input: List[str]) -> Tuple[str, Dict[str, Tuple[str, str]]]:
    it = iter(puzzle_input)
    polymer = next(it)
    rules = {}
    for r in dropwhile(lambda x: len(x) == 0, it):
        (left, right), insertion = r.split(" -> ")
        rules[(left + right)] = (left + insertion, insertion + right)
    return polymer, rules


def _get_polymer_pairs(polymer: str) -> DefaultDict[str, int]:
    pairs = defaultdict(int)
    for p in pairwise(polymer):
        pairs["".join(p)] += 1
    return pairs


def _grow_polymer_pairs(
    pairs: DefaultDict[str, int],
    rules: Dict[str, Tuple[str, str]],
    iterations: int,
) -> DefaultDict[str, int]:
    for _ in range(iterations):
        new_pairs = defaultdict(int)
        for p, count in pairs.items():
            for new in rules[p]:
                new_pairs[new] += count
        pairs = new_pairs
    return pairs


def _get_polymer_elements_counter(
    polymer: str,
    pairs: DefaultDict[str, int],
) -> List[Tuple[str, int]]:
    counter = defaultdict(int)
    for (left, _), count in pairs.items():
        counter[left] += count
    counter[polymer[-1]] += 1
    return tuple(sorted(counter.items(), key=lambda x: -x[1]))


def _solve(puzzle_input: List[str], iterations: int) -> int:
    polymer, rules = _parse(puzzle_input)
    pairs = _get_polymer_pairs(polymer)
    new_pairs = _grow_polymer_pairs(pairs, rules, iterations)
    counter = _get_polymer_elements_counter(polymer, new_pairs)
    return counter[0][1] - counter[-1][1]


def solve_part1(puzzle_input: List[str]) -> int:
    return _solve(puzzle_input, 10)


def solve_part2(puzzle_input: List[str]) -> int:
    return _solve(puzzle_input, 40)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 14)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
