from adventofcode.aoc2021.day12 import solve_part1, solve_part2
from pytest import fixture


@fixture
def puzzle_input():
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


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 226


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 3509
