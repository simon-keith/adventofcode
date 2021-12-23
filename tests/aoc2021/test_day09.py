from adventofcode.aoc2021.day09 import solve_part1, solve_part2
from pytest import fixture


@fixture
def puzzle_input():
    return ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 15


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) is None
