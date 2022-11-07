from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''

        arestasReais = []
        for i in self.arestas:
            arestaCorrente = self.arestas[i]
            verticesNasArestas = f'{arestaCorrente.v1}-{arestaCorrente.v2}'
            arestasReais.append(verticesNasArestas)
        verticesNaoAdjacentes = set()
        for i in range(len(self.vertices)):
            for j in range(i+1, len(self.vertices)):
                verticesPossiveis = f'{self.vertices[i]}-{self.vertices[j]}'
                if verticesPossiveis not in arestasReais and verticesPossiveis[::-1] not in arestasReais:
                    verticesNaoAdjacentes.add(verticesPossiveis)
        return verticesNaoAdjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.arestas:
            if self.arestas[a].v1 == self.arestas[a].v2:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V): raise VerticeInvalidoError

        g = 0
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V:
                g += 1
            if self.arestas[a].v2.rotulo == V:
                g += 1

        return g

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        temp = []
        for a in self.arestas:
            aresta = f'{self.arestas[a].v1}-{self.arestas[a].v2}'
            if aresta in temp:
                return True  
            else:
                temp.append(aresta)
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V): raise VerticeInvalidoError
        temp = set()

        for a in self.arestas:
            flagV1 = (V == self.arestas[a].v1.rotulo)
            flagV2 = (V == self.arestas[a].v2.rotulo)
            temp.add(a) if (flagV1 or flagV2) else {}

        return temp

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        numArestasPossiveis=0
        for i in range(len(self.vertices)):
            for j in range(i+1, len(self.vertices)):
                numArestasPossiveis+=1

        if(not MeuGrafo.ha_laco(self) and not MeuGrafo.ha_paralelas(self) and numArestasPossiveis==len(self.arestas)):
            return True
        else:
            return False

    def dfs(self, V=' '):

        arv_dfs = MeuGrafo()
        arv_dfs.adiciona_vertice(V)

        return self.dfs_aux_rec(V, arv_dfs)

    def dfs_aux_rec(self, V, arv_dfs):

        if len(self.vertices) == len(arv_dfs.vertices):
            return arv_dfs

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        rotulo = self.arestas_sobre_vertice(V)
        rotulos = list(rotulo)
        rotulos.sort()

        for a in rotulos:
            if not arv_dfs.existe_rotulo_vertice(a):

                if V == self.arestas[a].v1.rotulo:
                    r = self.arestas[a].v2.rotulo
                else:
                    r = self.arestas[a].v1.rotulo

                if not arv_dfs.existe_rotulo_vertice(r):
                    arv_dfs.adiciona_vertice(r)
                    arv_dfs.adiciona_aresta(self.arestas[a])

                    arv_dfs = self.dfs_aux_rec(r, arv_dfs)

        return arv_dfs



    def bfs(self, V=' '):

        arv_bfs = MeuGrafo()
        arv_bfs.adiciona_vertice(V)
        ordem = list()

        return self.bfs_aux_rec(V, arv_bfs, ordem)

    def bfs_aux_rec(self, V, arv_bfs, ordem):

        if len(self.vertices) == len(arv_bfs.vertices):
            print(ordem)
            return arv_bfs

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V and self.arestas[a].v1.rotulo != self.arestas[a].v2.rotulo:
                aux = self.arestas[a].v1.rotulo
                prox = self.arestas[a].v2.rotulo

                if arv_bfs.existe_rotulo_vertice(aux) and not arv_bfs.existe_rotulo_vertice(prox):
                    arv_bfs.adiciona_vertice(prox)
                    arv_bfs.adiciona_aresta(self.arestas[a])
                    ordem.append("{}-{}".format(self.arestas[a].v1.rotulo, self.arestas[a].v2.rotulo))

        self.bfs_aux_rec(prox, arv_bfs, ordem)

        return arv_bfs

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
g_p2.adiciona_aresta('a4', 'P', 'C')
g_p2.adiciona_aresta('a6', 'T', 'C')
g_p2.adiciona_aresta('a8', 'M', 'T')
g_p2.adiciona_aresta('a9', 'T', 'Z')

print(g_p.bfs("J"))
