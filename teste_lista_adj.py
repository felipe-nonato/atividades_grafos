from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoListaAdjacencia):

    def arestaMenorPeso(self):
        listaArestas = list(self.arestas)
        menorPeso = listaArestas[0]

        for a in self.arestas:
            if (self.arestas[a].peso < self.arestas[menorPeso].peso):
                menorPeso = a

        return self.arestas[menorPeso].v1

    def prim(self):
        verticeInicial = self.arestaMenorPeso()

        novoGrafo = MeuGrafo([verticeInicial])
        listaDeVertices = [verticeInicial]

        while len(self.vertices) != len(listaDeVertices):
            vMenorPeso = float('inf')
            verticeForaDaArvore = 0
            arestaMenorPeso = 0

            for a in self.arestas:
                arestaAtual = self.arestas[a]
                vertice1 = arestaAtual.v1
                vertice2 = arestaAtual.v2

                if vertice1 in listaDeVertices and vertice2 not in listaDeVertices:
                    if arestaAtual.peso < vMenorPeso:
                        vMenorPeso = arestaAtual.peso
                        arestaMenorPeso = a
                        verticeForaDaArvore = vertice2

                elif vertice2 in listaDeVertices and vertice1 not in listaDeVertices:
                    if arestaAtual.peso < vMenorPeso:
                        vMenorPeso = arestaAtual.peso
                        arestaMenorPeso = a
                        verticeForaDaArvore = vertice1

            if arestaMenorPeso == 0:
                return False

            arestaMenorPeso = self.arestas[arestaMenorPeso]
            listaDeVertices.append(verticeForaDaArvore)
            novoGrafo.adiciona_vertice(verticeForaDaArvore)

            arestaF = arestaMenorPeso.rotulo
            v1F = arestaMenorPeso.v1
            v2F = arestaMenorPeso.v2
            pesoF = arestaMenorPeso.peso

            print()

            novoGrafo.adiciona_aresta(Aresta(arestaF,v1F,v2F,pesoF))

        return novoGrafo

    def kruskall(self):
        '''
        Provê um novo grafo após o algoritmo de kruskal
        :return: novo grafo com algotimo de kruskal aplicado
        '''
        arvore = MeuGrafo(self.vertices)
        sortArestas = {}

        for a in self.arestas:
            sortArestas[self.arestas[a].rotulo] = self.arestas[a].peso

        sortArestas = sorted(sortArestas, key=sortArestas.get)

        cont = 0

        while True:
            if not arvore.caminho(self.arestas[sortArestas[cont]].v1, self.arestas[sortArestas[cont]].v2):
                arvore.adiciona_aresta(Aresta(self.arestas[sortArestas[cont]].rotulo, self.arestas[sortArestas[cont]].v1, self.arestas[sortArestas[cont]].v2,
                                      self.arestas[sortArestas[cont]].peso))
            cont += 1
            if arvore.conexo():
                break

        return arvore

    def caminho(grafo, v1, v2):
        g = grafo.bfs(v1)

        for i in g.arestas:
            if g.arestas[i].v1 == v2 or g.arestas[i].v2 == v2:
                return True
        return False
    # Codigos adjacentes
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



    def bfs(self, V=''):

        bfs = MeuGrafo(self.vertices[::])

        verticesVisitados = [V]
        fila = [V]

        temVertice = False

        for v in self.vertices:
            if v == V:
                temVertice = True

        while (len(fila) != 0):
            for a in self.arestas:
                v1 = self.arestas[a].v1
                v2 = self.arestas[a].v2
                verticeAnalisado = fila[0]

                if v1 == verticeAnalisado or v2 == verticeAnalisado:
                    verticeAdjacente = v2 if verticeAnalisado == v1 else v1

                    if verticeAdjacente not in verticesVisitados:
                        fila.append((verticeAdjacente))
                        verticesVisitados.append(verticeAdjacente)
                        bfs.adiciona_aresta(Aresta(a, verticeAnalisado, verticeAdjacente))

            fila.pop(0)

        if not temVertice:
            raise VerticeInvalidoError("O vértice", V, "não existe no grafo")
        else:
            return bfs

    def bfs_aux(self, V=''):
        bfs = MeuGrafo([V])

        verticesVisitados = [V]
        fila = [V]
        listaBfs = [V]

        while (len(fila) != 0):
            for a in self.arestas:
                v1 = self.arestas[a].v1
                v2 = self.arestas[a].v2
                verticeAnalisado = fila[0]

                if v1 == verticeAnalisado or v2 == verticeAnalisado:
                    verticeAdjacente = v2 if verticeAnalisado == v1 else v1

                    if verticeAdjacente not in verticesVisitados:
                        bfs.adiciona_vertice(verticeAdjacente)
                        fila.append((verticeAdjacente))
                        verticesVisitados.append(verticeAdjacente)
                        bfs.adiciona_aresta(Aresta(a, verticeAnalisado, verticeAdjacente))
                        listaBfs.append(verticeAdjacente)

            fila.pop(0)
        return listaBfs
    def conexo(self):
            '''
            Verifica se o grafo é conexo
            :return: Um valor booleano que indica se o grafo é ou não conexo
            '''
            grafo_bfs = self.bfs_aux(self.vertices[0])
            tamanhoGrafoBfs = len(grafo_bfs)
            tamanhoGrafoAnalisado = len(self.vertices)

            if (tamanhoGrafoBfs != tamanhoGrafoAnalisado):
                    return False
            else:
                    return True
# Grafo da Paraíba sem arestas paralelas
gc = MeuGrafo()
gc.adiciona_vertice("J")
gc.adiciona_vertice("C")
gc.adiciona_vertice("E")
gc.adiciona_vertice("P")
gc.adiciona_aresta('a1', 'J', 'C')
gc.adiciona_aresta('a2', 'J', 'E')
gc.adiciona_aresta('a3', 'J', 'P')
gc.adiciona_aresta('a4', 'E', 'C')
gc.adiciona_aresta('a5', 'P', 'C')
gc.adiciona_aresta('a6', 'P', 'E')


# print(gc.prim())
print(gc.kruskall())
