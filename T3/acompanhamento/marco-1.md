# Problema — CSES 1711 Distinct Routes

- **Trabalho:** T3 — Fluxo em redes e emparelhamento
- **Link oficial:** <https://cses.fi/problemset/task/1711>
- **Marco:** 1 — Problema e conhecimento prévio

## 1. Resumo do problema

Um jogo possui `n` salas conectadas por `m` teletransportadores de mão única. Cada teletransportador pode ser utilizado **no máximo uma vez** ao longo de todo o jogo.

O objetivo é jogar o maior número possível de dias, onde em cada dia o jogador começa na sala `1` e precisa chegar à sala `n` usando uma sequência válida de teletransportadores disponíveis.

Além de determinar o número máximo de dias `k`, é necessário imprimir `k` rotas válidas (sequências de salas de `1` até `n`) que sejam **aresta-disjuntas** entre si, isto é, nenhum teletransportador aparece em mais de uma rota.

## 2. Entrada

A entrada é formada por:

1. dois inteiros `n` e `m`, representando o número de salas e o número de teletransportadores;
2. `m` linhas seguintes, cada uma com dois inteiros `a` e `b`, indicando um teletransportador de mão única da sala `a` para a sala `b`.

As salas são numeradas de `1` a `n`.

## 3. Saída

Devem ser impressos:

1. um inteiro `k`: o número máximo de dias (rotas aresta-disjuntas de `1` até `n`);
2. para cada uma das `k` rotas:
   - uma linha com um inteiro `L` (quantidade de salas na rota);
   - uma linha com os `L` inteiros representando as salas visitadas na ordem, começando em `1` e terminando em `n`.

Caso existam múltiplas soluções válidas com `k` rotas, qualquer uma é aceita.

## 4. Restrições

| Parâmetro | Restrição |
| --- | --- |
| `n` | `2 ≤ n ≤ 500` |
| `m` | `1 ≤ m ≤ 1000` |
| teletransportador | `1 ≤ a, b ≤ n` |
| arestas paralelas | podem existir múltiplos teletransportadores entre o mesmo par `(a, b)` |

O limite de tempo é de `1.00 s` e o limite de memória é de `512 MB`. Com `n ≤ 500` e `m ≤ 1000`, algoritmos de fluxo máximo como Edmonds-Karp (`O(V · E²)`) executam confortavelmente dentro do limite.

## 5. Modelagem dos vértices e das arestas

Modelamos a instância como uma rede de fluxo dirigida `G = (V, E)` com fonte `s = 1` e sorvedouro `t = n`:

| Elemento | Interpretação |
| --- | --- |
| Vértice `v` | sala `v` |
| Vértice `1` | fonte `s` (início de cada rota) |
| Vértice `n` | sorvedouro `t` (destino de cada rota) |
| Aresta dirigida `(a, b)` | teletransportador de `a` para `b` com capacidade `c(a, b) = 1` |

Como cada teletransportador pode ser usado no máximo uma vez, atribuímos **capacidade unitária (`1`)** a cada aresta dirigida. Pelo teorema do corte mínimo e fluxo máximo (e pela integralidade das capacidades), o valor do fluxo máximo de `1` até `n` é exatamente igual ao número máximo de caminhos aresta-disjuntos de `1` até `n`.

## 6. Classificação do grafo

O grafo é:

- **dirigido**, pois os teletransportadores funcionam em uma única direção;
- **possivelmente multigrafo**, pois o enunciado não proíbe múltiplos teletransportadores entre o mesmo par `(a, b)`;
- **capacitado (capacidade unitária)** nas arestas, pois cada aresta suporta fluxo máximo `1`;
- **não ponderado nos vértices**, pois não há restrição de capacidade nas salas (uma mesma sala intermediária pode ser visitada em dias diferentes).

## 7. Instância de exemplo (Marco 1)

Utilizaremos a instância oficial do enunciado:

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

Nessa instância:

- há `n = 6` salas e `m = 7` teletransportadores;
- existem dois caminhos aresta-disjuntos de `1` até `6`: `1 → 2 → 6` e `1 → 3 → 4 → 6` (ou `1 → 3 → 5 → 6`);
- portanto, a resposta ótima é `k = 2`.
