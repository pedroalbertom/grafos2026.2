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

O Marco 1 foi registrado. Neste momento, o repositório contém a modelagem, a classificação do grafo, a relação com DFS/BFS e uma instância pequena rastreada manualmente.

- [Marco 1 — Problema e conhecimento prévio](acompanhamento/marco-1.md)

Os marcos seguintes ainda não foram produzidos. Implementação, testes completos, evidência de submissão e apresentação serão adicionados somente após o avanço do trabalho.

---

## 4. Linguagem e ambiente de execução

A linguagem do T2 ainda será definida entre Python e Java, conforme a implementação de referência escolhida e a orientação da disciplina. Ainda não há programa executável neste diretório.

Quando a implementação for criada, esta seção deverá informar:

* a linguagem e a versão utilizada;
* os comandos de compilação ou execução;
* a forma de fornecer a entrada por arquivo ou por `stdin`;
* as dependências diretas mantidas no repositório.

---

## 5. Estrutura do repositório

Estrutura esperada para a conclusão do T2:

```text
T2/
├── README.md
├── acompanhamento/
│   ├── marco-1.md              # produzido
│   ├── marco-2.md              # será produzido posteriormente
│   ├── marco-3.md              # será produzido posteriormente
│   └── marco-4.md              # será produzido posteriormente
├── apresentacao/
│   └── apresentacao.pdf        # será adicionado posteriormente
├── dados/
│   └── casos-de-teste.txt      # será adicionado posteriormente
├── evidencias/
│   └── accepted.png ou .pdf    # será adicionado após a submissão
└── src/
    └── Main.java ou main.py    # será implementado posteriormente
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

O critério formal, os estados adicionais da busca e a adaptação da implementação serão registrados nos marcos posteriores, depois do conteúdo teórico correspondente.

---

## 9. Algoritmo, implementação de referência e adaptações

Ainda não há algoritmo implementado no T2. A hipótese inicial é:

1. representar o dígrafo com listas de adjacência;
2. identificar as componentes fortemente conexas com uma estratégia baseada em DFS;
3. encontrar o menor custo e a quantidade de empates em cada componente;
4. somar os menores custos e multiplicar as quantidades módulo `1 000 000 007`.

A implementação de referência, as alterações e suas justificativas serão registradas quando a adaptação começar.

---

## 10. Complexidade

A hipótese inicial é uma solução com tempo `O(n + m)` e memória `O(n + m)`, compatível com os limites da entrada. A análise definitiva será feita após a escolha e a implementação do algoritmo.

---

## 11. Testes e validação

Até o Marco 1, há apenas a instância pequena usada para validar a modelagem e o resultado esperado. Os testes de implementação deverão incluir posteriormente:

* a instância pequena;
* uma única componente fortemente conexa;
* várias componentes sem ciclos entre si;
* empates de menor custo;
* custos iguais a zero;
* o caso-limite `m = 0`.

---

## 12. Evidência de submissão e `Accepted`

Ainda não há implementação submetida nem evidência de `Accepted`. O arquivo correspondente será adicionado em `evidencias/` após a conclusão e a validação da solução.

---

## 13. Apresentação

A apresentação será preparada posteriormente com foco em:

* problema e modelagem;
* classificação do dígrafo;
* DFS/BFS e conectividade forte;
* critério algorítmico;
* complexidade, testes e casos especiais.

---

## 14. Declaração sobre o uso de Inteligência Artificial

Durante o Marco 1, ferramentas de Inteligência Artificial generativa foram utilizadas como apoio à organização da documentação, à revisão da modelagem e à estruturação do rastreamento da instância pequena. O grupo deverá revisar, validar, compreender e adaptar todo conteúdo e código utilizado nos marcos seguintes, conforme as exigências do trabalho.
