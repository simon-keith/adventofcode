from pytest import fixture

from adventofcode.aoc2021.day03 import solve_part1
from adventofcode.aoc2021.day03 import solve_part2


@fixture
def puzzle_input():
    return [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 198


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 230
