import collections
from itertools import islice, pairwise
from typing import Any, Generator, Iterable, List, Tuple

from adventofcode.tools.input import read_puzzle_input


def sliding_window(
    iterable: Iterable[Any],
    n: int,
) -> Generator[Tuple[Any], None, None]:
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def _parse(puzzle_input: List[str]) -> Generator[int, None, None]:
    return (int(line) for line in puzzle_input)


def _count_positive_diffs(iterable: Iterable[int]) -> int:
    return sum(current > previous for previous, current in pairwise(iterable))


def solve_part1(puzzle_input: List[str]) -> int:
    iterable = _parse(puzzle_input)
    return _count_positive_diffs(iterable)


def solve_part2(puzzle_input: List[str]) -> int:
    iterable = (sum(w) for w in sliding_window(_parse(puzzle_input), 3))
    return _count_positive_diffs(iterable)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 1)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
