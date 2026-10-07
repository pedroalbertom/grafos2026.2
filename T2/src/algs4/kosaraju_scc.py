"""
Módulo KosarajuSCC adaptado da biblioteca de referência algs4.
Inclui suporte à identificação de componentes fortemente conexas e ao
cálculo do custo mínimo e combinações para postos policiais com custos nos vértices.
"""
from algs4.depth_first_order import DepthFirstOrder
from algs4.digraph import Digraph

MOD = 1_000_000_007


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
