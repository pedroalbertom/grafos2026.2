# Marco 2 — Propriedade estrutural

## 1. Propriedade exigida pelo problema

A propriedade estrutural central do Codeforces 427C é a **conectividade forte**.

Para dois vértices `u` e `v`, dizemos que eles são mutuamente alcançáveis quando:

```text
existe um caminho de u até v
e
existe um caminho de v até u
```

Uma **componente fortemente conexa** (CFC ou SCC, do inglês *strongly connected component*) é um conjunto maximal de vértices mutuamente alcançáveis. Todo vértice pertence a exatamente uma CFC.

No problema, um posto em `i` protege `j` exatamente quando `i` e `j` estão na mesma CFC. Assim:

- cada CFC precisa receber pelo menos um posto;
- o menor número de postos é o número de CFCs;
- depois de encontrar as CFCs, escolhe-se o menor custo de cada uma;
- a quantidade de escolhas é o produto da quantidade de vértices que empatam no menor custo de cada CFC.

Essa separação é importante: a DFS identifica a propriedade estrutural; a soma dos custos e a contagem de empates são a adaptação específica do problema.

## 2. Critério algorítmico: Kosaraju

O critério escolhido para este marco é o algoritmo de **Kosaraju-Sharir**, que usa duas etapas de DFS:

1. Construir o grafo reverso `G^R`, trocando cada aresta `u → v` por `v → u`.
2. Executar DFS em `G^R` e registrar cada vértice quando a sua exploração termina. Essa lista é a ordem de pós-visita.
3. Percorrer os vértices em ordem de pós-visita reversa.
4. Para cada vértice ainda não marcado, iniciar uma DFS no grafo original `G`. Todos os vértices alcançados nessa DFS recebem o mesmo identificador de componente.
5. Repetir até que todos os vértices tenham um identificador.

O uso da ordem de término da DFS no grafo reverso é o que impede que uma DFS da segunda etapa misture componentes ligadas apenas em um sentido. O critério produzido pelo algoritmo é:

```text
id[u] == id[v]  se, e somente se,  u e v pertencem à mesma CFC
```

Depois dessa classificação, percorremos os custos dos vértices e agregamos `min_cost[id[v]]` e `ways[id[v]]`.

### 2.1. Referência consultada

A implementação de referência da disciplina possui as duas versões do algoritmo:

- [KosarajuSCC em Python](https://github.com/carubbi/RPG/blob/main/algs4-py/algs4/kosaraju_scc.py);
- [KosarajuSharirSCC em Java](https://github.com/carubbi/RPG/blob/main/algs4-java/algs4/KosarajuSharirSCC.java).

Na referência, `DepthFirstOrder` calcula a ordem de término no grafo reverso; depois, `KosarajuSCC` ou `KosarajuSharirSCC` executa DFS no grafo original e armazena `marked`, `id` e `count`.

## 3. Estado adicional mantido pela DFS

Além da lista de adjacência, o critério precisa manter:

| Estado | Função |
| --- | --- |
| `G^R` | grafo auxiliar com todas as arestas invertidas |
| `marked[v]` | informa se `v` já foi visitado na etapa corrente |
| pós-visita | registra `v` somente depois que todos os seus vizinhos foram explorados |
| ordem de pós-visita reversa | define a ordem das raízes da segunda etapa |
| `id[v]` | identificador da CFC de `v` |
| `count` | quantidade de CFCs encontradas |
| `min_cost[c]` | menor custo conhecido na CFC `c`, na etapa de agregação |
| `ways[c]` | quantidade de vértices que atingem `min_cost[c]` |

O vetor `marked` da primeira DFS não deve ser confundido com o da segunda: a segunda etapa começa com uma nova marcação, porque precisa explorar o grafo original sem reutilizar as visitas feitas no grafo reverso.

## 4. Execução manual na instância do Marco 1

A instância é:

```text
7
5 2 2 7 1 1 4
9
1 2
2 1
2 3
3 4
4 3
4 5
5 6
6 5
6 7
```

Os custos não participam da identificação das CFCs; eles serão usados somente depois da classificação.

### 4.1. Grafo original

Usando a numeração dos vértices do enunciado, as listas de adjacência de `G` são:

| Vértice | Vizinhos alcançáveis diretamente |
| --- | --- |
| `1` | `2` |
| `2` | `1, 3` |
| `3` | `4` |
| `4` | `3, 5` |
| `5` | `6` |
| `6` | `5, 7` |
| `7` | — |

### 4.2. Grafo reverso

Invertendo cada aresta, obtemos `G^R`:

| Vértice | Vizinhos em `G^R` |
| --- | --- |
| `1` | `2` |
| `2` | `1` |
| `3` | `4, 2` |
| `4` | `3` |
| `5` | `6, 4` |
| `6` | `5` |
| `7` | `6` |

Por exemplo, as arestas `2 → 3`, `4 → 3` e `4 → 5` de `G` aparecem como `3 → 2`, `3 → 4` e `5 → 4` em `G^R`.

### 4.3. Primeira DFS: pós-visita em `G^R`

Considerando os vértices em ordem crescente e a ordem de vizinhos indicada na tabela:

| Raiz da DFS | Rastreamento resumido | Vértices adicionados ao terminar |
| --- | --- | --- |
| `1` | `1 → 2`; de `2` retorna para `1` já visitado | `2`, depois `1` |
| `3` | `3 → 4`; de `4` retorna para `3`; `2` já visitado | `4`, depois `3` |
| `5` | `5 → 6`; de `6` retorna para `5`; `4` já visitado | `6`, depois `5` |
| `7` | `7 → 6`, que já estava visitado | `7` |

A ordem de pós-visita é:

```text
2, 1, 4, 3, 6, 5, 7
```

Logo, a ordem de pós-visita reversa para a segunda etapa é:

```text
7, 5, 6, 3, 4, 1, 2
```

### 4.4. Segunda DFS: componentes em `G`

Agora usamos a ordem anterior no grafo original:

| Próxima raiz | Rastreamento resumido | CFC identificada |
| --- | --- | --- |
| `7` | `7` não possui saída | `C0 = {7}` |
| `5` | `5 → 6`; de `6`, `5` e `7` já estão marcados | `C1 = {5, 6}` |
| `6` | já marcado | — |
| `3` | `3 → 4`; de `4`, `3` já está na DFS e `5` já foi marcado | `C2 = {3, 4}` |
| `4` | já marcado | — |
| `1` | `1 → 2`; de `2`, `1` já está na DFS e `3` já foi marcado | `C3 = {1, 2}` |
| `2` | já marcado | — |

Portanto, o vetor de identificadores pode ser representado por:

| Vértice | `1` | `2` | `3` | `4` | `5` | `6` | `7` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `id[v]` | `3` | `3` | `2` | `2` | `1` | `1` | `0` |

Os números dos identificadores dependem da ordem usada para visitar os vértices; o que importa é que vértices da mesma CFC possuem o mesmo identificador.

## 5. Agregação específica do Checkposts

Depois de obter os identificadores, agrupamos os custos:

| CFC | Vértices | Custos | `min_cost` | `ways` |
| --- | --- | --- | ---: | ---: |
| `C0` | `{7}` | `4` | `4` | `1` |
| `C1` | `{5, 6}` | `1, 1` | `1` | `2` |
| `C2` | `{3, 4}` | `2, 7` | `2` | `1` |
| `C3` | `{1, 2}` | `5, 2` | `2` | `1` |

A resposta resultante é:

```text
custo = 4 + 1 + 2 + 2 = 9
maneiras = 1 · 2 · 1 · 1 = 2
saída = 9 2
```

As duas escolhas são `{2, 3, 5, 7}` e `{2, 3, 6, 7}`. O cálculo dos custos não substitui a identificação das CFCs: ele só é válido depois que o vetor `id` foi produzido pela segunda etapa da DFS.

## 6. Justificativa do critério

O algoritmo é adequado porque a proteção exige caminhos nos dois sentidos, exatamente a definição de conectividade forte. Uma DFS no grafo original, isoladamente, poderia alcançar todos os vértices a partir de `1` nesta instância, mas não concluiria que eles pertencem à mesma CFC. O grafo reverso e a ordem de término fornecem a informação adicional necessária para separar os grupos.

O algoritmo de Kosaraju executa duas DFS e percorre cada vértice e cada aresta um número constante de vezes. Assim, sua complexidade é `O(n + m)`. Considerando também o armazenamento de `G` e `G^R`, a memória é `O(n + m)`.

## 7. Relação com BFS

BFS não é usada como critério principal porque o problema não pede distância mínima. Ela poderia ser usada para testar alcançabilidade a partir de uma origem, mas verificar mutualidade dessa forma para todos os pares ou para todos os vértices seria muito mais caro do que uma decomposição em CFCs baseada em DFS.

## 8. Próxima etapa

Este marco formaliza a propriedade, o critério e o rastreamento manual. A implementação de referência ainda deverá ser adaptada ao formato de entrada do Codeforces, que contém custos de vértices além das arestas, e testada no Marco 3.
