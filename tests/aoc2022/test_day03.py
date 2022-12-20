from pytest import fixture

from adventofcode.aoc2022.day03 import solve_part1
from adventofcode.aoc2022.day03 import solve_part2


@fixture
def puzzle_input():
    return [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 157


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 70
