import sys

from aocd import get_data, submit
from util import grid3, dsu

DAY = 8
YEAR = 2025


def part1(data: str, connections: int) -> str:
    lines = data.splitlines()
    n = len(lines)
    uf = dsu.DSU(n)
    points = [tuple(map(int, line.split(','))) for line in lines]
    distances = [(i, j, grid3.squared_distance(points[i], points[j])) for i in range(n) for j in range(i + 1, n)]
    distances.sort(key=lambda x: x[2])
    for i in range(connections):
        a, b, d = distances[i]
        uf.union(a, b)
    roots = {uf.find(i) for i in range(n)}
    sizes = [uf.get_size(r) for r in roots]
    s1, s2, s3 = sorted(sizes, reverse=True)[:3]
    return str(s1 * s2 * s3)


def part2(data: str) -> str:
    lines = data.splitlines()
    n = len(lines)
    uf = dsu.DSU(n)
    points = [tuple(map(int, line.split(','))) for line in lines]
    distances = [(i, j, grid3.squared_distance(points[i], points[j])) for i in range(n) for j in range(i + 1, n)]
    distances.sort(key=lambda x: x[2])
    for i in range(len(distances)):
        a, b, d = distances[i]
        uf.union(a, b)
        if uf.get_num_sets() == 1:
            x1, x2 = points[a][0], points[b][0]
            return str(x1 * x2)

if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)
    input_data = get_data(day=DAY, year=YEAR)
    test_data = r"""162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
    test1 = part1(test_data, 10)
    ans1 = part1(input_data, 1000)
    print(test1)
    print(ans1)
    # submit(answer=ans1, day=DAY, year=YEAR, part=1)
    test2 = part2(test_data)
    ans2 = part2(input_data)
    print(test2)
    print(ans2)
    # submit(answer=ans2, day=DAY, year=YEAR, part=2)
