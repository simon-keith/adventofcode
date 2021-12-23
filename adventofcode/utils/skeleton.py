from importlib.util import find_spec
from pathlib import Path
from typing import Tuple

_SOLUTION = """from typing import List

from adventofcode.utils.input import read_puzzle_input


def solve_part1(puzzle_input: List[str]) -> int:
    pass


def solve_part2(puzzle_input: List[str]) -> int:
    pass


if __name__ == "__main__":
    puzzle_input = read_puzzle_input({year:d}, {day:d})
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
"""

_TESTS = """from adventofcode.{module}.{solution} import solve_part1, solve_part2
from pytest import fixture


@fixture
def puzzle_input():
    return []


def test_part1(puzzle_input):
    assert solve_part1(puzzle_input) is None


def test_part2(puzzle_input):
    assert solve_part2(puzzle_input) is None
"""


def format_module(year: int) -> str:
    return f"aoc{year:d}"


def format_solution(day: int) -> str:
    return f"day{day:02d}"


def format_test(day: int) -> str:
    solution = format_solution(day)
    return f"test_{solution}"


def generate_code(year: int, day: int) -> Tuple[str, str]:
    module = format_module(year)
    solution = format_solution(day)
    return _SOLUTION.format(year=year, day=day), _TESTS.format(
        module=module,
        solution=solution,
    )


def write_files(year: int, day: int) -> Tuple[Path, Path]:
    module = format_module(year)

    # get solution path
    solution_module_name = f"adventofcode.{module}"
    solution_module_spec = find_spec(solution_module_name)
    solution_module_path = Path(solution_module_spec.origin).parent
    solution = format_solution(day)
    solution_path = solution_module_path / f"{solution}.py"

    # get test path
    test_module_name = f"tests.{module}"
    test_module_spec = find_spec(test_module_name)
    test_module_path = Path(test_module_spec.origin).parent
    test = format_test(day)
    test_path = test_module_path / f"{test}.py"

    # write code
    solution_code, test_code = generate_code(year, day)
    with open(solution_path, "w") as f:
        f.write(solution_code)
    with open(test_path, "w") as f:
        f.write(test_code)
    return solution_path, test_path
