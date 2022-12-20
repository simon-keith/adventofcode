from pytest import fixture

from adventofcode.aoc2021.day11 import solve_part1
from adventofcode.aoc2021.day11 import solve_part2


@fixture
def puzzle_input():
    return [
        "5483143223",
        "2745854711",
        "5264556173",
        "6141336146",
        "6357385478",
        "4167524645",
        "2176841721",
        "6882881134",
        "4846848554",
        "5283751526",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 1656


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 195
