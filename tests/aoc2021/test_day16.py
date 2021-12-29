from adventofcode.aoc2021.day16 import solve_part1, solve_part2
from pytest import fixture, mark


@fixture
def puzzle_input(request):
    match request.param:
        case "1a":
            return ["8A004A801A8002F478"]
        case "1b":
            return ["620080001611562C8802118E34"]
        case "1c":
            return ["C0015000016115A2E0802F182340"]
        case "1d":
            return ["A0016C880162017C3686B18A3D4780"]
        case "2a":
            return ["C200B40A82"]
        case "2b":
            return ["04005AC33890"]
        case "2c":
            return ["880086C3E88112"]
        case "2d":
            return ["CE00C43D881120"]
        case "2e":
            return ["D8005AC2A8F0"]
        case "2f":
            return ["F600BC2D8F"]
        case "2g":
            return ["9C005AC2F8F0"]
        case "2h":
            return ["9C0141080250320F1802104A08"]
        case _:
            raise ValueError("invalid fixture parameter")


@mark.parametrize(
    "puzzle_input,expected",
    [("1a", 16), ("1b", 12), ("1c", 23), ("1d", 31)],
    indirect=["puzzle_input"],
)
def test_part1(puzzle_input, expected):
    assert solve_part1(puzzle_input) == expected


@mark.parametrize(
    "puzzle_input,expected",
    [
        ("2a", 3),
        ("2b", 54),
        ("2c", 7),
        ("2d", 9),
        ("2e", 1),
        ("2f", 0),
        ("2g", 0),
        ("2h", 1),
    ],
    indirect=["puzzle_input"],
)
def test_part2(puzzle_input, expected):
    assert solve_part2(puzzle_input) == expected
