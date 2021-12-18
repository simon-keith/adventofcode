from adventofcode.aoc2021.day06 import solve_part1, solve_part2
from pytest import fixture


@fixture
def puzzle_input():
    return ["3,4,3,1,2"]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 5934


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 26984457539
