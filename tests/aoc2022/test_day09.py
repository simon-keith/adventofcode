from pytest import fixture
from pytest import mark

from adventofcode.aoc2022.day09 import solve_part1
from adventofcode.aoc2022.day09 import solve_part2


@fixture
def puzzle_input(request):
    match request.param:
        case 1:
            return [
                "R 4",
                "U 4",
                "L 3",
                "D 1",
                "R 4",
                "D 1",
                "L 5",
                "R 2",
            ]
        case 2:
            return [
                "R 5",
                "U 8",
                "L 8",
                "D 3",
                "R 17",
                "D 10",
                "L 25",
                "U 20",
            ]


@mark.parametrize(
    "puzzle_input,expected",
    [(1, 13)],
    indirect=["puzzle_input"],
)
def test_part1(puzzle_input, expected):
    assert solve_part1(puzzle_input) == expected


@mark.parametrize(
    "puzzle_input,expected",
    [(1, 1), (2, 36)],
    indirect=["puzzle_input"],
)
def test_part2(puzzle_input, expected):
    assert solve_part2(puzzle_input) == expected
