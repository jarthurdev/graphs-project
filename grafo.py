import heapq ###
from collections import deque # Double Ended Queue - Manipular os lados da fila de forma mais fácil (E&D).

class Grafo:

    def __init__(self): # Construtor referente à própria classe = Grafo.
        self.grafo = {} # Criação do dicionário vazio, para receber os valores. <------

    def add_vertice(self, vertice): # Função para adição de vértice. #FAZER O MENU, PARA EVITAR BUGS.
        if vertice not in self.grafo: # Verifica se o vértice já existe no grafo.
            self.grafo[vertice] = []    # Caso não exista, adiciona uma chave ao dicionário do self.grafo. ----->

    def add_aresta(self, origem, destino, peso): # Função para adição de aresta.
        self.add_vertice(origem) # Garante o vértice de início
        self.add_vertice(destino) # Garante o vértice do fim
        self.grafo[origem].append((destino, peso)) # ---->
        self.grafo[destino].append((origem, peso)) # <----

    def exibir(self):
        for vertice in self.grafo:
            print(f"{vertice} -> {self.grafo[vertice]}")

    # Função para verificar se há um caminho entre dois vértices (Busca em Largura - BFS)

    def verificar_conexao(self, origem, destino):
        if origem not in self.grafo or destino not in self.grafo: # Verifica se o grafo possui origem e destino
            return False # Não possui algum dos dois.

        visitados = set() # Inicializa um set para indicar os pontos que foram visitados
        fila = deque([origem]) # Inicialização da fila com o vértice de origem

        while fila:
            vertice = fila.popleft() # Enquanto houver elementos na fila, remove os elementos que entraram primeiro. **

            if vertice == destino: # Verificação com o vértice de destino.
                return True # Destino encontrado.

            for vizinho, _ in self.grafo[vertice]: # Percorre os vizinhos do vértice.
                if vizinho not in visitados: # Verifica se o vizinho ainda não foi visitado.
                    visitados.add(vizinho) # Marca como visitado.
                    fila.append(vizinho) # É adicionado na fila para que seja explorado isoladamente. **

        return False # Se não há destino, retorna False.