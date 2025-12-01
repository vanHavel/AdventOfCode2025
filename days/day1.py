import sys

from aocd import get_data, submit

DAY = 1
YEAR = 2025


def part1(data: str) -> str:
    lines = data.splitlines()
    cur = 50
    ans = 0
    for line in lines:
        fact = (-1) if line[0] == "L" else 1
        add = int(line[1:])
        cur += add * fact
        cur %= 100
        if cur == 0:
            ans += 1
    return str(ans)


def part2(data: str) -> str:
    lines = data.splitlines()
    cur = 50
    ans = 0
    for line in lines:
        prev = cur
        fact = (-1) if line[0] == "L" else 1
        add = int(line[1:])
        ans += add // 100
        add %= 100
        if add != 0:
            cur += add * fact
            if (cur <= 0 and prev != 0) or cur >= 100:
                ans += 1
            cur %= 100
    return str(ans)


if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)
    input_data = get_data(day=DAY, year=YEAR)
    test_data = r"""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
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
