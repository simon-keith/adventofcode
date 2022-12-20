from pytest import fixture

from adventofcode.aoc2021.day05 import solve_part1
from adventofcode.aoc2021.day05 import solve_part2


@fixture
def puzzle_input():
    return [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 5


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 12
