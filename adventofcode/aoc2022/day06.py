from typing import Iterator
from typing import List

from adventofcode.library.iter import iter_sliding_windows
from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(puzzle_input: List[str]) -> Iterator[str]:
    (buffer,) = puzzle_input
    yield from buffer


def find_marker(buffer: Iterator[str], size: int):
    for i, marker in enumerate(iter_sliding_windows(buffer, size)):
        if len(set(marker)) == size:
            return i + size
    raise ValueError("could not find marker")


def solve_part1(puzzle_input: List[str]) -> int:
    marker_size = 4
    buffer_it = parse_puzzle_input(puzzle_input)
    return find_marker(buffer_it, marker_size)


def solve_part2(puzzle_input: List[str]) -> int:
    marker_size = 14
    buffer_it = parse_puzzle_input(puzzle_input)
    return find_marker(buffer_it, marker_size)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2022, 6)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
