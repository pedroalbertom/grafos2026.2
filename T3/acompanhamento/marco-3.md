# Marco 3 — Adaptação e testes

## 1. Estratégia algorítmica

Para resolver o **CSES 1711 (Distinct Routes)**, a estratégia é dividida em duas etapas sobre a rede de fluxo `G = (V, E)` com fonte `s = 1`, sorvedouro `t = n` e capacidades unitárias (`1`):

1. **Cálculo do fluxo máximo (Edmonds-Karp):**
   - Construir o grafo residual com cada aresta original `(a, b)` de capacidade `1` e sua respectiva aresta reversa `(b, a)` de capacidade `0`.
   - Executar sucessivas buscas em largura (**BFS**) a partir de `1` até `n` no grafo residual, encontrando o caminho aumentante mais curto em número de arestas.
   - A cada caminho encontrado, enviar `1` unidade de fluxo (subtraindo `1` da capacidade residual das arestas diretas e somando `1` nas reversas) e incrementar `max_flow`.
2. **Reconstrução das `k = max_flow` rotas:**
   - Repetir `k` vezes uma travessia partindo de `1` até `n`.
   - Em cada vértice `u`, escolher uma aresta original `(u, v)` que tenha fluxo efetivo (`cap_residual == 0` e não marcada como `used`), marcá-la como `used = True` e avançar para `v` até alcançar `n`.

## 2. Adaptações e justificativas

| Elemento | Adaptação para o Distinct Routes | Justificativa |
| --- | --- | --- |
| Capacidade das arestas | Todas as arestas originais recebem capacidade `1` | Cada teletransportador pode ser usado no máximo uma vez |
| Aresta reversa no grafo residual | Criada com capacidade inicial `0` e ponteiro `rev` | Permite cancelar fluxo enviado anteriormente caso uma BFS futura encontre um rearranjo melhor |
| Arestas paralelas | Armazenadas como entradas independentes na lista de adjacência | O enunciado permite múltiplos teletransportadores entre o mesmo par `(a, b)` |
| Flag `used` / `is_original` | Distingue arestas originais de reversas e evita reuso na reconstrução | Garante que apenas arestas reais com fluxo `1` sejam impressas e que nenhuma seja usada em duas rotas |

## 3. Instância adicional (caso com arestas paralelas)

Para validar o comportamento com múltiplos teletransportadores entre o mesmo par de salas:

```text
4 5
1 2
1 2
2 3
2 4
3 4
```

- **Fluxo máximo esperado:** `2` (duas rotas saindo de `1` por arestas paralelas até `2`, depois uma segue `2 → 4` e a outra `2 → 3 → 4`).
- **Saída esperada:**

```text
2
3
1 2 4
4
1 2 3 4
```

## 4. Código de referência (Python 3)

Implementação pronta para ser integrada em `T3/src/` na etapa de execução e testes:

```python
from collections import deque
import sys


class Edge:
    def __init__(self, to: int, rev: int, cap: int, is_original: bool) -> None:
        self.to = to
        self.rev = rev
        self.cap = cap
        self.is_original = is_original
        self.used = False


def add_edge(adj: list[list[Edge]], u: int, v: int) -> None:
    fwd = Edge(v, len(adj[v]), 1, True)
    bwd = Edge(u, len(adj[u]), 0, False)
    adj[u].append(fwd)
    adj[v].append(bwd)


def edmonds_karp(adj: list[list[Edge]], s: int, t: int, n: int) -> int:
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
```
