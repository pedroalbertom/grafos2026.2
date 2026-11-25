# Marco 4 — Adaptação e integração

## 1. Integração e adaptação da implementação

A solução foi implementada em **Python 3** no arquivo [main.py](file:///home/pedro/Documents/faculdade/Grafos/grafos2026.2/T3/src/main.py), utilizando apenas a biblioteca padrão (`collections.deque` e `sys`), sem dependências externas.

## 2. Justificativa das alterações realizadas

| Elemento | Adaptação para o Distinct Routes | Justificativa |
| --- | --- | --- |
| Estrutura `Edge` | Armazena `to`, `rev`, `cap`, `is_original` e `used` | Permite representar o grafo residual com acesso `O(1)` à aresta reversa e distinguir arestas reais de reversas na reconstrução |
| Capacidade unitária (`cap = 1`) | Todas as arestas originais recebem capacidade `1` e as reversas `0` | Garante que cada teletransportador seja usado no máximo uma vez |
| Arestas paralelas | Cada leitura `(a, b)` adiciona um novo objeto `Edge` em `adj[a]` | Suporta múltiplos teletransportadores entre o mesmo par de salas sem sobrescrever capacidades |
| `extract_path` com `used` | Consome apenas arestas com `is_original == True`, `cap == 0` e `used == False` | Evita que uma mesma aresta saturada seja reutilizada em mais de uma rota na impressão |

## 3. Dependências

- **Linguagem:** Python 3.
- **Bibliotecas:** apenas biblioteca padrão (`collections.deque` para a fila da BFS e `sys` para leitura/escrita rápida via `stdin`/`stdout`).

## 4. Execução reproduzível

Com a instância de teste salva em [casos-de-teste.txt](file:///home/pedro/Documents/faculdade/Grafos/grafos2026.2/T3/dados/casos-de-teste.txt):

```bash
python3 T3/src/main.py < T3/dados/casos-de-teste.txt
```

Saída obtida:

```text
2
3
1 2 6
4
1 3 4 6
```
