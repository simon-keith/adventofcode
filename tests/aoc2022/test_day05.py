from pytest import fixture

from adventofcode.aoc2022.day05 import solve_part1
from adventofcode.aoc2022.day05 import solve_part2


@fixture
def puzzle_input():
    return [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == "CMZ"


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == "MCD"
