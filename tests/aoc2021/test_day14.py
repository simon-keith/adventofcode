from pytest import fixture

from adventofcode.aoc2021.day14 import solve_part1
from adventofcode.aoc2021.day14 import solve_part2


@fixture
def puzzle_input():
    return [
        "NNCB",
        "",
        "CH -> B",
        "HH -> N",
        "CB -> H",
        "NH -> C",
        "HB -> C",
        "HC -> B",
        "HN -> C",
        "NN -> C",
        "BH -> H",
        "NC -> B",
        "NB -> B",
        "BN -> B",
        "BB -> N",
        "BC -> B",
        "CC -> N",
        "CN -> C",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 1588


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 2188189693529
