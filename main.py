import grafo

def menu():
    print("\n🚍 Bem-vindo à Agência JBA 🚍")
    print("Sua melhor opção para viajar com conforto e segurança!")

grafo = grafo.Grafo()

grafo.add_aresta('A', 'B', 10)  # A está conectada a B (10 km)
grafo.add_aresta('B', 'C', 15)  # B está conectada a C (15 km) # O rio separa A e B das demais cidades, e há uma ponte entre B e C.
grafo.add_aresta('C', 'D', 12)  # C está conectada a D (12 km)

while True:
    menu()
    cidades = input("Digite a sequência de cidades separadas por espaço (exemplo: A B C D): ").split()
    
    if len(cidades) < 2:
        print("⚠️ Você deve inserir pelo menos duas cidades para calcular a rota!")
        continue
    
    rota_completa = []
    distancia_total = 0
    
    for i in range(len(cidades) - 1):
        origem, destino = cidades[i], cidades[i + 1]
        resultado = grafo.dijkstra(origem, destino)
        
        if resultado is None:
            print(f"❌ Não foi possível encontrar um caminho entre {origem} e {destino}.")
            break
        else:
            distancia, caminho = resultado
            rota_completa.extend(caminho[:-1])
            distancia_total += distancia
    
    rota_completa.append(cidades[-1])
    
    print("\n🚌 Sua viagem está pronta!")
    print("➡️ Saindo para embarque...")
    for i, cidade in enumerate(rota_completa):
        if i == 0:
            print(f"🏁 Partida: {cidade}")
        elif i == len(rota_completa) - 1:
            print(f"🏁 Chegada: {cidade}")
        else:
            print(f"🚏 Próxima parada: {cidade}")
    print(f"🛣️ Distância total: {distancia_total} km")
    
    continuar = input("Deseja fazer outra viagem? (s/n): ").strip().lower()
    if continuar != 's':
        print("Obrigado por viajar com a Agência JBA! ✈️")
        break
