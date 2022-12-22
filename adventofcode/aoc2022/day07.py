from collections import defaultdict
from itertools import accumulate
from typing import DefaultDict
from typing import Iterator
from typing import List
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(puzzle_input: List[str]) -> Iterator[Tuple[str, ...]]:
    for line in puzzle_input:
        yield tuple(line.split())


def build_tree(terminal_iter: Iterator[Tuple[str, ...]]) -> DefaultDict[str, int]:
    tree: DefaultDict[str, int] = defaultdict(int)
    path: List[str] = []
    for args in terminal_iter:
        match args:
            case "$", "cd", "/":
                path.clear()
                path.append("/")
            case "$", "cd", "..":
                path.pop()
            case "$", "cd", dirname:
                path.append(f"{dirname}/")
            case "$", "ls":
                pass
            case "dir", _:
                pass
            case size, _:
                for p in accumulate(path):
                    tree[p] += int(size)
    return tree


def solve_part1(puzzle_input: List[str]) -> int:
    tree = build_tree(parse_puzzle_input(puzzle_input))
    return sum(size for size in tree.values() if size <= 100000)


def solve_part2(puzzle_input: List[str]) -> int:
    tree = build_tree(parse_puzzle_input(puzzle_input))
    excess = tree["/"] - (70000000 - 30000000)
    return min(size for size in tree.values() if size >= excess)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2022, 7)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
