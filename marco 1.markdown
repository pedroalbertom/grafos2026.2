message route

Syrjälä's network has n computers and m connections. Your task is to find out if Uolevi can send a message to Maija, and if it is possible, what is the minimum number of computers on such a route.
Input
The first input line has two integers n and m: the number of computers and connections. The computers are numbered 1,2,\dots,n. Uolevi's computer is 1 and Maija's computer is n.
Then, there are m lines describing the connections. Each line has two integers a and b: there is a connection between those computers.
Every connection is between two different computers, and there is at most one connection between any two computers.
Output
If it is possible to send a message, first print k: the minimum number of computers on a valid route. After this, print an example of such a route. You can print any valid solution.
If there are no routes, print "IMPOSSIBLE".

precisamos gerar esse artefato descrevendo as seguintes caracteristicas desse grafo/problema

Marco 1 — Modelagem

enunciado:
 O PPROBLEMA CONSISTE EM DESCOBRIR SE É POSSIVEL ENVIAR UMA MENSAGEM DE UM COMPUTADOR A PARA B E, CASO SEJA, DESCOBRIR OS NUMEROS DE COMPUTADORES E AS ROTAS 
entrada:
 3 entradas: n eh o numero de computadores, m eh o numero de conexoes e a lista de conexoes entre os computadores.
saida:
 k o numero minimo de computadores numa rota valida e um exemplo de rota valida. se nao houver rota valida, printar impossible
restricoes:
 minimo de computadores = 2; maximo de computadores: 10⁵
 numero de conexoes vai de 1 a 2*10⁵
 1 <= a, b <= n, a e b sao computadores e sempre vao estar entre 1 e n

vértices:
 computadores
arestas:
 conexoes entre os computadores
tipo de grafo:
 grafo simples, pois a conexao nao eh direcionada, nao existem laços nem arestas paralelas.
instancia pequena:
n = 5
m = 5
[a,b] = [(1,2), (1,3), (1,4), (2,3), (5,4)]
 
resultado esperado:
3
1 4 5

hipótese inicial de solução:
fazer uma busca em largura e checar a existencia de um caminho possivel, escolher o menor;
BFS BREADTH FIRST SEARCH
DFS DEPTH FIRST SEARCH

