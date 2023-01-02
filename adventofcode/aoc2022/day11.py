import functools
import itertools
import math
import operator
import re
from collections import OrderedDict
from dataclasses import dataclass
from typing import Callable
from typing import Iterator
from typing import List
from typing import Optional

from adventofcode.tools.input import read_puzzle_input

_MONKEY_PATTERN_STR = r"""Monkey (?P<index>\d+):
  Starting items: (?P<item_list>\d+(, \d+)*)
  Operation: new = old (?P<operation_operator>[-+\*/]) (?P<operation_argument>\d+|old)
  Test: divisible by (?P<test_modulo>\d+)
    If true: throw to monkey (?P<test_true>\d+)
    If false: throw to monkey (?P<test_false>\d+)"""
_MONKEY_PATTERN = re.compile(_MONKEY_PATTERN_STR)
_MONKEY_OPERATORS = {
    "*": operator.mul,
    "/": operator.truediv,
    "+": operator.add,
    "-": operator.sub,
}


@dataclass
class MonkeyTest:
    modulo: int
    true: int
    false: int

    def test(self, worry_level: int) -> int:
        return self.true if worry_level % self.modulo == 0 else self.false


@dataclass
class MonkeyOperation:
    operator: Callable[[int, int], int]
    argument: Optional[int]

    def inspect(self, worry_level: int) -> int:
        return (
            self.operator(worry_level, self.argument)
            if self.argument is not None
            else self.operator(worry_level, worry_level)
        )


@dataclass
class MonkeyData:
    index: int
    item_list: List[int]
    operation: MonkeyOperation
    test: MonkeyTest
    inspections: int = 0


def parse_monkey_data(monkey_data: str) -> MonkeyData:
    m = _MONKEY_PATTERN.match(monkey_data)
    if not m:
        raise ValueError("invalid input")
    (
        index,
        item_list,
        operation_op,
        operation_arg_str,
        test_modulo,
        test_true,
        test_false,
    ) = (
        int(m.group("index")),
        [int(x) for x in m.group("item_list").split(", ")],
        _MONKEY_OPERATORS[m.group("operation_operator")],
        m.group("operation_argument"),
        int(m.group("test_modulo")),
        int(m.group("test_true")),
        int(m.group("test_false")),
    )
    operation_arg = None if operation_arg_str == "old" else int(operation_arg_str)
    return MonkeyData(
        index=index,
        item_list=item_list,
        operation=MonkeyOperation(operator=operation_op, argument=operation_arg),
        test=MonkeyTest(modulo=test_modulo, true=test_true, false=test_false),
    )


def parse_puzzle_input(puzzle_input: List[str]) -> Iterator[MonkeyData]:
    puzzle_iter = iter(puzzle_input)
    while True:
        monkey_data = "\n".join(itertools.takewhile(len, puzzle_iter))
        if monkey_data == "":
            return
        yield parse_monkey_data(monkey_data)


def take_turns(
    monkey_map: OrderedDict[int, MonkeyData],
    update_worry_level: Callable[[int], int],
):
    for monkey in monkey_map.values():
        for worry_level in monkey.item_list:
            new_worry_level = update_worry_level(monkey.operation.inspect(worry_level))
            target_monkey = monkey.test.test(new_worry_level)
            monkey_map[target_monkey].item_list.append(new_worry_level)
            monkey.inspections += 1
        monkey.item_list.clear()


def evaluate_monkey_business(monkey_map: OrderedDict[int, MonkeyData]) -> int:
    first, second = sorted(monkey_map.values(), key=lambda x: -x.inspections)[:2]
    return first.inspections * second.inspections


def _floordiv(a: int, b: int) -> int:
    return a // b


def _mod(a: int, b: int) -> int:
    return a % b


def solve_part1(puzzle_input: List[str]) -> int:
    monkey_map = OrderedDict([(m.index, m) for m in parse_puzzle_input(puzzle_input)])
    update_worry_level = functools.partial(_floordiv, b=3)
    for _ in range(20):
        take_turns(monkey_map, update_worry_level)
    return evaluate_monkey_business(monkey_map)


def solve_part2(puzzle_input: List[str]) -> int:
    monkey_map = OrderedDict([(m.index, m) for m in parse_puzzle_input(puzzle_input)])
    relief = math.lcm(*(m.test.modulo for m in monkey_map.values()))
    update_worry_level = functools.partial(_mod, b=relief)
    for _ in range(10000):
        take_turns(monkey_map, update_worry_level)
    return evaluate_monkey_business(monkey_map)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2022, 11)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
