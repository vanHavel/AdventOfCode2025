import functools
import sys

from aocd import get_data

DAY = 3
YEAR = 2025

@functools.cache
def get_highest(line: str, select: int, start: int) -> int:
    if select == 0:
        return 0
    if start >= len(line):
        return -1000000000000000
    digit = int(line[start])
    rec = get_highest(line, select - 1, start + 1)
    c1 = digit * (10 ** (select - 1)) + rec
    c2 = get_highest(line, select, start + 1)
    best = max(c1, c2)
    return best

def part1(data: str) -> str:
    lines = data.splitlines()
    ans = 0
    for line in lines:
        ans += get_highest(line, 2, 0)
    return str(ans)


def part2(data: str) -> str:
    lines = data.splitlines()
    ans = 0
    for line in lines:
        ans += get_highest(line, 12, 0)
    return str(ans)


if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)
    input_data = get_data(day=DAY, year=YEAR)
    test_data = r"""987654321111111
811111111111119
234234234234278
818181911112111"""
    test1 = part1(test_data)
    ans1 = part1(input_data)
    print(test1)
    print(ans1)
    # submit(answer=ans1, day=DAY, year=YEAR, part=1)
    test2 = part2(test_data)
    ans2 = part2(input_data)
    print(test2)
    print(ans2)
    # submit(answer=ans2, day=DAY, year=YEAR, part=2)
