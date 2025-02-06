import grafo  # Importando o módulo do grafo para utilizar as funções

def menu():
    # Exibe o menu inicial
    print("\n🚍 Bem-vindo à Agência JBA 🚍")
    print("Sua melhor opção para viajar com conforto e segurança!")

# Criando um novo grafo para armazenar as cidades e conexões
grafo = grafo.Grafo()

# Adicionando conexões entre as cidades (arestas com distâncias em km)
grafo.add_aresta('A', 'B', 20)  # Conexão entre A e B (20 km)
grafo.add_aresta('B', 'F', 20)  # Conexão entre B e F (20 km)
grafo.add_aresta('F', 'E', 25)  # Conexão entre F e E (25 km)
grafo.add_aresta('C', 'A', 30)  # Conexão entre C e A (30 km)
grafo.add_aresta('C', 'E', 20)  # Conexão entre C e E (20 km)
grafo.add_aresta('E', 'D', 18)  # Conexão entre E e D (18 km)

# Loop principal para permitir múltiplas viagens
while True:
    menu()  # Mostra o menu toda vez que inicia uma nova consulta
    
    # Usuário insere a sequência de cidades que deseja percorrer
    cidades = input("Digite a sequência de cidades separadas por espaço (exemplo: A B C D E F): ").split()
    
    # Se o usuário inserir menos de duas cidades, avisa e pede novamente
    if len(cidades) < 2:
        print("⚠️ Você deve inserir pelo menos duas cidades para calcular a rota!")
        continue  # Volta para o início do loop
    
    rota_completa = []  # Lista para armazenar o caminho total percorrido
    distancia_total = 0  # Variável para armazenar a distância total da viagem
    
    # Percorre todas as cidades escolhidas pelo usuário
    for i in range(len(cidades) - 1):
        origem, destino = cidades[i], cidades[i + 1]  # Define a cidade de partida e destino
        resultado = grafo.dijkstra(origem, destino)  # Calcula a menor rota usando Dijkstra
        
        # Se não existir um caminho entre as cidades, exibe uma mensagem e interrompe a busca
        if resultado is None:
            print(f"❌ Não foi possível encontrar um caminho entre {origem} e {destino}.")
            break
        else:
            distancia, caminho = resultado  # Pega a distância e o caminho gerado pelo Dijkstra
            rota_completa.extend(caminho[:-1])  # Adiciona o caminho sem repetir a última cidade
            distancia_total += distancia  # Soma a distância ao total
    
    # Adiciona a última cidade na rota completa
    rota_completa.append(cidades[-1])
    
    # Exibe a viagem completa de forma estilizada
    print("\n🚌 Sua viagem está pronta!")
    print("➡️ Saindo para embarque...")
    for i, cidade in enumerate(rota_completa):
        if i == 0:
            print(f"🏁 Partida: {cidade}")  # Cidade inicial
        elif i == len(rota_completa) - 1:
            print(f"🏁 Chegada: {cidade}")  # Última cidade
        else:
            print(f"🚏 Próxima parada: {cidade}")  # Cidades intermediárias
    print(f"🛣️ Distância total: {distancia_total} km")  # Exibe a distância total da viagem
    
    # Pergunta se o usuário quer continuar ou sair
    continuar = input("Deseja fazer outra viagem? (s/n): ").strip().lower()
    if continuar != 's':
        print("Obrigado por viajar com a Agência JBA! ✈️")  # Mensagem de encerramento
        break  # Sai do loop e finaliza o programa
