from collections import defaultdict
from itertools import dropwhile
from itertools import pairwise
from typing import DefaultDict
from typing import Dict
from typing import List
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(
    puzzle_input: List[str],
) -> Tuple[str, Dict[str, Tuple[str, str]]]:
    it = iter(puzzle_input)
    polymer = next(it)
    rules = {}
    for r in dropwhile(lambda x: len(x) == 0, it):
        pair, insertion = r.split(" -> ")
        left, right = list(pair)
        rules[pair] = (left + insertion, insertion + right)
    return polymer, rules


def get_polymer_pairs(polymer: str) -> DefaultDict[str, int]:
    pairs: DefaultDict[str, int] = defaultdict(int)
    for p in pairwise(polymer):
        pairs["".join(p)] += 1
    return pairs


def grow_polymer_pairs(
    pairs: DefaultDict[str, int],
    rules: Dict[str, Tuple[str, str]],
    iterations: int,
) -> DefaultDict[str, int]:
    for _ in range(iterations):
        new_pairs: DefaultDict[str, int] = defaultdict(int)
        for p, count in pairs.items():
            for new in rules[p]:
                new_pairs[new] += count
        pairs = new_pairs
    return pairs


def get_polymer_elements_counter(
    polymer: str,
    pairs: DefaultDict[str, int],
) -> Tuple[Tuple[str, int], ...]:
    counter: DefaultDict[str, int] = defaultdict(int)
    for pair, count in pairs.items():
        left, _ = list(pair)
        counter[left] += count
    counter[polymer[-1]] += 1
    return tuple(sorted(counter.items(), key=lambda x: -x[1]))


def solve(puzzle_input: List[str], iterations: int) -> int:
    polymer, rules = parse_puzzle_input(puzzle_input)
    pairs = get_polymer_pairs(polymer)
    new_pairs = grow_polymer_pairs(pairs, rules, iterations)
    counter = get_polymer_elements_counter(polymer, new_pairs)
    return counter[0][1] - counter[-1][1]


def solve_part1(puzzle_input: List[str]) -> int:
    return solve(puzzle_input, 10)


def solve_part2(puzzle_input: List[str]) -> int:
    return solve(puzzle_input, 40)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 14)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
