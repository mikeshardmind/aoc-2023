from math import inf
from operator import itemgetter
from pathlib import Path

from ahocorasick_rs import AhoCorasick, MatchKind

path = Path(__file__).parent.with_name("inputs") / "day1.txt"

def part_one() -> int:
    getter = itemgetter(0, -1)
    with path.open(mode="r", encoding="utf-8") as fp:
        return sum(map(int, ("".join(getter([*filter(str.isdigit, line)])) for line in fp.readlines())))

nums = {
    '0': 0, 'zero': 0, '1': 1, 'one': 1,
    '2': 2, 'two': 2, '3': 3, 'three': 3,
    '4': 4, 'four': 4, '5': 5, 'five': 5,
    '6': 6, 'six': 6, '7': 7, 'seven': 7,
    '8': 8, 'eight': 8, '9': 9, 'nine': 9
}

first_finder = AhoCorasick(nums.keys(), matchkind=MatchKind.LeftmostFirst)
last_finder = AhoCorasick(nums.keys(), matchkind=MatchKind.Standard)

def part_two() -> int:
    total = 0
    with path.open(mode="r", encoding="utf-8") as fp:
        for line in fp.readlines():
            total += nums[first_finder.find_matches_as_strings(line)[0]] * 10
            total += nums[last_finder.find_matches_as_strings(line, overlapping=True)[-1]]
    return total


def part_two_stdlib() -> int:
    total = 0
    with path.open(mode="r", encoding="utf-8") as fp:
        for line in fp.readlines():
            total += nums[min(nums.keys(), key=lambda k: idx if (idx:=line.find(k)) >= 0 else inf)] * 10
            total += nums[max(nums.keys(), key=line.rfind)]
    return total


if __name__ == "__main__":
    print(part_one(), part_two(), part_two_stdlib())