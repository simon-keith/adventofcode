from collections import deque
from statistics import median_high
from typing import Deque
from typing import Iterator
from typing import List
from typing import Optional

from adventofcode.tools.input import read_puzzle_input

OPENING_MAP = {")": "(", "]": "[", "}": "{", ">": "<"}
CLOSING_MAP = {v: k for k, v in OPENING_MAP.items()}
SYNTAX_ERROR_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
AUTOCOMPLETE_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


class CorruptedLineError(ValueError):
    def __init__(self, *args: object, symbol: str) -> None:
        super().__init__(*args)
        self.symbol = symbol


def check(line: str) -> Deque[str]:
    stack: Deque[str] = deque()
    for symbol in line:
        try:
            expected_opening_symbol = OPENING_MAP[symbol]
        except KeyError:
            # not a closing symbol
            stack.append(symbol)
        else:
            actual_opening_symbol = stack.pop()
            if actual_opening_symbol != expected_opening_symbol:
                raise CorruptedLineError("invalid symbol", symbol=symbol)
    return stack


def complete(stack: Deque[str]) -> Iterator[str]:
    while len(stack) > 0:
        opening_symbol = stack.pop()
        closing_symbol = CLOSING_MAP[opening_symbol]
        yield closing_symbol


def score_autocomplete(line: str) -> Optional[int]:
    try:
        stack = check(line)
    except CorruptedLineError:
        return None
    score = 0
    for closing_symbol in complete(stack):
        score *= 5
        score += AUTOCOMPLETE_SCORES[closing_symbol]
    return score


def solve_part1(puzzle_input: List[str]) -> int:
    score = 0
    for line in puzzle_input:
        try:
            check(line)
        except CorruptedLineError as e:
            score += SYNTAX_ERROR_SCORES[e.symbol]
    return score


def solve_part2(puzzle_input: List[str]) -> int:
    scores = list(score_autocomplete(line) for line in puzzle_input)
    return median_high(s for s in scores if s is not None)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 10)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
