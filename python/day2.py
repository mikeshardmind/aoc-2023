from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterator
from functools import reduce
from operator import mul
from pathlib import Path

path = Path(__file__).parent.with_name("inputs") / "day2.txt"

GameNumber = int
ColorCounts = dict[str, int]
Game = tuple[GameNumber, ColorCounts]


def parse_gamerow(row: str) -> Game:
    gamenstr, countstr = row.split(":", maxsplit=1)
    gn = int("".join(filter(str.isdigit, gamenstr)))
    cs: ColorCounts = defaultdict(int)
    for pull in countstr.split(";"):
        for sec in pull.split(","):
            c, col = sec.strip().split(" ")
            cs[col] = max(int(c), cs[col])
    return gn, cs


def gamerow_iterator() -> Iterator[Game]:
    with path.open(mode="r", encoding="utf-8") as fp:
        for row in fp.readlines():
            yield parse_gamerow(row.strip())


def part_one() -> int:
    return sum(
        game_num
        for game_num, game in gamerow_iterator()
        if game["red"] <= 12 and game["blue"] <= 14 and game["green"] <= 13
    )


def part_two() -> int:
    return sum(reduce(mul, filter(None, game.values())) for _game_num, game in gamerow_iterator())


if __name__ == "__main__":
    print(part_one(), part_two())
