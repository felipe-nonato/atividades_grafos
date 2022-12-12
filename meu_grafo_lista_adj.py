from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoListaAdjacencia):

    # auxiliares de prim

    def reverse(self, V, a):
        if a.v1.rotulo == V:
            V = a.v2.rotulo
            return V
        else:
            V = a.v1.rotulo
            return V

    # prim
    def prim(self, v):
        prim = MeuGrafo()
        next = self.arestas[]
        visitados = []
        prim.adiciona_vertice(next)
        while True:
            if len(self.vertices) == len(prim.vertices):
                break
            sobre = self.arestas_sobre_vertice(next)
            menor = float('inf')
            ares_menor = ''
            for a in sobre:
                if self.arestas[a].peso <= menor:
                    if not prim.existe_rotulo_vertice(self.reverse(next, self.arestas[a])):
                        ares_menor = self.arestas[a]
                        menor = self.arestas[a].peso
            visitados.append(ares_menor)
            if ares_menor.v1.rotulo == next:
                next = ares_menor.v2.rotulo
            else:
                next = ares_menor.v1.rotulo
            if not prim.existe_rotulo_vertice(next):
                prim.adiciona_vertice(next)
                prim.adiciona_aresta(ares_menor)

        return prim

    # Auxiliares kruskall
    def sortAux(self):
        sorted = []
        menor = float('inf')
        for a in self.arestas:
            if self.arestas[a].peso <= menor and not a in sorted:
                menor = self.arestas[a].peso
        while len(sorted) < len(self.arestas):
            for a in self.arestas:
                if self.arestas[a].peso == menor:
                    sorted.append(a)
            menor += 1
        return sorted

    def bucket_sort(self):
        lista_pesos = []
        for a in self.arestas:
            if not self.arestas[a].peso in lista_pesos:
                lista_pesos.append(self.arestas[a].peso)
        lista_pesos.sort()
        bucket = list()
        for i in range(len(lista_pesos)):
            bucket.append([])
            for a in self.arestas:
                if self.arestas[a].peso == lista_pesos[i]:
                    bucket[i].append(a)
        return bucket

    # kruskall
    def kruskall(self):
        arv_final = MeuGrafo()
        row = self.bucket_sort()
        for v in self.vertices:
            arv_final.adiciona_vertice(v.rotulo)

        for i in range(len(row)):
            for a in row[i]:
                aresta = self.arestas[a]
                kruskall_dfs = arv_final.dfs(aresta.v1.rotulo)

                if kruskall_dfs.existe_rotulo_vertice(aresta.v1.rotulo) and kruskall_dfs.existe_rotulo_vertice(
                        aresta.v2.rotulo):
                    pass
                else:
                    arv_final.adiciona_aresta(aresta)

        return arv_final

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