import functools
import sys

from aocd import get_data, submit

DAY = 11
YEAR = 2025

adj = {}

def parse(data: str) -> None:
    lines = data.splitlines()
    adj.clear()
    for line in lines:
        left, right = line.split(": ")
        neighbors = right.split(" ")
        adj[left] = neighbors

@functools.cache
def count_paths(node: str) -> int:
    if node == "out":
        return 1
    total = 0
    for neighbor in adj[node]:
        total += count_paths(neighbor)
    return total

@functools.cache
def count_paths2(node: str, dac: bool, fft: bool) -> int:
    if node == "out":
        return int(not dac and not fft)
    total = 0
    for neighbor in adj[node]:
        if neighbor == "dac":
            total += count_paths2(neighbor, False, fft)
        elif neighbor == "fft":
            total += count_paths2(neighbor, dac, False)
        else:
            total += count_paths2(neighbor, dac, fft)
    return total


def part1(data: str) -> str:
    parse(data)
    count_paths.cache_clear()
    ans = count_paths("you")
    return str(ans)


def part2(data: str) -> str:
    parse(data)
    count_paths2.cache_clear()
    ans = count_paths2("svr", True, True)
    return str(ans)


if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)
    input_data = get_data(day=DAY, year=YEAR)
    test_data = r"""aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""
    test1 = part1(test_data)
    ans1 = part1(input_data)
    print(test1)
    print(ans1)
    # submit(answer=ans1, day=DAY, year=YEAR, part=1)
    test_data = r"""svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""
    test2 = part2(test_data)
    ans2 = part2(input_data)
    print(test2)
    print(ans2)
    # submit(answer=ans2, day=DAY, year=YEAR, part=2)
