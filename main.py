import heapq
from grafo import Grafo

def menu():
    print("\n=====================================")
    print("Bem-vindo à Agência de Ônibus JBA!  ")
    print("=======================================")
    print("Seu destino começa aqui! Vamos rodar!")
    print("\nDigite as cidades para viajar (Ex: A B C D E F), ou 'sair' para encerrar:")

def mostrar_rota(distancia, caminho):
    print("\n🚍 Embarque confirmado!")
    print(f"\nDistância total da rota: {distancia} km")
    print("\n🛣️ Próxima parada: " + " -> ".join(caminho))
    print("\nAproveite sua viagem!")

def main():
    grafo = Grafo()

    # Conexões entre as cidades, levando em consideração a geografia fictícia
    grafo.add_aresta('A', 'B', 10)  # Cidade A e B conectadas
    grafo.add_aresta('A', 'C', 15)  # Cidade A e C conectadas
    grafo.add_aresta('A', 'D', 30)  # Cidade A e D conectadas
    grafo.add_aresta('B', 'D', 50)  # Cidade B e D conectadas
    grafo.add_aresta('C', 'D', 25)  # Cidade C e D conectadas
    grafo.add_aresta('E', 'F', 70)  # Cidade E e F conectadas
    grafo.add_aresta('B', 'F', 100)  # Cidade B e F conectadas
    grafo.add_aresta('A', 'E', 40)  # Cidade A e E conectadas
    grafo.add_aresta('B', 'C', 20)  # Cidade B e C conectadas
    grafo.add_aresta('C', 'E', 60)  # Cidade C e E conectadas

    while True:
        menu()
        entrada = input("Sua escolha: ").strip().lower()

        if entrada == "sair":
            print("\nAté logo! Agradecemos pela preferência da Agência JBA!")
            break

        cidades = entrada.split()
        if len(cidades) < 2:
            print("Por favor, digite pelo menos duas cidades para calcular a rota.")
            continue

        origem = cidades[0].upper()
        destino = cidades[-1].upper()

        distancia, caminho = grafo.dijkstra(origem, destino)

        if distancia is None:
            print("\n⚠️ Não foi possível encontrar um caminho entre as estações fornecidas.")
        else:
            print(f"\n🚍 Embarque confirmado! Rota de {origem} a {destino}")
            print(f"\nDistância total da rota: {distancia} km")
            print(f"🛣️ Rota: {' -> '.join(caminho)}")
            print("\nAproveite sua viagem com a Agência JBA!")

if __name__ == "__main__":
    main()
