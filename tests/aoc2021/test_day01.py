from pytest import fixture

from adventofcode.aoc2021.day01 import solve_part1
from adventofcode.aoc2021.day01 import solve_part2


@fixture
def puzzle_input():
    return [
        "199",
        "200",
        "208",
        "210",
        "200",
        "207",
        "240",
        "269",
        "260",
        "263",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 7


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 5
