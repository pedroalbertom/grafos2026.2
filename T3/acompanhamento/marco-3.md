# Marco 3 — Escolha do algoritmo

## 1. Justificativa do algoritmo: Edmonds-Karp

Dentre os algoritmos da família de fluxo máximo, escolhemos o **Edmonds-Karp** (implementação do método de Ford-Fulkerson que utiliza **Busca em Largura — BFS** para encontrar caminhos aumentantes no grafo residual):

- **Garantia de término e tempo polinomial:** diferentemente do Ford-Fulkerson genérico com DFS, a BFS escolhe sempre o caminho aumentante com menor número de arestas, garantindo complexidade polinomial independente da ordem das arestas.
- **Adequação às restrições:** com `V ≤ 500` e `E ≤ 1000`, o algoritmo executa confortavelmente dentro do limite de `1.00 s`.
- **Simplicidade para reconstrução das rotas:** como todas as capacidades são `1`, cada aumento de fluxo envia exatamente `1` unidade ao longo de um caminho; ao final, basta decompor o fluxo seguindo `k` caminhos por arestas originais saturadas (`cap_residual == 0`).

## 2. Condições de aplicabilidade

O algoritmo de Edmonds-Karp é aplicável ao problema porque:

1. O grafo é **dirigido** e possui fonte `s = 1` e sorvedouro `t = n` bem definidos.
2. Todas as capacidades das arestas são **não-negativas e inteiras** (`c(u, v) = 1`).
3. Pelo **Teorema da Integralidade**, como as capacidades são inteiras, existe um fluxo máximo inteiro — o que garante que cada unidade de fluxo corresponde a um caminho aresta-disjunto completo de `s` até `t`.

## 3. Invariante e operação central

- **Operação central:** busca de caminho aumentante mínimo (em número de arestas) no grafo residual `G_f` via BFS, seguida de atualização das capacidades residuais ao longo do caminho encontrado (subtraindo o gargalo `1` das arestas diretas e somando `1` nas reversas).
- **Invariante:** a cada iteração do laço principal, o fluxo `f` mantido na rede é um **fluxo válido** (respeita conservação de fluxo nos vértices intermediários `v ∉ {s, t}` e limites de capacidade `0 ≤ f(u, v) ≤ 1`), e a distância em arestas de `s` até qualquer vértice no grafo residual nunca diminui. Quando não há mais caminho aumentante de `s` até `t` em `G_f`, `f` é máximo.

## 4. Estimativa de complexidade

| Métrica | Complexidade | Análise para `V ≤ 500, E ≤ 1000` |
| --- | --- | --- |
| **Tempo (Fluxo Máximo)** | `O(V · E²)` (ou `O(k · E)` em redes unitárias, onde `k ≤ E`) | No pior caso com capacidades unitárias, há no máximo `E` aumentos de fluxo, cada um custando uma BFS `O(V + E)` → `~10⁶` operações |
| **Tempo (Reconstrução)** | `O(k · V)` | Extrair `k` caminhos de comprimento no máximo `V` |
| **Espaço** | `O(V + E)` | Lista de adjacência residual + vetores `parent_v` e `parent_e` da BFS |
