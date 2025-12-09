import functools
import sys

from aocd import get_data
from util import grid

DAY = 9
YEAR = 2025

edges: list[grid.Edge] = []

@functools.cache
def is_on(point: grid.Pos, edge: grid.Edge) -> bool:
    (x1, y1), (x2, y2) = edge
    if x1 == x2:  # vertical edge
        if point[0] != x1:
            return False
        return min(y1, y2) <= point[1] <= max(y1, y2)
    else:  # horizontal edge
        if point[1] != y1:
            return False
        return min(x1, x2) <= point[0] <= max(x1, x2)

@functools.cache
def is_inside(point: grid.Pos) -> bool:
    crossings = 0
    px, py = point
    for e in edges:
        if is_on(point, e):
            return True
        if e[0][0] == e[1][0]:  # vertical edge
            x = e[0][0]
            miny = min(e[0][1], e[1][1])
            maxy = max(e[0][1], e[1][1])
            # slight perturbation to avoid corner cases
            if px < x and miny <= py + 0.1 <= maxy:
                crossings += 1
    return crossings % 2 == 1


def part1(data: str) -> str:
    lines = data.splitlines()
    points = [(int(x), int(y)) for x, y in (line.split(',') for line in lines)]
    ans = max([
        (1 + abs(x1 - x2)) * (1 + abs(y1 - y2))
        for (x1, y1) in points
        for (x2, y2) in points
    ])
    return str(ans)


def part2(data: str) -> str:
    lines = data.splitlines()
    points = [(int(x), int(y)) for x, y in (line.split(',') for line in lines)]
    points.append(points[0])
    edges.clear()
    edges.extend([(p1, p2) for p1, p2 in zip(points, points[1:])])
    vertical_edges = sorted((e for e in edges if e[0][0] == e[1][0]), key=lambda e: e[0][0])
    horizontal_edges = sorted((e for e in edges if e[0][1] == e[1][1]), key=lambda e: e[0][1])
    ans = 0
    for (x1, y1) in points:
        for (x2, y2) in points:
            if x1 == x2 or y1 == y2:
                continue
            area = (1 + abs(x1 - x2)) * (1 + abs(y1 - y2))
            if area <= ans:
                continue
            # check other corners
            points_to_check = [(x1, y2), (x2, y1)]
            horizontal_borders = [((x1, y1), (x2, y1)), ((x1, y2), (x2, y2))]
            vertical_borders = [((x1, y1), (x1, y2)), ((x2, y1), (x2, y2))]
            for (hx1, hy), (hx2, _) in horizontal_borders:
                for (vx, vy1), (_, vy2) in vertical_edges:
                    if min(vy1, vy2) <= hy <= max(vy1, vy2) and min(hx1, hx2) <= vx <= max(hx1, hx2) and vx < max(x1, x2):
                        # intersection points, plus eps to avoid edge cases
                        points_to_check.append((vx + 0.1, hy))
            for (vx, vy1), (_, vy2) in vertical_borders:
                for (hx1, hy), (hx2, _) in horizontal_edges:
                    if min(hx1, hx2) <= vx <= max(hx1, hx2) and min(vy1, vy2) <= hy <= max(vy1, vy2) and hy < max(y1, y2):
                        # intersection points, plus eps to avoid edge cases
                        points_to_check.append((vx, hy + 0.1))
            if all(is_inside(point) for point in points_to_check):
                ans = max(ans, area)

    return str(ans)



if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)
    input_data = get_data(day=DAY, year=YEAR)
    test_data = r"""7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
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