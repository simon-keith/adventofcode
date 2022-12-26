from pytest import fixture
from pytest import mark

from adventofcode.aoc2022.day06 import solve_part1
from adventofcode.aoc2022.day06 import solve_part2


@fixture
def puzzle_input(request):
    match request.param:
        case 1:
            return ["mjqjpqmgbljsphdztnvjfqwrcgsmlb"]
        case 2:
            return ["bvwbjplbgvbhsrlpgdmjqwftvncz"]
        case 3:
            return ["nppdvjthqldpwncqszvftbrmjlhg"]
        case 4:
            return ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"]
        case 5:
            return ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]
        case _:
            raise ValueError("invalid fixture parameter")


@mark.parametrize(
    "puzzle_input,expected",
    [(1, 7), (2, 5), (3, 6), (4, 10), (5, 11)],
    indirect=["puzzle_input"],
)
def test_part1(puzzle_input, expected):
    assert solve_part1(puzzle_input) == expected


@mark.parametrize(
    "puzzle_input,expected",
    [(1, 19), (2, 23), (3, 23), (4, 29), (5, 26)],
    indirect=["puzzle_input"],
)
def test_part2(puzzle_input, expected):
    assert solve_part2(puzzle_input) == expected
