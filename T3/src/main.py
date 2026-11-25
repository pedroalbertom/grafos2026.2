from collections import deque
import sys


class Edge:
    """Aresta do grafo residual para o algoritmo de Edmonds-Karp."""

    def __init__(self, to: int, rev: int, cap: int, is_original: bool) -> None:
        self.to = to
        self.rev = rev
        self.cap = cap
        self.is_original = is_original
        self.used = False


def add_edge(adj: list[list[Edge]], u: int, v: int) -> None:
    """Adiciona aresta dirigida (u -> v) de capacidade 1 e sua reversa residual."""
    fwd = Edge(v, len(adj[v]), 1, True)
    bwd = Edge(u, len(adj[u]), 0, False)
    adj[u].append(fwd)
    adj[v].append(bwd)


def edmonds_karp(adj: list[list[Edge]], s: int, t: int, n: int) -> int:
    """Calcula o fluxo máximo de s até t usando BFS (Edmonds-Karp)."""
    max_flow = 0
    while True:
        parent_v = [-1] * (n + 1)
        parent_e = [-1] * (n + 1)
        parent_v[s] = s
        q = deque([s])

        while q and parent_v[t] == -1:
            u = q.popleft()
            for idx, edge in enumerate(adj[u]):
                if parent_v[edge.to] == -1 and edge.cap > 0:
                    parent_v[edge.to] = u
                    parent_e[edge.to] = idx
                    q.append(edge.to)

        if parent_v[t] == -1:
            break

        curr = t
        while curr != s:
            prev = parent_v[curr]
            edge = adj[prev][parent_e[curr]]
            edge.cap -= 1
            adj[curr][edge.rev].cap += 1
            curr = prev

        max_flow += 1

    return max_flow


def extract_path(adj: list[list[Edge]], s: int, t: int) -> list[int]:
    """Reconstrói um caminho aresta-disjunto de s até t consumindo arestas saturadas."""
    path = [s]
    curr = s
    while curr != t:
        for edge in adj[curr]:
            if edge.is_original and edge.cap == 0 and not edge.used:
                edge.used = True
                curr = edge.to
                path.append(curr)
                break
    return path


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj: list[list[Edge]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        add_edge(adj, a, b)

    k = edmonds_karp(adj, 1, n, n)
    out = [str(k)]
    for _ in range(k):
        path = extract_path(adj, 1, n)
        out.append(str(len(path)))
        out.append(" ".join(map(str, path)))

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
