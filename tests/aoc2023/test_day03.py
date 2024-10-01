from pytest import fixture

from adventofcode.aoc2023.day03 import solve_part1
from adventofcode.aoc2023.day03 import solve_part2


@fixture
def puzzle_input():
    return [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 4361


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 467835
