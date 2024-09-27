from pytest import fixture
from pytest import mark

from adventofcode.aoc2023.day01 import solve_part1
from adventofcode.aoc2023.day01 import solve_part2


@fixture
def puzzle_input(request):
    match request.param:
        case 1:
            return ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        case 2:
            return [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ]


@mark.parametrize(
    "puzzle_input,expected",
    [(1, 142)],
    indirect=["puzzle_input"],
)
def test_part1(puzzle_input, expected):
    assert solve_part1(puzzle_input) == expected


@mark.parametrize(
    "puzzle_input,expected",
    [(1, 142), (2, 281)],
    indirect=["puzzle_input"],
)
def test_part2(puzzle_input, expected):
    assert solve_part2(puzzle_input) == expected
