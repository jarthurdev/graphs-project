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