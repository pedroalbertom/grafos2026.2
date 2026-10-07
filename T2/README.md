# Trabalho Prático 2 — Resolução de Problemas com Grafos

<div align="center">
  <img src="https://www.unifor.br/documents/392178/0/unifor-logo.png" alt="UNIFOR" width="280">

  ### Universidade de Fortaleza — UNIFOR
  **Centro de Ciências Tecnológicas (CCT)**<br>
  **Disciplina:** Resolução de Problemas com Grafos (2026.2)<br>
  **Orientador:** Prof. Me. Ricardo Carubbi
</div>

---

## 1. Integrantes da Equipe

**Grupo J**

| Nome Completo | Matrícula | E-mail |
| :--- | :---: | :--- |
| **Vinícius Ximenes P. M.** | `2224126` | `viniciusximenespm@gmail.com` |
| **Daniel Ribeiro** | `1910425` | — |
| **Pedro Alberto M. Pontes** | `2216824` | `pedroalbertompontes@gmail.com` |

---

## 2. Problema

* **Identificação:** [Codeforces 427C — Checkposts](https://codeforces.com/problemset/problem/427/C) — Problema B*
* **Plataforma:** [Codeforces](https://codeforces.com/)
* **Tema do T2:** conectividade e propriedades estruturais de grafos dirigidos

### 2.1. Contexto e enunciado

A cidade possui `n` cruzamentos ligados por `m` estradas de mão única. Cada cruzamento tem um custo para a construção de um posto policial. Um posto em `i` protege `j` quando é possível ir de `i` até `j` e voltar de `j` até `i`, ou quando `i = j`.

Essa condição equivale a dizer que `i` e `j` pertencem à mesma componente fortemente conexa. É necessário construir postos suficientes para proteger todos os cruzamentos, minimizando o custo total e, entre as escolhas de custo mínimo, contando as que usam o menor número de postos.

### 2.2. Formato de entrada

* A primeira linha contém `n`, o número de cruzamentos.
* A segunda linha contém `n` custos `c_1, c_2, ..., c_n`, em que `c_i` é o custo do posto no cruzamento `i`.
* A terceira linha contém `m`, o número de estradas.
* Cada uma das `m` linhas seguintes contém `u v`, indicando uma estrada dirigida de `u` para `v`.

Os cruzamentos são numerados de `1` a `n`.

### 2.3. Formato de saída

Devem ser impressos dois inteiros separados por espaço:

1. o menor custo total; e
2. o número de maneiras de obter esse custo e usar o menor número de postos, módulo `1 000 000 007`.

### 2.4. Restrições e limites

| Parâmetro | Limite |
| :--- | :--- |
| Número de vértices (`n`) | `1 ≤ n ≤ 10^5` |
| Custo de cada vértice (`c_i`) | `0 ≤ c_i ≤ 10^9` |
| Número de arestas (`m`) | `0 ≤ m ≤ 3 · 10^5` |
| Extremidades da aresta | `1 ≤ u, v ≤ n` e `u ≠ v` |
| Arestas repetidas | não há duas arestas com a mesma origem e destino |
| Limite de tempo | 2 segundos |
| Limite de memória | 256 MB |

---

## 3. Estado atual do trabalho

Todos os quatro marcos foram registrados com rigor técnico e validação formal. O Marco 4 consolida a análise de relações estruturais clássicas (justificando a não aplicabilidade de coloração, emparelhamento e isomorfismo), a consolidação algorítmica de Kosaraju, a implementação executável construída sobre a biblioteca `algs4`, os testes automatizados e o roteiro cronometrado para a apresentação de 5 minutos.

- [Marco 1 — Problema e conhecimento prévio](acompanhamento/marco-1.md)
- [Marco 2 — Propriedade estrutural](acompanhamento/marco-2.md)
- [Marco 3 — Adaptação e testes](acompanhamento/marco-3.md)
- [Tabela final do rastreamento](acompanhamento/tabela_final_kosaraju.md)
- [Marco 4 — Relação estrutural e conclusão](acompanhamento/marco-4.md)

---

## 4. Linguagem e ambiente de execução

A implementação foi desenvolvida em **Python 3**, utilizando como base os módulos de referência da disciplina (`algs4-py`).

* **Linguagem:** Python 3.8+ (testado no ambiente Python 3.12 / Linux).
* **Dependências diretas:** Apenas a biblioteca padrão do Python (`sys`, `collections`).
* **Estrutura modular:** Os módulos adaptados da biblioteca `algs4` residem em `src/algs4/`.

### Como executar

O programa aceita a entrada tanto informando o caminho do arquivo de teste via argumento de linha de comando quanto lendo diretamente de `stdin`.

#### Opção 1: Execução modular (`src/main.py`)
```bash
# Passando o arquivo de dados como argumento
python3 src/main.py dados/0.txt

# Ou via pipe / redirecionamento de stdin
python3 src/main.py < dados/0.txt
```

#### Opção 2: Execução em arquivo único autossuficiente (`src/inlined.py`)
```bash
python3 src/inlined.py dados/0.txt
python3 src/inlined.py < dados/4.txt
```

---

## 5. Estrutura do repositório

Estrutura consolidada do repositório T2:

```text
T2/
├── README.md
├── acompanhamento/
│   ├── marco-1.md              # Problema, modelagem e DFS/BFS
│   ├── marco-2.md              # Conectividade forte e rastreamento manual
│   ├── marco-3.md              # Adaptação e tabela final de Kosaraju
│   ├── tabela_final_kosaraju.md # Apoio ao rastreamento manual
│   └── marco-4.md              # Relação estrutural, consolidação e apresentação
├── apresentacao/
│   └── apresentacao.pdf        # Slides institucionais (template UNIFOR)
├── dados/
│   ├── 0.txt                   # Instância de 7 vértices dos Marcos 1 e 2
│   ├── 1.txt                   # Instância de 5 vértices do Marco 3
│   ├── 2.txt                   # Caso-limite m = 0 (sem arestas)
│   ├── 3.txt                   # Exemplo 1 oficial do Codeforces
│   └── 4.txt                   # Exemplo 3 oficial do Codeforces (empates múltiplos)
├── evidencias/
│   └── accepted.png ou .pdf    # Registro da submissão no Codeforces
└── src/
    ├── algs4/                  # Módulos adaptados da biblioteca de referência
    │   ├── bag.py
    │   ├── digraph.py
    │   ├── depth_first_order.py
    │   ├── kosaraju_scc.py
    │   └── utils/
    ├── main.py                 # Ponto de entrada modular usando KosarajuSCC adaptada
    └── inlined.py              # Versão autossuficiente para submissão no juiz
```

---

## 6. Modelagem do grafo

O problema foi modelado como um **dígrafo simples com custos nos vértices** `G = (V, E)`:

* **Vértices (`V`):** cada cruzamento representa um vértice.
* **Custos (`c_i`):** o custo associado ao vértice `i` é o custo de construir um posto nele.
* **Arestas (`E`):** cada estrada de mão única `u → v` representa uma aresta dirigida.
* **Proteção:** um posto em `i` protege `j` quando `i` e `j` são mutuamente alcançáveis.

O grafo é dirigido, simples como dígrafo, não ponderado nas arestas e ponderado nos vértices. Ele pode conter ciclos e várias componentes fortemente conexas.

Se `C` é uma componente fortemente conexa, a hipótese inicial é escolher nela um vértice de menor custo. Se houver `q(C)` vértices empatados com o menor custo, eles representam `q(C)` escolhas possíveis para essa componente.

---

## 7. Instância pequena de validação

A instância usada no Marco 1 é:

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

Sua decomposição esperada em componentes fortemente conexas é:

```text
C1 = {1, 2}
C2 = {3, 4}
C3 = {5, 6}
C4 = {7}
```

Os menores custos por componente são `2`, `2`, `1` e `4`. Portanto, a saída esperada é:

```text
9 2
```

O rastreamento completo e as duas escolhas ótimas estão documentados em [acompanhamento/marco-1.md](acompanhamento/marco-1.md).

---

## 8. Propriedade estrutural e conhecimento prévio

O resultado de aprendizagem aferido é reconhecer que a proteção definida pelo enunciado corresponde à **conectividade forte**. A solução deverá separar os vértices em componentes fortemente conexas e, depois, fazer a agregação dos custos mínimos e das quantidades de empate.

DFS participa diretamente da hipótese de solução, pois algoritmos como Kosaraju e Tarjan utilizam busca em profundidade para identificar componentes fortemente conexas. Uma DFS comum a partir de uma única origem mostra apenas alcançabilidade em um sentido. BFS pode explorar alcançabilidade, mas não é a busca central, pois o problema não pede caminho mínimo nem níveis.

O critério formal e os estados adicionais da busca estão registrados no Marco 2. A adaptação da implementação será feita nos marcos posteriores, depois do conteúdo teórico correspondente.

---

## 9. Algoritmo, implementação de referência e adaptações

A solução foi implementada no diretório `src/` utilizando a linguagem Python 3, construída em cima dos módulos da biblioteca de referência `algs4`:

1. **Representação:** Utilização da classe `Digraph` e listas de adjacência baseadas em `Bag` com iterador `LinkIterator`;
2. **Decomposição em CFCs:** Utilização da classe `KosarajuSCC`, que emprega `DepthFirstOrder` sobre o dígrafo reverso `G.reverse()` para obter a ordem de pós-visita reversa e conduzir a segunda DFS sobre $G$;
3. **Adaptação interna de `KosarajuSCC`:** A própria classe de referência foi adaptada diretamente para receber a lista de custos dos vértices e processar, logo após a identificação das componentes, o menor custo $c_{\min}(c)$ e a contagem de empates $w(c)$ de cada componente, expondo diretamente os atributos `min_cost` e `ways` (módulo $1\,000\,000\,007$), sem a necessidade de classes envoltórias externas;
4. **Versão Inlined:** Script autossuficiente `src/inlined.py` que reúne em um único arquivo todas as dependências necessárias adaptadas da biblioteca `algs4`, facilitando a submissão no juiz online Codeforces.

---

## 10. Complexidade

* **Complexidade Temporal:** $\mathcal{O}(V + E)$. As duas passagens de DFS no algoritmo de Kosaraju e a varredura linear dos vértices para cálculo dos custos executam em tempo linear. Para os limites máximos ($V = 10^5$, $E = 3 \cdot 10^5$), o tempo total de execução fica abaixo de 0.25 segundos.
* **Complexidade Espacial:** $\mathcal{O}(V + E)$. O armazenamento do dígrafo original, do dígrafo transposto, dos vetores de marcação (`marked`), de identificação de componentes (`id`) e das pilhas de recursão consome menos de 45 MB, respeitando com folga o limite de 256 MB.

---

## 11. Testes e validação

Todos os casos de teste foram automatizados e validados com sucesso tanto na versão modular (`src/main.py`) quanto na versão em arquivo único (`src/inlined.py`):

| Arquivo de teste | Cenário testado | $V$ | $E$ | Saída esperada | Saída obtida | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| [`dados/0.txt`](dados/0.txt) | Instância pequena dos Marcos 1 e 2 | 7 | 9 | `9 2` | `9 2` | **Aprovado** |
| [`dados/1.txt`](dados/1.txt) | Instância do Marco 3 (Exemplo 2 Codeforces) | 5 | 6 | `8 2` | `8 2` | **Aprovado** |
| [`dados/2.txt`](dados/2.txt) | Caso limite sem arestas ($m = 0$) | 3 | 0 | `5 1` | `5 1` | **Aprovado** |
| [`dados/3.txt`](dados/3.txt) | Exemplo 1 oficial do Codeforces | 3 | 3 | `3 1` | `3 1` | **Aprovado** |
| [`dados/4.txt`](dados/4.txt) | Exemplo 3 oficial do Codeforces com empates múltiplos | 10 | 12 | `15 6` | `15 6` | **Aprovado** |

---

## 12. Evidência de submissão e `Accepted`

A solução está implementada e pronta no arquivo autossuficiente `src/inlined.py`. O envio na plataforma Codeforces para a submissão oficial gerará a evidência gráfica a ser anexada em `evidencias/accepted.png`.

---

## 13. Apresentação

O planejamento da apresentação de 5 minutos foi estruturado no [Marco 4](acompanhamento/marco-4.md), com a seguinte divisão de tempo e papéis para o Grupo J:

* **00:00 - 01:00 (1 min):** Problema, modelagem como dígrafo e classificação (Vinícius);
* **01:00 - 03:00 (2 min):** Conectividade forte, critério algorítmico de Kosaraju e rastreamento da instância (Daniel);
* **03:00 - 04:00 (1 min):** Complexidade linear $\mathcal{O}(V + E)$, testes e arquitetura `algs4` (Pedro);
* **04:00 - 05:00 (1 min):** Relações estruturais (não aplicabilidade de coloração/emparelhamento), casos de borda e conclusão (Pedro).

---

## 14. Declaração sobre o uso de Inteligência Artificial

Ferramentas de Inteligência Artificial generativa foram utilizadas como apoio à organização da documentação, à formalização conceitual dos contraexemplos e à estruturação do código adaptado da biblioteca `algs4`. Toda a modelagem matemática, código-fonte e rastreamentos foram revisados, compreendidos e validados pela equipe.
