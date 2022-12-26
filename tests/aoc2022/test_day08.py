from pytest import fixture

from adventofcode.aoc2022.day08 import solve_part1
from adventofcode.aoc2022.day08 import solve_part2


@fixture
def puzzle_input():
    return [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 21


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 8
