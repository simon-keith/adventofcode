import re
from typing import Iterator
from typing import List
from typing import Set
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input

_CARD_PTRN = re.compile(r"Card\s+\d+:\s+(?P<winning>[\d\s]+)\s+\|\s+(?P<own>[\d\s]+)")


def iter_cards(puzzle_input: List[str]) -> Iterator[Tuple[Set[int], Set[int]]]:
    for line in puzzle_input:
        m = _CARD_PTRN.match(line)
        if m:
            winning_set = set(int(x) for x in m.group("winning").split())
            own_set = set(int(x) for x in m.group("own").split())
            yield winning_set, own_set


def solve_part1(puzzle_input: List[str]) -> int:
    union_iter = (w & o for w, o in iter_cards(puzzle_input))
    return sum((2 ** (len(u) - 1) for u in union_iter if len(u) > 0))


def solve_part2(puzzle_input: List[str]) -> int:
    card_count = [1] * len(puzzle_input)
    for i, (w, o) in enumerate(iter_cards(puzzle_input)):
        for j in range(len(w & o)):
            card_count[i + j + 1] += card_count[i]
    return sum(card_count)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2023, 4)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
