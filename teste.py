from bibgrafo.vertice import Vertice
from bibgrafo.aresta import Aresta
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia

J = Vertice("J")
C = Vertice("C")
E = Vertice("E")
P = Vertice("P")
M = Vertice("M")
T = Vertice("T")
Z = Vertice("Z")

a1 = Aresta("a1",J,C)
a2 = Aresta("a2",C,E)
a3 = Aresta("a3",C,E)
a4 = Aresta("a4",C,P)
a5 = Aresta("a5",C,P)
a6 = Aresta("a6",C,M)
a7 = Aresta("a7",C,T)
a8 = Aresta("a8",M,T)
a9 = Aresta("a9",T,Z)

grafo = GrafoListaAdjacencia(
    [J, C, E, P, M, T, Z],
    {1:a1, 2:a2, 3:a3, 4:a4, 5:a5, 6:a6, 7:a7, 8:a8, 9:a9}
)

temp = []
for a in grafo.arestas:
    aresta = f'{grafo.arestas[a].v1}-{grafo.arestas[a].v2}'
    print("Identifiquei paralela") if aresta in temp else temp.append(aresta)