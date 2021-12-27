from collections import defaultdict
from typing import Dict, List, Set

from adventofcode.tools.input import read_puzzle_input


def _parse(puzzle_input: List[str]) -> Dict[str, Set[str]]:
    network = defaultdict(set)
    for line in puzzle_input:
        origin, destination = line.split("-")
        network[origin].add(destination)
        network[destination].add(origin)
    return network


def _count_paths(
    network: Dict[str, Set[str]],
    extra: bool = False,
    *,
    _cave: str = "start",
    _visited: Set[str] = {"start"},
) -> int:
    if _cave == "end":
        return 1
    paths = 0
    for adj in network[_cave]:
        if adj not in _visited:
            new = {adj} if adj.islower() else set()
            paths += _count_paths(network, extra, _cave=adj, _visited=_visited | new)
        elif extra and adj != "start":
            paths += _count_paths(network, False, _cave=adj, _visited=_visited)
    return paths


def solve_part1(puzzle_input: List[str]) -> int:
    network = _parse(puzzle_input)
    return _count_paths(network)


def solve_part2(puzzle_input: List[str]) -> int:
    network = _parse(puzzle_input)
    return _count_paths(network, True)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 12)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
