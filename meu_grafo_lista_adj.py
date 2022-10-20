from sys import flags
from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *
import re

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

    def dfs(self, V=''):
        # Verificando se existe vertice
        V = Vertice(V)
        verticesVisitados = []
        grafoFinal = MeuGrafo()
        vertice = V
        ultimoNumero = int(re.findall(r'\d+', list(self.arestas)[-1])[0])+1

        for a in self.arestas:
            if((a not in grafoFinal.arestas) and (self.arestas[a].v2 not in verticesVisitados)):
                verticesVisitados.append(vertice)
                vertice = self.arestas[a].v2
                grafoFinal.adiciona_vertice(self.get_vertice(vertice))
                grafoFinal.adiciona_aresta("a"+str(ultimoNumero),a.v1.rotulo,a.v2.rotulo)
                self.dfs(self, vertice)
        return grafoFinal

        
    def bfs(self, V=''):
        pass