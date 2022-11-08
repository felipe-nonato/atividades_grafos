from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):
    def drone_dijkstra(self,vi,vf):
            peso = {}
            visitada = {}
            predecessor = {}
            for i in range(len(self.vertices)):
                for j in range(len(self.vertices)):
                    if(self.matriz[i][j]!={}):
                        for k in self.matriz[i][j]:
                            print(self.matriz[i][j][k])

a = MeuGrafo()
a.adiciona_vertice('A')
a.adiciona_vertice('B')
a.adiciona_vertice('C')
a.adiciona_vertice('D')
a.adiciona_aresta('a1','A','B',2)
a.adiciona_aresta('a2','A','C',5)
a.adiciona_aresta('a3','C','D',1)
a.adiciona_aresta('a4','D','B',3)
a.drone_dijkstra('A','B')