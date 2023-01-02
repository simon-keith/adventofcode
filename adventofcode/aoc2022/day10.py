from typing import Iterator
from typing import List
from typing import Optional

from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(puzzle_input: List[str]) -> Iterator[Optional[int]]:
    for line in puzzle_input:
        match line.split():
            case "addx", x:
                yield int(x)
            case ("noop",):
                yield None
            case _:
                raise ValueError("invalid input")


def iter_register_values(puzzle_input: List[str]) -> Iterator[int]:
    register = 1
    for x in parse_puzzle_input(puzzle_input):
        yield register
        if x is not None:
            yield register
            register += x


def solve_part1(puzzle_input: List[str]) -> int:
    strength = 0
    for idx, register in enumerate(iter_register_values(puzzle_input)):
        if ((idx + 1) - 20) % 40 == 0:
            strength += (idx + 1) * register
    return strength


def solve_part2(puzzle_input: List[str]) -> str:
    register_value_list = list(iter_register_values(puzzle_input))
    width, height = 40, len(register_value_list) // 40
    crt = [["."] * width for _ in range(height)]
    for idx, register in enumerate(register_value_list):
        i, j = idx // width, idx % width
        if j - 1 <= register <= j + 1:
            crt[i][j] = "#"
    return "\n".join("".join(row) for row in crt)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2022, 10)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
