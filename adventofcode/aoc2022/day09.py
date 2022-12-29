import re
from itertools import pairwise
from typing import Iterator
from typing import List
from typing import Set

from adventofcode.tools.input import read_puzzle_input

_PATTERN = re.compile(r"([DRUL]) (\d+)")
_MOTIONS = {"D": -1j, "R": 1 + 0j, "U": 1j, "L": -1 + 0j}


def parse_puzzle_input(puzzle_input: List[str]) -> Iterator[complex]:
    for row in puzzle_input:
        if (mtch := _PATTERN.match(row)) is None:
            raise ValueError("invalid motion")
        name, length = mtch.groups()
        motion = _MOTIONS[name]
        yield from (motion for _ in range(int(length)))


def sign(x: complex) -> complex:
    return complex((x.real > 0) - (x.real < 0), (x.imag > 0) - (x.imag < 0))


def move_tail_towards_head(tail: complex, head: complex) -> complex:
    return tail + sign(head - tail)


def is_touching(tail: complex, head: complex) -> bool:
    return abs(head - tail) < 2


def solve_part1(puzzle_input: List[str]) -> int:
    tail, head = 0j, 0j
    visited: Set[complex] = {tail}
    for motion in parse_puzzle_input(puzzle_input):
        head += motion
        while not is_touching(tail, head):
            tail = move_tail_towards_head(tail, head)
            visited.add(tail)
    return len(visited)


def solve_part2(puzzle_input: List[str]) -> int:
    rope = [0j] * 10
    visited: Set[complex] = {rope[-1]}
    for motion in parse_puzzle_input(puzzle_input):
        rope[0] += motion
        for head, tail in pairwise(range(len(rope))):
            while not is_touching(rope[head], rope[tail]):
                rope[tail] = move_tail_towards_head(rope[tail], rope[head])
                if tail == len(rope) - 1:
                    visited.add(rope[tail])
    return len(visited)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2022, 9)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
