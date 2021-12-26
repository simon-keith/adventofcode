from adventofcode.aoc2021.day13 import solve_part1, solve_part2
from pytest import fixture


@fixture
def puzzle_input():
    return [
        "6,10",
        "0,14",
        "9,10",
        "0,3",
        "10,4",
        "4,11",
        "6,0",
        "6,12",
        "4,1",
        "0,13",
        "10,12",
        "3,4",
        "3,0",
        "8,4",
        "1,10",
        "2,14",
        "8,10",
        "9,0",
        "",
        "fold along y=7",
        "fold along x=5",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 17


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == "\n".join(
        [
            "#####",
            "#...#",
            "#...#",
            "#...#",
            "#####",
        ]
    )
