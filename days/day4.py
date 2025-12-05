import sys

from aocd import get_data, submit
from util import grid

DAY = 4
YEAR = 2025


def iter(g: grid.Grid) -> int:
    updates = []
    for pos in g.positions():
        y, x = pos
        if g.get(pos) != '@':
            continue
        rolls = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0 or not g.inside((y + dy, x + dx)):
                    continue
                if g.get((y + dy, x + dx)) == '@':
                    rolls += 1
        if rolls < 4:
            updates.append((y, x))
    for pos in updates:
        g.set(pos, '.')
    return len(updates)

def part1(data: str) -> str:
    g = grid.from_block(data)
    ans = iter(g)
    return str(ans)


def part2(data: str) -> str:
    g = grid.from_block(data)
    ans = 0
    while cur := iter(g):
        ans += cur
    return str(ans)


if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)
    input_data = get_data(day=DAY, year=YEAR)
    test_data = r"""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
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
