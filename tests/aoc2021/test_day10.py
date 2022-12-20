from pytest import fixture

from adventofcode.aoc2021.day10 import solve_part1
from adventofcode.aoc2021.day10 import solve_part2


@fixture
def puzzle_input():
    return [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) == 26397


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) == 288957
