# Marco 2 — Propriedade estrutural

## 1. Propriedade exigida pelo problema

A propriedade estrutural central do CSES 1711 é a existência de **caminhos aresta-disjuntos** entre a fonte `s = 1` e o sorvedouro `t = n`.

Em uma rede de fluxo `G = (V, E)` onde cada aresta dirigida `(u, v)` possui capacidade `c(u, v) = 1`:

- cada unidade de fluxo enviada de `s` até `t` corresponde a um caminho dirigido usando arestas com fluxo `1`;
- como as capacidades são inteiras e iguais a `1`, nenhuma aresta pode ser compartilhada por duas unidades de fluxo;
- portanto, o **fluxo máximo** `F` de `1` até `n` é exatamente a quantidade máxima `k` de rotas aresta-disjuntas.

Após encontrar o fluxo máximo, a extração das `k` rotas consiste em decompor o fluxo: partindo de `1`, seguimos arestas originais que receberam fluxo `1`, consumindo (zerando) esse fluxo à medida que reconstruímos cada caminho até `n`.

## 2. Critério algorítmico: Edmonds-Karp

O algoritmo escolhido para este marco é o **Edmonds-Karp**, que implementa o método de Ford-Fulkerson utilizando **Busca em Largura (BFS)** para encontrar caminhos aumentantes no grafo residual `G_f`.

### 2.1. Funcionamento

1. Para cada aresta original `(u, v)` com capacidade `1`, criamos também uma aresta reversa `(v, u)` com capacidade `0` no grafo residual.
2. Enquanto existir um caminho aumentante de `s = 1` até `t = n` no grafo residual (encontrado via **BFS**, garantindo o caminho com menor número de arestas):
   - calculamos o gargalo `bottleneck` ao longo do caminho (como as capacidades são unitárias, `bottleneck = 1`);
   - somamos `bottleneck` ao fluxo total;
   - atualizamos as capacidades residuais ao longo do caminho: subtraímos `1` da aresta direta e somamos `1` na aresta reversa.
3. Quando a BFS não alcança mais `t`, o fluxo acumulado é o fluxo máximo `k`.
4. **Reconstrução das `k` rotas:** repetimos `k` vezes:
   - começamos em `u = 1` e adicionamos `u` ao caminho;
   - procuramos uma aresta original saindo de `u` cujo fluxo enviado seja `1` (ou seja, capacidade residual da aresta direta igual a `0` e da reversa igual a `1`);
   - marcamos essa aresta como consumida (para não reutilizá-la em outra rota) e avançamos para o próximo vértice até atingir `n`.

### 2.2. Complexidade

- **Tempo:** `O(V · E²)`. Com `V ≤ 500` e `E ≤ 1000`, o algoritmo realiza no máximo `k ≤ m` aumentos de fluxo, cada um com uma BFS de custo `O(V + E)`, executando bem abaixo de `1.00 s`.
- **Espaço:** `O(V + E)` para armazenar a lista de adjacência residual e os vetores auxiliares da BFS.

## 3. Estado adicional mantido pelo algoritmo

Além da lista de adjacência com arestas residuais (armazenando destino, capacidade residual, índice da aresta reversa e indicador se é aresta original), o algoritmo mantém:

| Estado | Função |
| --- | --- |
| `parent_v[v]` | vértice anterior no caminho aumentante encontrado pela BFS |
| `parent_e[v]` | índice da aresta usada para chegar em `v` na BFS |
| `max_flow` | fluxo máximo acumulado (`k`) |
| `used` (na aresta) | marca se a aresta original com fluxo `1` já foi consumida na reconstrução |

## 4. Execução manual na instância do Marco 1

A instância é:

```text
6 7
1 2
1 3
2 6
3 4
3 5
4 6
5 6
```

### Etapa 1: Primeira BFS a partir de `1`

- Fila inicial: `[1]`.
- Vizinhos de `1` com capacidade residual `> 0`: `2` e `3`.
- Vizinhos de `2`: `6` (atingiu o sorvedouro `t = 6`).
- Caminho aumentante encontrado: `1 → 2 → 6` (gargalo = `1`).
- Atualização residual: arestas `(1, 2)` e `(2, 6)` ficam com capacidade residual `0`; suas reversas `(2, 1)` e `(6, 2)` ficam com `1`.
- `max_flow = 1`.

### Etapa 2: Segunda BFS a partir de `1`

- Fila inicial: `[1]`.
- De `1`, apenas `(1, 3)` tem capacidade residual `> 0`.
- De `3`, visitamos `4` e `5`.
- De `4`, visitamos `6` (atingiu `t = 6`).
- Caminho aumentante encontrado: `1 → 3 → 4 → 6` (gargalo = `1`).
- Atualização residual: arestas `(1, 3)`, `(3, 4)` e `(4, 6)` ficam com capacidade residual `0`; suas reversas ficam com `1`.
- `max_flow = 2`.

### Etapa 3: Terceira BFS a partir de `1`

- De `1`, tanto `(1, 2)` quanto `(1, 3)` têm capacidade residual `0`.
- A BFS não alcança `6`. O algoritmo encerra com `k = 2`.

### Etapa 4: Reconstrução das rotas

1. **Rota 1:** partindo de `1`, seguimos `(1, 2)` (fluxo `1`, consumida) e `(2, 6)` (fluxo `1`, consumida) → `1 2 6` (tamanho `3`).
2. **Rota 2:** partindo de `1`, `(1, 2)` já foi consumida; seguimos `(1, 3)`, `(3, 4)` e `(4, 6)` → `1 3 4 6` (tamanho `4`).

Saída esperada:

```text
2
3
1 2 6
4
1 3 4 6
```
