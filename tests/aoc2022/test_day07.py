from pytest import fixture

from adventofcode.aoc2022.day07 import solve_part1
from adventofcode.aoc2022.day07 import solve_part2


@fixture
def puzzle_input():
    return [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 95437


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 24933642
