import sys

from aocd import get_data, submit

DAY = 5
YEAR = 2025

def parse(data: str) -> tuple[list[tuple[int, int]], list[int]]:
    sections = data.split('\n\n')
    ranges = []
    for line in sections[0].splitlines():
        a, b = line.split('-')
        ranges.append((int(a), int(b)))
    queries = [int(x) for x in sections[1].splitlines()]
    return ranges, queries

def part1(data: str) -> str:
    ranges, queries = parse(data)
    ans = 0
    for query in queries:
        if any(a <= query <= b for a, b in ranges):
            ans += 1
    return str(ans)


def part2(data: str) -> str:
    ranges, _ = parse(data)
    merged = []
    ranges = sorted(ranges)
    cur = ranges[0]
    for range in ranges[1:]:
        if range[0] <= cur[1]:
            cur = (cur[0], max(cur[1], range[1]))
        else:
            merged.append(cur)
            cur = range
    merged.append(cur)
    ans = 0
    for l, r in merged:
        ans += r - l + 1
    return str(ans)


if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)
    input_data = get_data(day=DAY, year=YEAR)
    test_data = r"""3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
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
