from collections import deque
from typing import List, Optional

from adventofcode.utils.input import read_puzzle_input

_CHUNK_MAP = {")": "(", "]": "[", "}": "{", ">": "<"}
_SYNTAX_ERROR_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}


def _find_illegal(line: str) -> Optional[str]:
    stack = deque()
    for char in line:
        try:
            expected = _CHUNK_MAP[char]
        except KeyError:
            stack.append(char)
        else:
            if stack.pop() != expected:
                return char


def solve_part1(puzzle_input: List[str]) -> int:
    score = 0
    for line in puzzle_input:
        illegal = _find_illegal(line)
        if illegal:
            score += _SYNTAX_ERROR_SCORES[illegal]
    return score


def solve_part2(puzzle_input: List[str]) -> int:
    pass


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 10)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
