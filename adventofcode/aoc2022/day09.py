from typing import Iterator
from typing import List
from typing import Set
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(puzzle_input: List[str]) -> Iterator[Tuple[int, int]]:
    for row in puzzle_input:
        match row.split():
            case "D", x:
                yield from ((1, 0) for _ in range(int(x)))
            case "R", x:
                yield from ((0, 1) for _ in range(int(x)))
            case "U", x:
                yield from ((-1, 0) for _ in range(int(x)))
            case "L", x:
                yield from ((0, -1) for _ in range(int(x)))


def sign_or_zero(x: int) -> int:
    return 1 if x > 0 else (-1 if x < 0 else 0)


def move_one_step(tail: Tuple[int, int], head: Tuple[int, int]) -> Tuple[int, int]:
    tail_i, tail_j = tail
    head_i, head_j = head
    return (
        tail_i + sign_or_zero(head_i - tail_i),
        tail_j + sign_or_zero(head_j - tail_j),
    )


def is_touching(tail: Tuple[int, int], head: Tuple[int, int]) -> bool:
    tail_i, tail_j = tail
    head_i, head_j = head
    return abs(head_i - tail_i) <= 1 and abs(head_j - tail_j) <= 1


def solve_part1(puzzle_input: List[str]) -> int:
    tail_i, tail_j, head_i, head_j = 0, 0, 0, 0
    visited: Set[Tuple[int, int]] = {(tail_i, tail_j)}
    for delta_i, delta_j in parse_puzzle_input(puzzle_input):
        head_i, head_j = head_i + delta_i, head_j + delta_j
        while not is_touching((tail_i, tail_j), (head_i, head_j)):
            tail_i, tail_j = move_one_step((tail_i, tail_j), (head_i, head_j))
            visited.add((tail_i, tail_j))
    return len(visited)


def solve_part2(puzzle_input: List[str]) -> int:
    head_i, head_j, rope_len = 0, 0, 9
    tail_list: List[Tuple[int, int]] = [(0, 0) for _ in range(rope_len)]
    visited: Set[Tuple[int, int]] = {tail_list[-1]}
    for delta_i, delta_j in parse_puzzle_input(puzzle_input):
        next_i, next_j = head_i, head_j = head_i + delta_i, head_j + delta_j
        for i in range(len(tail_list)):
            tail_i, tail_j = tail_list[i]
            while not is_touching((tail_i, tail_j), (next_i, next_j)):
                tail_i, tail_j = move_one_step((tail_i, tail_j), (next_i, next_j))
                if i == rope_len - 1:
                    visited.add((tail_i, tail_j))
            tail_list[i] = next_i, next_j = tail_i, tail_j
    return len(visited)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2022, 9)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
