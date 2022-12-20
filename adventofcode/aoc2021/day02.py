from typing import Iterable
from typing import Iterator
from typing import List
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(
    puzzle_input: List[str],
) -> Iterator[Tuple[str, int]]:
    for row in puzzle_input:
        command, value = row.split()
        yield command, int(value)


def interpret(iterable: Iterable[Tuple[str, int]]) -> Iterator[Tuple[int, int]]:
    for cmd in iterable:
        match cmd:
            case ("forward", x):
                yield x, 0
            case ("down", x):
                yield 0, x
            case ("up", x):
                yield 0, -x
            case _:
                raise ValueError("invalid command")


def compile_data(iterable: Iterable[Tuple[int, int]]) -> Tuple[int, int]:
    horizontal, depth = 0, 0
    for h, d in iterable:
        horizontal += h
        depth += d
    return horizontal, depth


def compile_with_aim(iterable: Iterable[Tuple[int, int]]) -> Tuple[int, int]:
    horizontal, depth, aim = 0, 0, 0
    for h, a in iterable:
        horizontal += h
        aim += a
        depth += aim * h
    return horizontal, depth


def solve_part1(puzzle_input: List[str]) -> int:
    iterable = interpret(parse_puzzle_input(puzzle_input))
    horizontal, depth = compile_data(iterable)
    return horizontal * depth


def solve_part2(puzzle_input: List[str]) -> int:
    iterable = interpret(parse_puzzle_input(puzzle_input))
    horizontal, depth = compile_with_aim(iterable)
    return horizontal * depth


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 2)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
