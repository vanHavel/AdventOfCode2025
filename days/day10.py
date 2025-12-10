import sys

import pulp
from aocd import get_data
from util import astar

DAY = 10
YEAR = 2025

def parse(line: str) -> tuple[set[int], list[set[int]], tuple[int]]:
    parts = line.split(' ')
    goal = frozenset(index for index, ch in enumerate(parts[0][1:-1]) if ch == '#')
    moves = [frozenset(int(num) for num in part[1:-1].split(",")) for part in parts[1:-1]]
    joltage = tuple(int(num) for num in parts[-1][1:-1].split(","))
    return goal, moves, joltage


def part1(data: str) -> str:
    lines = data.splitlines()
    problems = [parse(line) for line in lines]
    ans = 0
    for goal, moves, _ in problems:
        a = astar.AStar(
            succ=lambda s: [(1, s ^ mv) for mv in moves],
            goal=lambda s: s == goal,
            h=lambda s: 0,
            return_path=False,
        )
        cost, _ = a.search(frozenset())
        ans += cost
    return str(ans)


def part2(data: str) -> str:
    lines = data.splitlines()
    problems = [parse(line) for line in lines]
    ans = 0

    for _, moves, joltage in problems:
        prob = pulp.LpProblem("MinMoves", pulp.LpMinimize)
        x = {}
        for j in range(len(moves)):
            x[j] = pulp.LpVariable(f"x_{j}", lowBound=0, upBound=max(joltage), cat='Integer')
        for i in range(len(joltage)):
            prob += pulp.lpSum(
                1 * x[j] for j in range(len(moves)) if i in moves[j]
            ) == joltage[i]
        prob += pulp.lpSum(x[j] for j in range(len(moves)))
        prob.solve()
        ans += int(pulp.value(prob.objective))

    return str(ans)


if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)
    input_data = get_data(day=DAY, year=YEAR)
    test_data = r"""[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
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
