"""
Solução autossuficiente (inlined) para o Codeforces 427C — Checkposts.
Contém as estruturas adaptadas da biblioteca algs4 (Bag, Digraph,
DepthFirstOrder e KosarajuSCC) em um único arquivo, com a adaptação de
custos e combinações incorporada diretamente na classe KosarajuSCC.
"""
from collections import deque
import sys

# Ajuste do limite de recursão para dígrafos com até 10^5 vértices
sys.setrecursionlimit(300000)

MOD = 1_000_000_007


class Node:

    def __init__(self, item, next_node):
        self.item = item
        self.next = next_node


class LinkIterator:

    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        item = self.current.item
        self.current = self.current.next
        return item


class Bag:

    def __init__(self):
        self.first = None
        self.n = 0

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def add(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1


class Digraph:

    def __init__(self, v=0):
        self.V = v
        self.E = 0
        self.adj = [Bag() for _ in range(self.V)]

    def add_edge(self, v, w):
        self.adj[v].add(w)
        self.E += 1

    def reverse(self):
        r = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj[v]:
                r.add_edge(w, v)
        return r


class DepthFirstOrder:

    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.post = deque()
        for w in range(G.V):
            if not self.marked[w]:
                self.dfs(G, w)

    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)
        self.post.append(v)

    def reverse_post(self):
        return reversed(self.post)


class KosarajuSCC:

    def __init__(self, G, costs=None):
        self.marked = [False for _ in range(G.V)]
        self.id = [0 for _ in range(G.V)]
        self.count = 0
        self.costs = costs
        self.min_cost = 0
        self.ways = 1

        order = DepthFirstOrder(G.reverse())
        for v in order.reverse_post():
            if not self.marked[v]:
                self.dfs(G, v)
                self.count += 1

        if costs is not None:
            self._compute_costs()

    def dfs(self, G, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)

    def strongly_connected(self, v, w):
        return self.id[v] == self.id[w]

    def _compute_costs(self):
        if self.count == 0:
            self.min_cost = 0
            self.ways = 1
            return

        INF = float('inf')
        min_comp_cost = [INF] * self.count
        ways_comp = [0] * self.count

        for v in range(len(self.marked)):
            c_id = self.id[v]
            c_val = self.costs[v]
            if c_val < min_comp_cost[c_id]:
                min_comp_cost[c_id] = c_val
                ways_comp[c_id] = 1
            elif c_val == min_comp_cost[c_id]:
                ways_comp[c_id] += 1

        total_cost = 0
        total_ways = 1

        for c in range(self.count):
            total_cost += min_comp_cost[c]
            total_ways = (total_ways * ways_comp[c]) % MOD

        self.min_cost = total_cost
        self.ways = total_ways


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

    scc = KosarajuSCC(graph, costs)
    print(f"{scc.min_cost} {scc.ways}")


if __name__ == "__main__":
    main()
