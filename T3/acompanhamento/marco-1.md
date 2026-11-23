# Marco 1 — Formulação

- **Trabalho:** T3 — Otimização em grafos ponderados e redes (Classe: Fluxo máximo)
- **Problema:** D* — CSES 1711 Distinct Routes
- **Link oficial:** <https://cses.fi/problemset/task/1711>

## 1. Resumo do problema

Um jogo possui `n` salas conectadas por `m` teletransportadores de mão única. Cada teletransportador pode ser utilizado **no máximo uma vez** ao longo de todo o jogo.

O objetivo é jogar o maior número possível de dias, onde em cada dia o jogador começa na sala `1` e precisa chegar à sala `n` usando uma sequência válida de teletransportadores disponíveis.

Além de determinar o número máximo de dias `k`, é necessário imprimir `k` rotas válidas (sequências de salas de `1` até `n`) que sejam **aresta-disjuntas** entre si, isto é, nenhum teletransportador pode aparecer em mais de uma rota.

## 2. Entrada, saída, objetivo e restrições

### Entrada
1. Dois inteiros `n` e `m`: número de salas e número de teletransportadores.
2. `m` linhas seguintes com dois inteiros `a` e `b`: um teletransportador de mão única da sala `a` para a sala `b`.

### Saída
1. Um inteiro `k`: o número máximo de dias (rotas aresta-disjuntas de `1` até `n`).
2. Para cada uma das `k` rotas:
   - uma linha com um inteiro `L` (quantidade de salas na rota);
   - uma linha com os `L` inteiros das salas visitadas na ordem, começando em `1` e terminando em `n`.

### Objetivo
Maximizar `k` (quantidade de caminhos aresta-disjuntos de `1` até `n`) e reconstruir `k` caminhos válidos sem reutilizar arestas.

### Restrições
| Parâmetro | Restrição |
| --- | --- |
| `n` | `2 ≤ n ≤ 500` |
| `m` | `1 ≤ m ≤ 1000` |
| teletransportador | `1 ≤ a, b ≤ n` |
| arestas paralelas | podem existir múltiplos teletransportadores entre o mesmo par `(a, b)` |
| tempo / memória | `1.00 s` / `512 MB` |

## 3. Definição de vértices, arestas, direção e capacidades

| Elemento | Definição |
| --- | --- |
| **Vértices (`V`)** | Salas `1, 2, ..., n`, sendo `s = 1` a fonte e `t = n` o sorvedouro |
| **Arestas (`E`)** | Teletransportadores `(a, b)` |
| **Direção** | **Dirigido** (teletransportadores são de mão única: `a → b`) |
| **Capacidades** | **Capacidade unitária `c(a, b) = 1`** em cada aresta, pois cada teletransportador pode ser usado no máximo uma vez |

## 4. Instância pequena

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

Nesta instância (`n = 6`, `m = 7`), existem `k = 2` rotas aresta-disjuntas possíveis de `1` até `6` (por exemplo, `1 → 2 → 6` e `1 → 3 → 4 → 6`).
