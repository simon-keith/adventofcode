from importlib import resources
from typing import List


def read_puzzle_input(year: int, day: int) -> List[str]:
    package = f"adventofcode.aoc{year:d}.data"
    resource = f"day{day:02d}.txt"
    with resources.open_text(package, resource) as f:
        return f.read().strip().split("\n")
