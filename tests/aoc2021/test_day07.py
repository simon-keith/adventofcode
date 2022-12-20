from pytest import fixture

from adventofcode.aoc2021.day07 import solve_part1
from adventofcode.aoc2021.day07 import solve_part2


@fixture
def puzzle_input():
    return ["16,1,2,0,4,2,7,1,2,14"]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 37


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 168
