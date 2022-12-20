from pytest import fixture

from adventofcode.aoc2022.day01 import solve_part1
from adventofcode.aoc2022.day01 import solve_part2


@fixture
def puzzle_input():
    return [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 24000


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 45000
