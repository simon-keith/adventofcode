from pytest import fixture

from adventofcode.aoc2021.day15 import solve_part1
from adventofcode.aoc2021.day15 import solve_part2


@fixture
def puzzle_input():
    return [
        "1163751742",
        "1381373672",
        "2136511328",
        "3694931569",
        "7463417111",
        "1319128137",
        "1359912421",
        "3125421639",
        "1293138521",
        "2311944581",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 40


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 315
