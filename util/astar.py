import heapq
from typing import Callable, Dict, Iterable, Set


class AStar[S]:
    def __init__(
        self,
        succ: Callable[[S], Iterable[tuple[int, S]]],
        goal: Callable[[S], bool],
        h: Callable[[S], int],
        return_path: bool = True,
    ):
        self.succ = succ
        self.goal = goal
        self.h = h
        self.return_path = return_path

    def search(self, start: S) -> None | int | tuple[int, list[S]]:
        costs = {start: 0}
        preds: Dict[S, S] = {} if self.return_path else None
        closed: Set[S] = set()
        pq: list[tuple[int, S]] = [(0, start)]

        while pq:
            f, u = heapq.heappop(pq)

            if u in closed:
                continue
            closed.add(u)

            if self.goal(u):
                if not self.return_path:
                    return f, []

                path = [u]
                cur = u
                while cur in preds:
                    path.append(preds[cur])
                    cur = preds[cur]
                return f, list(reversed(path))

            for d, v in self.succ(u):
                if v in closed:
                    continue

                g = costs[u] + d
                if v not in costs or costs[v] > g:
                    costs[v] = g
                    if self.return_path:
                        preds[v] = u
                    f_new = g + self.h(v)
                    heapq.heappush(pq, (f_new, v))

        return None

