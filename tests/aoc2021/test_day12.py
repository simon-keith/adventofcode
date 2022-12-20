from pytest import fixture
from pytest import mark

from adventofcode.aoc2021.day12 import solve_part1
from adventofcode.aoc2021.day12 import solve_part2


@fixture
def puzzle_input(request):
    match request.param:
        case "small":
            return ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]
        case "medium":
            return [
                "dc-end",
                "HN-start",
                "start-kj",
                "dc-start",
                "dc-HN",
                "LN-dc",
                "HN-end",
                "kj-sa",
                "kj-HN",
                "kj-dc",
            ]
        case "large":
            return [
                "fs-end",
                "he-DX",
                "fs-he",
                "start-DX",
                "pj-DX",
                "end-zg",
                "zg-sl",
                "zg-pj",
                "pj-he",
                "RW-he",
                "fs-DX",
                "pj-RW",
                "zg-RW",
                "start-pj",
                "he-WI",
                "zg-he",
                "pj-fs",
                "start-RW",
            ]
        case _:
            raise ValueError("invalid fixture parameter")


@mark.parametrize(
    "puzzle_input,expected",
    [("small", 10), ("medium", 19), ("large", 226)],
    indirect=["puzzle_input"],
)
def test_part1(puzzle_input, expected):
    assert solve_part1(puzzle_input) == expected


@mark.parametrize(
    "puzzle_input,expected",
    [("small", 36), ("medium", 103), ("large", 3509)],
    indirect=["puzzle_input"],
)
def test_part2(puzzle_input, expected):
    assert solve_part2(puzzle_input) == expected
