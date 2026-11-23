# Marco 2 — Representação e validação

## 1. Justificativa da representação computacional

Para `n ≤ 500` e `m ≤ 1000`, o grafo é **esparso** (`m` da ordem de `2n`). A representação escolhida é a **lista de adjacência** com suporte a **grafo residual**:

- **Eficiência de memória:** `O(V + E)` em vez de `O(V²)` de uma matriz de adjacência.
- **Suporte a arestas paralelas:** como o problema permite múltiplos teletransportadores entre o mesmo par `(a, b)`, a lista de adjacência armazena cada teletransportador como uma entrada independente, sem sobrescrever capacidades.
- **Acesso direto à aresta reversa:** cada aresta direta `(u, v)` guarda o índice da sua aresta reversa `(v, u)` na lista de `v`, permitindo atualizar capacidades residuais em `O(1)`.

## 2. Representação da instância pequena

Para a instância do Marco 1 (`n = 6`, `m = 7`), a lista de adjacência inicial (apenas arestas originais com capacidade `1`) é:

| Vértice | Arestas de saída `(destino, cap)` |
| --- | --- |
| `1` | `(2, 1)`, `(3, 1)` |
| `2` | `(6, 1)` |
| `3` | `(4, 1)`, `(5, 1)` |
| `4` | `(6, 1)` |
| `5` | `(6, 1)` |
| `6` | `—` |

*(No grafo residual, cada aresta `(u, v)` acima possui também uma aresta reversa `(v, u)` com capacidade inicial `0`.)*

## 3. Validação de entrada e saída esperada

- **Entrada:** `6` salas e `7` teletransportadores válidos no intervalo `[1, 6]`, com `s = 1` e `t = 6`.
- **Saída esperada:**

```text
2
3
1 2 6
4
1 3 4 6
```

*(Nota: a rota `1 3 5 6` também é válida no lugar de `1 3 4 6`, pois ambas são aresta-disjuntas de `1 2 6`.)*

## 4. Identificação preliminar da família do problema

O problema pertence à família de **Fluxo Máximo** em redes capacitadas:

- Cada teletransportador tem capacidade `1` (uso único).
- O número máximo de caminhos aresta-disjuntos de `1` até `n` equivale ao **valor do fluxo máximo** de `s = 1` até `t = n` (pelo Teorema do Fluxo Máximo e Corte Mínimo, com capacidades inteiras).
