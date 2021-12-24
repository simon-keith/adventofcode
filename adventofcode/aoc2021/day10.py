from collections import deque
from typing import Generator, List, Optional, Deque, Tuple
from statistics import median_high

from adventofcode.utils.input import read_puzzle_input

_OPENING_MAP = {")": "(", "]": "[", "}": "{", ">": "<"}
_CLOSING_MAP = {v: k for k, v in _OPENING_MAP.items()}
_SYNTAX_ERROR_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
_AUTOCOMPLETE_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


class CorruptedLineError(ValueError):
    def __init__(self, *args: object, symbol: str) -> None:
        super().__init__(*args)
        self.symbol = symbol


def _check(line: str) -> Deque[str]:
    stack = deque()
    for symbol in line:
        try:
            expected_opening_symbol = _OPENING_MAP[symbol]
        except KeyError:
            # not a closing symbol
            stack.append(symbol)
        else:
            actual_opening_symbol = stack.pop()
            if actual_opening_symbol != expected_opening_symbol:
                raise CorruptedLineError("invalid symbol", symbol=symbol)
    return stack


def _complete(stack: Deque[str]) -> Generator[str, None, None]:
    while len(stack) > 0:
        opening_symbol = stack.pop()
        closing_symbol = _CLOSING_MAP[opening_symbol]
        yield closing_symbol


def _score_autocomplete(line: str) -> Optional[int]:
    try:
        stack = _check(line)
    except CorruptedLineError:
        return
    score = 0
    for closing_symbol in _complete(stack):
        score *= 5
        score += _AUTOCOMPLETE_SCORES[closing_symbol]
    return score


def solve_part1(puzzle_input: List[str]) -> int:
    score = 0
    for line in puzzle_input:
        try:
            _check(line)
        except CorruptedLineError as e:
            score += _SYNTAX_ERROR_SCORES[e.symbol]
    return score


def solve_part2(puzzle_input: List[str]) -> int:
    scores = list(
        filter(
            lambda x: x is not None,
            list(_score_autocomplete(line) for line in puzzle_input),
        )
    )
    return median_high(scores)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 10)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
