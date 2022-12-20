from pytest import fixture

from adventofcode.aoc2022.day02 import solve_part1
from adventofcode.aoc2022.day02 import solve_part2


@fixture
def puzzle_input():
    return [
        "A Y",
        "B X",
        "C Z",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 15


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 12
