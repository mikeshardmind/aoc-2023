import re
from collections import defaultdict
from functools import reduce
from itertools import product
from operator import mul
from pathlib import Path

path = Path(__file__).parent.with_name("inputs") / "day3.txt"


def solver() -> tuple[int, int]:
    with path.open(mode="r", encoding="utf-8") as fp:
        grid = fp.read().splitlines()

    ret_one = 0
    adjacencies: dict[tuple[int, int], list[int]] = defaultdict(list)
    for row_n, line in enumerate(grid):
        for m in re.finditer(r"\d+", line):
            r1_added = False
            for r, c in (
                (row_n, m.start() - 1),
                (row_n, m.end()),
                *((row_n + offset, col) for col, offset in product(range(m.start() - 1, m.end() + 1), (-1, 1))),
            ):
                try:
                    if grid[r][c] != ".":
                        v = int(m.group())
                        if grid[r][c] == "*":
                            adjacencies[r, c].append(v)
                        if not r1_added:
                            r1_added = True
                            ret_one += v
                except IndexError:
                    pass
    return ret_one, sum(reduce(mul, vals) for vals in adjacencies.values() if len(vals) == 2)


if __name__ == "__main__":
    print(solver())
