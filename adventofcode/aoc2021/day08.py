from typing import FrozenSet, Generator, Iterable, List, Tuple

from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(
    puzzle_input: List[str],
) -> Generator[
    Tuple[Tuple[FrozenSet[str], ...], Tuple[FrozenSet[str], ...]],
    None,
    None,
]:
    for line in puzzle_input:
        signals, digits = line.split("|")
        signals = tuple(frozenset(s) for s in signals.split())
        digits = tuple(frozenset(s) for s in digits.split())
        yield signals, digits


def count_easy_digits(digits_iterable: Iterable[Tuple[FrozenSet[str], ...]]) -> int:
    total = 0
    unique_lengths = {2, 3, 4, 7}
    for digits in digits_iterable:
        for pattern in digits:
            total += len(pattern) in unique_lengths
    return total


def decode(
    signals: Tuple[FrozenSet[str], ...],
    digits: Tuple[FrozenSet[str], ...],
) -> int:
    # 1, 4, 7 and 8 have a unique number of segments
    # 2, 3 and 5 have 5 segments
    # 0, 6 and 9 have 6 segments
    # using 1 and 4 and checking the number of common segments is enough to distinguish
    d1 = next(s for s in signals if len(s) == 2)
    d4 = next(s for s in signals if len(s) == 4)
    display = ""
    for d in digits:
        d1_common = d & d1
        d4_common = d & d4
        match len(d), len(d4_common), len(d1_common):
            case 2, _, _:
                display += "1"
            case 3, _, _:
                display += "7"
            case 4, _, _:
                display += "4"
            case 5, 2, _:
                display += "2"
            case 5, 3, 1:
                display += "5"
            case 5, 3, 2:
                display += "3"
            case 6, 3, 1:
                display += "6"
            case 6, 3, 2:
                display += "0"
            case 6, 4, _:
                display += "9"
            case 7, _, _:
                display += "8"
    return int(display)


def solve_part1(puzzle_input: List[str]) -> int:
    return count_easy_digits((d for _, d in parse_puzzle_input(puzzle_input)))


def solve_part2(puzzle_input: List[str]) -> int:
    total = 0
    for signals, digits in parse_puzzle_input(puzzle_input):
        total += decode(signals, digits)
    return total


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 8)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
