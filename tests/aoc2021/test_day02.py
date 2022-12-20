from pytest import fixture

from adventofcode.aoc2021.day02 import solve_part1
from adventofcode.aoc2021.day02 import solve_part2


@fixture
def puzzle_input():
    return [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 150


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 900
