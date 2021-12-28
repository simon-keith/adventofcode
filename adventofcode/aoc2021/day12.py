from collections import defaultdict
from typing import Dict, List, Set

from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(puzzle_input: List[str]) -> Dict[str, Set[str]]:
    network = defaultdict(set)
    for line in puzzle_input:
        origin, destination = line.split("-")
        network[origin].add(destination)
        network[destination].add(origin)
    return network


def count_paths(
    network: Dict[str, Set[str]],
    extra: bool = False,
    *,
    cave: str = "start",
    visited: Set[str] = {"start"},
) -> int:
    if cave == "end":
        return 1
    paths = 0
    for adj in network[cave]:
        if adj not in visited:
            new = {adj} if adj.islower() else set()
            paths += count_paths(network, extra, cave=adj, visited=visited | new)
        elif extra and adj != "start":
            paths += count_paths(network, False, cave=adj, visited=visited)
    return paths


def solve_part1(puzzle_input: List[str]) -> int:
    network = parse_puzzle_input(puzzle_input)
    return count_paths(network)


def solve_part2(puzzle_input: List[str]) -> int:
    network = parse_puzzle_input(puzzle_input)
    return count_paths(network, True)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 12)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
