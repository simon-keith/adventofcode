from pytest import fixture

from adventofcode.aoc2022.day04 import solve_part1
from adventofcode.aoc2022.day04 import solve_part2


@fixture
def puzzle_input():
    return [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 2


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 4
