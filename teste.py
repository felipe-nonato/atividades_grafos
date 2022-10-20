from bibgrafo.vertice import Vertice
from bibgrafo.aresta import Aresta
from meu_grafo_lista_adj import MeuGrafo
import re

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
a10 = Aresta("a10",T,Z)
grafo = MeuGrafo(
    [J, C, E, P, M, T, Z],
    {"a1":a1, "a2":a2, "a3":a3, "a4":a4, "a5":a5, "a6":a6, "a7":a7, "a8":a8, "a9":a9}
)

print(grafo.dfs("J"))