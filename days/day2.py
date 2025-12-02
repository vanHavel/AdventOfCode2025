import sys

from aocd import get_data, submit

DAY = 2
YEAR = 2025

def get_next_invalid_number(n: int, p: int) -> int:
    # Returns the next number >= n that consists of p identical parts
    s = str(n)
    d = len(s)
    h = d // p
    # we need more digits
    if d % p != 0:
        next = ("1" + "0" * h) * p
        return int(next)
    else:
        parts = [s[i * h:(i + 1) * h] for i in range(p)]
        # all parts are identical
        if all(part == parts[0] for part in parts):
            return n
        # if the first different part is smaller -> repeat the first part
        for i in range(1, p):
            if parts[i] > parts[0]:
                break
            if parts[i] < parts[0]:
                return int(parts[0] * p)
        # need to increment the first part
        inc = str(int(parts[0]) + 1)
        return int(inc * p)

def part1(data: str) -> str:
    ranges = [(low, hi) for low, hi in (map(int, range.split("-")) for range in data.split(","))]
    ans = 0
    for low, hi in ranges:
        cur = get_next_invalid_number(low, 2)
        while cur <= hi:
            ans += cur
            cur = get_next_invalid_number(cur + 1, 2)
    return str(ans)


def part2(data: str) -> str:
    ranges = [(low, hi) for low, hi in (map(int, range.split("-")) for range in data.split(","))]
    ans = 0
    for low, hi in ranges:
        candidates = [get_next_invalid_number(low, p) for p in range(2, 11)]
        cur = min(candidates)
        while cur <= hi:
            ans += cur
            candidates = [get_next_invalid_number(cur + 1, p) for p in range(2, 11)]
            cur = min(candidates)
    return str(ans)

if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)
    input_data = get_data(day=DAY, year=YEAR)
    test_data = r"""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
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
