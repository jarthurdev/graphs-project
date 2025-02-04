import grafo

grafo = grafo.Grafo()

grafo.add_aresta('Cidade A', 'Cidade B', 10)
grafo.add_aresta('Cidade A', 'Cidade C', 15)
grafo.add_aresta('Cidade B', 'Cidade C', 5)
grafo.add_aresta('Cidade B', 'Cidade D', 20)

grafo.exibir()