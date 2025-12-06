import sys
from dataclasses import dataclass

from aocd import get_data, submit

DAY = 6
YEAR = 2025


@dataclass
class Problem:
    numbers: list[int]
    op: str

def solve_problems(problems: list[Problem]) -> int:
    ans = 0
    for problem in problems:
        if problem.op == '+':
            res = sum(problem.numbers)
        elif problem.op == '*':
            res = 1
            for num in problem.numbers:
                res *= num
        ans += res
    return ans

def part1(data: str) -> str:
    lines = data.splitlines()
    nums = [line.split() for line in lines[:-1]]
    ops = lines[-1].split()
    problems = []
    for i in range(len(ops)):
        problem = Problem(op=ops[i], numbers=[int(nums[row][i]) for row in range(len(nums))])
        problems.append(problem)
    ans = solve_problems(problems)
    return str(ans)

def part2(data: str) -> str:
    lines = data.splitlines()
    problem_indices = [i for i in range(len(lines[-1])) if lines[-1][i] in '+*'] + [len(lines[-1]) + 1] #sentinel
    problems = []
    for i in range(len(problem_indices) - 1):
        start = problem_indices[i]
        end = problem_indices[i + 1]
        op = lines[-1][start]
        problem_numbers = [int("".join([line[col] for line in lines[:-1]])) for col in range(start, end - 1)]
        problem = Problem(op=op, numbers=problem_numbers)
        problems.append(problem)
    ans = solve_problems(problems)
    return str(ans)

if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)
    input_data = get_data(day=DAY, year=YEAR)
    test_data = r"""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""
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
