import sys

# Ajuste do limite de recursão para grafos de grande profundidade (até 10^5 vértices)
sys.setrecursionlimit(300000)

from algs4.digraph import Digraph
from checkposts_solver import CheckpostsSolver


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            tokens = f.read().split()
    else:
        tokens = sys.stdin.read().split()

    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    costs = [int(next(it)) for _ in range(n)]
    m = int(next(it))

    graph = Digraph(n)
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        graph.add_edge(u, v)

    solver = CheckpostsSolver(graph, costs)
    min_cost, ways = solver.result()
    print(f"{min_cost} {ways}")


if __name__ == "__main__":
    main()
