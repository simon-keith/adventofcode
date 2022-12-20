import collections
import collections.abc
import math
from dataclasses import dataclass
from itertools import islice
from typing import Iterable
from typing import List
from typing import Optional
from typing import Tuple

from adventofcode.tools.input import read_puzzle_input


def parse_puzzle_input(puzzle_input: List[str]) -> str:
    (transmission,) = puzzle_input
    return transmission


def collect(it: Iterable[str]) -> str:
    return "".join(it)


@dataclass
class Packet:
    version: int
    type_id: int
    literal: Optional[int] = None
    sub_packets: Tuple["Packet", ...] = ()

    def __iter__(self):
        yield self
        for p in self.sub_packets:
            yield from p

    def get_value(self) -> int:
        match self.type_id:
            case 0:
                return sum(p.get_value() for p in self.sub_packets)
            case 1:
                return math.prod(p.get_value() for p in self.sub_packets)
            case 2:
                return min(p.get_value() for p in self.sub_packets)
            case 3:
                return max(p.get_value() for p in self.sub_packets)
            case 4:
                if self.literal is None:
                    raise ValueError("literal value is not defined")
                return self.literal
            case 5:
                s1, s2 = self.sub_packets
                return int(s1.get_value() > s2.get_value())
            case 6:
                s1, s2 = self.sub_packets
                return int(s1.get_value() < s2.get_value())
            case 7:
                s1, s2 = self.sub_packets
                return int(s1.get_value() == s2.get_value())
            case _:
                raise ValueError("invalid packet type")


class Transmission(collections.abc.Sized, collections.abc.Iterator):
    def __init__(self, data: str) -> None:
        num_bits = len(data) * 4
        binary_data = bin(int(data, 16))[2:].zfill(num_bits)
        self._i = 0
        self._n = len(binary_data)
        self._it = iter(binary_data)

    def __len__(self) -> int:
        return self._n - self._i

    def __next__(self) -> str:
        s = next(self._it)
        self._i += 1
        return s

    def _fetch(self, size: int) -> str:
        c = collect(islice(self._it, size))
        self._i += len(c)
        return c

    def _get_next_literal(self) -> int:
        literal = ""
        while len(self) > 0:
            group = self._fetch(5)
            if len(group) != 5:
                raise ValueError("group is incomplete")
            literal += "".join(group[1:])
            if group[0] == "0":
                return int(literal, 2)
        raise ValueError("the last group must start with 0")

    def _get_next_header(self) -> Tuple[int, int]:
        header = tuple(self._fetch(3) for _ in range(2))
        if not all(len(h) == 3 for h in header):
            raise ValueError("header is incomplete")
        version, type_id = tuple(int(h, 2) for h in header)
        return version, type_id

    def decode(self) -> Packet:
        version, type_id = self._get_next_header()
        if type_id == 4:
            literal = self._get_next_literal()
            return Packet(version=version, type_id=type_id, literal=literal)
        sub_packets = []
        if next(self) == "0":
            bits_to_read = int(collect(islice(self, 15)), 2)
            length_to_reach = len(self) - bits_to_read
            while length_to_reach < len(self):
                sub_packets.append(self.decode())
        else:
            packets_to_decode = int(collect(islice(self, 11)), 2)
            for _ in range(packets_to_decode):
                sub_packets.append(self.decode())
        return Packet(version=version, type_id=type_id, sub_packets=tuple(sub_packets))


def solve_part1(puzzle_input: List[str]) -> int:
    data = parse_puzzle_input(puzzle_input)
    packet = Transmission(data).decode()
    return sum(p.version for p in packet)


def solve_part2(puzzle_input: List[str]) -> int:
    data = parse_puzzle_input(puzzle_input)
    packet = Transmission(data).decode()
    return packet.get_value()


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(2021, 16)
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))
