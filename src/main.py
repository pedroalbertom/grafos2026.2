import sys

from algs4.graph import Graph
from algs4.breadth_first_paths import BreadthFirstPaths

# abrir dataset ou usar stdin como um
dataset = None
if len(sys.argv) > 1:
    dataset = open(sys.argv[1])
else:
    dataset = sys.stdin

# obter numero de vertices (computadores) e arestas (conexões)
vertex_count, edges_count = map(int, dataset.readline().split(" "))
graph = Graph(vertex_count)

# obtendo e criando as arestas entre os vértices
for edge in range(edges_count):
    # NOTA: a entrada do problema é 1-indexada, então removemos 1 para tornar 0 indexada
    a, b = map(lambda x: int(x) - 1, dataset.readline().split())
    graph.add_edge(a, b)

# realizando o BFS
bfs = BreadthFirstPaths(graph, 0)
path = bfs.path_to(vertex_count - 1)

if path:
    # transformando o iterator em uma lista (e tornando o resultado 1-indexado)
    elems = [str(v + 1) for v in path]
    print(len(elems))
    print(" ".join(elems))
else:
    # não existe rota
    print("IMPOSSIBLE")

_ = dataset.close()
