from enum import Enum
from typing import Dict
from typing import Iterable
from typing import List
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input


class Shape(str, Enum):
    ROCK = "ROCK"
    PAPER = "PAPER"
    SCISSORS = "SCISSORS"


class Outcome(int, Enum):
    LOST = 0
    DRAW = 3
    WON = 6


_shape = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS,
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSORS,
}
_value = {Shape.ROCK: 1, Shape.PAPER: 2, Shape.SCISSORS: 3}
_matchup: Dict[Tuple[Shape, Shape], int] = {
    (Shape.ROCK, Shape.PAPER): Outcome.WON,
    (Shape.ROCK, Shape.SCISSORS): Outcome.LOST,
    (Shape.PAPER, Shape.ROCK): Outcome.LOST,
    (Shape.PAPER, Shape.SCISSORS): Outcome.WON,
    (Shape.SCISSORS, Shape.ROCK): Outcome.WON,
    (Shape.SCISSORS, Shape.PAPER): Outcome.LOST,
}
_outcome = {"X": Outcome.LOST, "Y": Outcome.DRAW, "Z": Outcome.WON}
_reverse_matchup = {
    (opponent, outcome): player for (opponent, player), outcome in _matchup.items()
}


def parse_puzzle_input(puzzle_input: List[str]) -> Iterable[Tuple[str, str]]:
    for rnd in puzzle_input:
        left, right = rnd.split()
        yield left, right


def compute_round_score(opponent: Shape, player: Shape) -> int:
    return _value[player] + _matchup.get((opponent, player), Outcome.DRAW)


def solve_part1(puzzle_input: List[str]) -> int:
    total = 0
    for left, right in parse_puzzle_input(puzzle_input):
        opponent, player = _shape[left], _shape[right]
        total += compute_round_score(opponent, player)
    return total


def solve_part2(puzzle_input: List[str]) -> int:
    total = 0
    for left, right in parse_puzzle_input(puzzle_input):
        opponent, outcome = _shape[left], _outcome[right]
        player = _reverse_matchup.get((opponent, outcome), opponent)
        total += compute_round_score(opponent, player)
    return total


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2022, 2)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
