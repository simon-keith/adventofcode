from collections import deque
from typing import Deque, List, Tuple

from adventofcode.tools.input import read_puzzle_input

_CYCLE_LENGTH = 7
_NEW_TIMER_VALUE = 8


def _parse(puzzle_input: List[str]) -> Tuple[int, ...]:
    (data,) = puzzle_input
    return tuple(int(x) for x in data.split(","))


def _init_timer(initial_state: Tuple[int, ...]) -> Deque[int]:
    timer = [0] * (max(_NEW_TIMER_VALUE, _CYCLE_LENGTH) + 1)
    for s in initial_state:
        timer[s] += 1
    return deque(timer)


def _inc_timer(timer: Deque[int]):
    timer.rotate(-1)
    timer[_CYCLE_LENGTH - 1] += timer[_NEW_TIMER_VALUE]


def _simulate(population: Tuple[int, ...], epoch: int) -> int:
    timer = _init_timer(population)
    for _ in range(epoch):
        _inc_timer(timer)
    return sum(timer)


def solve_part1(puzzle_input: List[str]) -> int:
    population = _parse(puzzle_input)
    return _simulate(population, 80)


def solve_part2(puzzle_input: List[str]) -> int:
    population = _parse(puzzle_input)
    return _simulate(population, 256)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 6)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
