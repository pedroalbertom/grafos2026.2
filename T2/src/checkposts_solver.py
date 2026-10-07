"""
CheckpostsSolver — Resolução do problema Codeforces 427C (Checkposts)
Construído sobre a biblioteca algs4 (KosarajuSCC e Digraph).
"""
from algs4.kosaraju_scc import KosarajuSCC

MOD = 1_000_000_007


class CheckpostsSolver:
    """
    Resolve o problema Checkposts determinando o menor custo total
    e a quantidade de maneiras de atingir esse menor custo com o menor
    número de postos policiais (módulo 1 000 000 007).
    """

    def __init__(self, digraph, costs):
        """
        :param digraph: Instância de algs4.digraph.Digraph com V cruzamentos (0-indexados)
        :param costs: Lista de inteiros de tamanho V onde costs[i] é o custo do cruzamento i
        """
        self.digraph = digraph
        self.costs = costs
        self.scc = KosarajuSCC(digraph)
        self.min_cost = 0
        self.ways = 1
        self._solve()

    def _solve(self):
        num_components = self.scc.count
        if num_components == 0:
            self.min_cost = 0
            self.ways = 1
            return

        INF = float('inf')
        min_comp_cost = [INF] * num_components
        ways_comp = [0] * num_components

        for v in range(self.digraph.V):
            c_id = self.scc.id[v]
            c_val = self.costs[v]
            if c_val < min_comp_cost[c_id]:
                min_comp_cost[c_id] = c_val
                ways_comp[c_id] = 1
            elif c_val == min_comp_cost[c_id]:
                ways_comp[c_id] += 1

        total_cost = 0
        total_ways = 1

        for c_id in range(num_components):
            total_cost += min_comp_cost[c_id]
            total_ways = (total_ways * ways_comp[c_id]) % MOD

        self.min_cost = total_cost
        self.ways = total_ways

    def result(self):
        """Retorna uma tupla (min_cost, ways)."""
        return self.min_cost, self.ways
