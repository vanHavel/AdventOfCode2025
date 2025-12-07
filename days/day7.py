import functools
import sys
from collections import defaultdict

from aocd import get_data, submit

from util import grid

DAY = 7
YEAR = 2025

succs = defaultdict(list)

def part1(data: str) -> str:
    g = grid.from_block(data)
    start, = g.where(lambda x: x == 'S')
    g.mark(start, 'filled', True)
    splits = 0
    for y in range(1, g.n):
        for x in range(g.m):
            filled = False
            if g.meta((y - 1, x), 'filled') and g.get((y - 1, x)) != '^':
                filled = True
                if g.get((y, x)) == '^':
                    splits += 1
            if x > 0 and g.get((y - 1, x - 1)) == '^' and g.meta((y - 1, x - 1), 'filled'):
                filled = True
            if x + 1 < g.m and g.get((y - 1, x + 1)) == '^' and g.meta((y - 1, x + 1), 'filled'):
                filled = True
            if filled:
                g.mark((y, x), 'filled', True)
    return str(splits)

def part2(data: str) -> str:
    g = grid.from_block(data)
    start, = g.where(lambda x: x == 'S')
    # (sy, sx) is points to first splitter
    sy, sx = start
    while g.get((sy, sx)) != '^':
        sy += 1

    for (y, x) in g.positions():
        if g.get((y, x)) == '^':
            # get right successor
            if x + 1 < g.m:
                cy = y + 1
                while cy < g.n and g.get((cy, x + 1)) != '^':
                    cy += 1
                if cy < g.n:
                    succs[(y, x)].append((cy, x + 1))
            # get left successor
            if x - 1 >= 0:
                cy = y + 1
                while cy < g.n and g.get((cy, x - 1)) != '^':
                    cy += 1
                if cy < g.n:
                    succs[(y, x)].append((cy, x - 1))
    ans = count_paths((sy, sx))
    return str(ans)

@functools.cache
def count_paths(pos: grid.Pos) -> int:
    if succs[pos] == []:
        return 2
    if len(succs[pos]) == 1:
        return count_paths(succs[pos][0]) + 1
    return sum(count_paths(s) for s in succs[pos])


if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)
    input_data = get_data(day=DAY, year=YEAR)
    test_data = r""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
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
