import heapq # Ele permite inserir e remover elementos mantendo-os ordenados de forma eficiente.

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
    
    # Função para encontrar o menor caminho entre dois vértices (Algoritmo de Dijkstra)
    
    def dijkstra(self, origem, destino):
        if origem not in self.grafo or destino not in self.grafo: # Verifica se o grafo possui origem e destino
            return None # Não possui algum dos dois.

        distancias = {vertice: float('inf') for vertice in self.grafo} # Inicializa a distância como inf, pois os vértices são considerados inalcançáveis. !!!
        distancias[origem] = 0 # Exceto a origem, começa de 0.
        pq = [(0, origem)]  # (distância, vértice) # Priority Queue, deixa o vértice com menor distância no topo.
        caminho = {} # Armazena o caminho (predecessores). 

        while pq: # Enquanto houver elementos na fila de prioridade.
            distancia_atual, vertice_atual = heapq.heappop(pq) # Pega o vértice mais próximo (menor distância) da fila pq com heapq.heappop(pq)

            if vertice_atual == destino: #  Se o vértice atual for o destino, paramos – porque já encontramos o menor caminho até ele.
                break

            for vizinho, peso in self.grafo[vertice_atual]: # Percorre os vizinhos do vértice atual
                nova_distancia = distancia_atual + peso # Calcula a distância acumulada até esse vizinho

                if nova_distancia < distancias[vizinho]: # Se encontramos um caminho mais curto até o vizinho...
                    distancias[vizinho] = nova_distancia # Atualiza a menor distância conhecida até ele
                    heapq.heappush(pq, (nova_distancia, vizinho)) # Adiciona na fila para processar futuramente
                    caminho[vizinho] = vertice_atual # Guarda de onde viemos para reconstruir o caminho depois

        # Reconstruir o caminho
        caminho_final = [] # Caminho inverso (destino até a origem).
        vertice = destino # Início da reconstrução.
        while vertice != origem: # Enquanto não chegarmos na origem...
            caminho_final.append(vertice) # Adicionamos o vértice atual ao caminho
            vertice = caminho[vertice] # Voltamos para o vértice anterior no caminho mais curto
        caminho_final.append(origem) # Adicionamos a origem, já que o loop parou antes de incluí-la
        caminho_final.reverse() # Como adicionamos de trás para frente, invertamos a lista para ficar na ordem correta

        return distancias[destino], caminho_final # Retorna a menor distância e a sequência até o caminho final.