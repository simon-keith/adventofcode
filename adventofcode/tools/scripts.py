import argparse

import adventofcode.tools.run as run
import adventofcode.tools.skeleton as sklt


def _get_puzzle_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate the skeleton for the given year and day.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "year",
        type=int,
        help="Advent of Code puzzle year",
    )
    parser.add_argument(
        "day",
        type=int,
        help="Advent of Code puzzle day",
    )
    return parser


def skeleton():
    parser = _get_puzzle_parser()
    args = parser.parse_args()
    paths = sklt.write_files(year=args.year, day=args.day)
    for p in paths:
        print(p)


def solve():
    parser = _get_puzzle_parser()
    args = parser.parse_args()
    try:
        results = run.solve(year=args.year, day=args.day)
    except ModuleNotFoundError:
        return
    for i, r in enumerate(results):
        part = i + 1
        print(f"# {args.year:d}.{args.day:02d}.{part:d}")
        print(r)


def timeit():
    parser = _get_puzzle_parser()
    args = parser.parse_args()
    try:
        t1, t2 = run.timeit(year=args.year, day=args.day)
    except ModuleNotFoundError:
        return
    print(f"{args.year:d}\t{args.day:02d}\t{t1:.6f}\t{t2:.6f}")
