import re
from typing import List

from adventofcode.tools.input import read_puzzle_input

_PATTERN = re.compile(r"\d")
_SUB_MAP = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def compile_line(line: str) -> int:
    digits = _PATTERN.findall(line)
    if len(digits) > 0:
        return int(digits[0] + digits[-1])
    return 0


def sub_line(line: str) -> str:
    for k, v in _SUB_MAP.items():
        line = line.replace(k, v)
    return line


def solve_part1(puzzle_input: List[str]) -> int:
    return sum(compile_line(line) for line in puzzle_input)


def solve_part2(puzzle_input: List[str]) -> int:
    return sum(compile_line(sub_line(line)) for line in puzzle_input)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2023, 1)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
