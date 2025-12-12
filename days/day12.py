import sys

from aocd import get_data, submit
from util import grid

DAY = 12
YEAR = 2025

def parse(data: str) -> tuple[list[list[bool]], list[tuple[grid.Pos, list[int]]]]:
    lines = data.splitlines()
    shapes = []
    i = 0
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        if "x" in lines[i]:
            break
        i += 1
        shape = []
        while i < len(lines) and lines[i].strip():
            shape.append([ch == '#' for ch in lines[i]])
            i += 1
        shapes.append(shape)

    queries = []
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        size_part, shape_part = lines[i].split(": ")
        h, w = map(int, size_part.split("x"))
        shape_counts = list(map(int, shape_part.split(" ")))
        queries.append(((h, w), shape_counts))
        i += 1
    return shapes, queries


def part1(data: str) -> str:
    shapes, queries = parse(data)
    ans = 0
    for query in queries:
        size, shape_counts = query
        h, w = size
        total_spaces = h * w
        shape_sizes = [sum(sum(1 for cell in row if cell) for row in shape) for shape in shapes]
        total_requested = sum([
            shape_sizes[i] * shape_counts[i] for i in range(len(shapes))
        ])
        if total_requested <= total_spaces:
            ans += 1
    return str(ans)


def part2(data: str) -> str:
    lines = data.splitlines()
    return str(lines)


if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)
    input_data = get_data(day=DAY, year=YEAR)
    test_data = r"""0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""
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
