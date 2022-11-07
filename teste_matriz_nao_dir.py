from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        g = 0
        arestasUnicas = []
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if(self.matriz[i][j]!={}):
                    for k in self.matriz[i][j]:
                        if self.matriz[i][j][k].rotulo not in arestasUnicas:
                            if self.matriz[i][j][k].v1.rotulo == V:
                                g += 1
                            if self.matriz[i][j][k].v2.rotulo == V:
                                g += 1
                            arestasUnicas.append(self.matriz[i][j][k].rotulo)
        return g

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V): raise VerticeInvalidoError
        temp = set()

        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if(self.matriz[i][j]!={}):
                    for k in self.matriz[i][j]:
                        flagV1 = (V == self.matriz[i][j][k].v1.rotulo)
                        flagV2 = (V == self.matriz[i][j][k].v2.rotulo)
                        if (flagV1 or flagV2): temp.add(k)
        return temp
        


g_p = MeuGrafo()
g_p.adiciona_vertice("J")
g_p.adiciona_vertice("C")
g_p.adiciona_vertice("E")
g_p.adiciona_vertice("P")
g_p.adiciona_vertice("M")
g_p.adiciona_vertice("T")
g_p.adiciona_vertice("Z")
g_p.adiciona_aresta('a1', 'J', 'C')
g_p.adiciona_aresta('a2', 'C', 'E')
g_p.adiciona_aresta('a3', 'C', 'E')
g_p.adiciona_aresta('a4', 'P', 'C')
g_p.adiciona_aresta('a5', 'P', 'C')
g_p.adiciona_aresta('a6', 'T', 'C')
g_p.adiciona_aresta('a7', 'M', 'C')
g_p.adiciona_aresta('a8', 'M', 'T')
g_p.adiciona_aresta('a9', 'T', 'Z')

g_p2 = MeuGrafo()
g_p2.adiciona_vertice("J")
g_p2.adiciona_vertice("C")
g_p2.adiciona_vertice("E")
g_p2.adiciona_vertice("P")
g_p2.adiciona_vertice("M")
g_p2.adiciona_vertice("T")
g_p2.adiciona_vertice("Z")
g_p2.adiciona_aresta('a1', 'J', 'C')
g_p2.adiciona_aresta('a2', 'C', 'E')
g_p2.adiciona_aresta('a3', 'C', 'E')
g_p2.adiciona_aresta('a4', 'P', 'C')
g_p2.adiciona_aresta('a5', 'P', 'C')
g_p2.adiciona_aresta('a6', 'T', 'C')
g_p2.adiciona_aresta('a7', 'M', 'C')
g_p2.adiciona_aresta('a8', 'M', 'T')
g_p2.adiciona_aresta('a9', 'T', 'Z')

g_l2 = MeuGrafo()
g_l2.adiciona_vertice("A")
g_l2.adiciona_vertice("B")
g_l2.adiciona_vertice("C")
g_l2.adiciona_vertice("D")
g_l2.adiciona_aresta('a1', 'A', 'B')
g_l2.adiciona_aresta('a2', 'B', 'B')
g_l2.adiciona_aresta('a3', 'B', 'A')

# Grafos com laco
g_l1 = MeuGrafo()
g_l1.adiciona_vertice("A")
g_l1.adiciona_vertice("B")
g_l1.adiciona_vertice("C")
g_l1.adiciona_vertice("D")
g_l1.adiciona_aresta('a1', 'A', 'A')
g_l1.adiciona_aresta('a2', 'A', 'B')
g_l1.adiciona_aresta('a3', 'A', 'A')

print(g_p.grau('C'))