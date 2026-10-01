# Tabela final — Kosaraju

Ordem usada na segunda DFS:

`RPostorder = [1, 5, 4, 2, 3]`

| `RPostorder[i]` | Vértice | `Marked` | `EdgeTo` | SCC |
|---|---:|:---:|---:|---:|
| `RPostorder[0]` | 1 | X | — | 0 |
| `RPostorder[1]` | 5 | X | 4 | 0 |
| `RPostorder[2]` | 4 | X | 3 | 0 |
| `RPostorder[3]` | 2 | X | — | 1 |
| `RPostorder[4]` | 3 | X | 1 | 0 |

## Tabela organizada por vértice

| Vértice | `Marked` | `EdgeTo` | SCC |
|---:|:---:|---:|---:|
| 1 | X | — | 0 |
| 2 | X | — | 1 |
| 3 | X | 1 | 0 |
| 4 | X | 3 | 0 |
| 5 | X | 4 | 0 |

## Componentes fortemente conexas

- `SCC 0 = [1, 3, 4, 5]`
- `SCC 1 = [2]`
