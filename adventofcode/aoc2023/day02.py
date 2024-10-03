import re
from dataclasses import dataclass
from typing import List
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input

_GAME_PATTERN = re.compile(r"Game (?P<id>\d+): (?P<draw_list>.*)")
_DRAW_PATTERN = re.compile(r"(?P<count>\d+) (?P<color>\w+)")


@dataclass
class Draw:
    red: int
    green: int
    blue: int

    def filter(self, max_red: int, max_green: int, max_blue: int) -> bool:
        return self.red <= max_red and self.green <= max_green and self.blue <= max_blue

    def get_power(self) -> int:
        return self.red * self.green * self.blue


@dataclass
class Game:
    id: int
    draw_list: Tuple[Draw, ...]

    def get_max_draw(self) -> Draw:
        return Draw(
            red=max(d.red for d in self.draw_list),
            green=max(d.green for d in self.draw_list),
            blue=max(d.blue for d in self.draw_list),
        )


def _parse_draw(draw: str) -> Draw:
    draw_map = {
        m.group("color"): int(m.group("count"))
        for m in (
            _DRAW_PATTERN.match(color_count.strip()) for color_count in draw.split(",")
        )
        if m
    }
    return Draw(
        red=draw_map.get("red", 0),
        green=draw_map.get("green", 0),
        blue=draw_map.get("blue", 0),
    )


def parse_game(line: str) -> Game:
    game_match = _GAME_PATTERN.match(line)
    if not game_match:
        raise ValueError("invalid game record")
    return Game(
        id=int(game_match.group("id")),
        draw_list=tuple(
            _parse_draw(d) for d in game_match.group("draw_list").split(";")
        ),
    )


def solve_part1(puzzle_input: List[str]) -> int:
    return sum(
        game.id
        for game in (parse_game(line) for line in puzzle_input)
        if game.get_max_draw().filter(12, 13, 14)
    )


def solve_part2(puzzle_input: List[str]) -> int:
    return sum(parse_game(line).get_max_draw().get_power() for line in puzzle_input)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2023, 2)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
