"""
10. Algoritmo de Dijkstra
Utiliza a estrutura de grafo para implementar o algoritmo de Dijkstra,
encontrando o caminho mais curto entre dois vértices.
Retorna a distância e o caminho.
"""

import heapq


class Grafo:
    """Grafo não direcionado com lista de adjacência (mesmo do exercício 6)."""

    def __init__(self):
        self.adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2, peso=1):
        self.adicionar_vertice(vertice1)
        self.adicionar_vertice(vertice2)
        self.adjacencia[vertice1].append((vertice2, peso))
        self.adjacencia[vertice2].append((vertice1, peso))

    def obter_vizinhos(self, vertice):
        return self.adjacencia.get(vertice, [])

    def obter_vertices(self):
        return list(self.adjacencia.keys())


def dijkstra(grafo, origem, destino):
    """Encontra o caminho mais curto entre dois vértices usando Dijkstra.

    Args:
        grafo: instância de Grafo
        origem: vértice de origem
        destino: vértice de destino

    Returns:
        Tupla (distancia, caminho) onde:
        - distancia: menor distância entre origem e destino
        - caminho: lista de vértices do caminho mais curto
        Retorna (float('inf'), []) se não houver caminho.
    """
    # Distâncias mínimas conhecidas
    distancias = {vertice: float("inf") for vertice in grafo.obter_vertices()}
    distancias[origem] = 0

    # Predecessores para reconstruir o caminho
    predecessores = {vertice: None for vertice in grafo.obter_vertices()}

    # Fila de prioridade: (distância, vértice)
    fila_prioridade = [(0, origem)]

    # Conjunto de vértices já processados
    processados = set()

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        # Pula se já foi processado com distância menor
        if vertice_atual in processados:
            continue
        processados.add(vertice_atual)

        # Se chegamos ao destino, podemos parar
        if vertice_atual == destino:
            break

        # Relaxa as arestas dos vizinhos
        for vizinho, peso in grafo.obter_vizinhos(vertice_atual):
            if vizinho not in processados:
                nova_distancia = distancia_atual + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = vertice_atual
                    heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    # Reconstrói o caminho
    caminho = []
    vertice = destino
    while vertice is not None:
        caminho.append(vertice)
        vertice = predecessores[vertice]
    caminho.reverse()

    # Se o caminho não começa pela origem, não há caminho
    if caminho[0] != origem:
        return float("inf"), []

    return distancias[destino], caminho


# --- Exemplo de uso ---
if __name__ == "__main__":
    grafo = Grafo()

    # Criando um grafo com pesos nas arestas
    grafo.adicionar_aresta("A", "B", 4)
    grafo.adicionar_aresta("A", "C", 2)
    grafo.adicionar_aresta("B", "D", 3)
    grafo.adicionar_aresta("B", "E", 1)
    grafo.adicionar_aresta("C", "B", 1)
    grafo.adicionar_aresta("C", "D", 5)
    grafo.adicionar_aresta("D", "E", 2)

    # Encontrando o caminho mais curto
    origem = "A"
    destino = "E"
    distancia, caminho = dijkstra(grafo, origem, destino)

    print(f"Caminho mais curto de '{origem}' até '{destino}':")
    print(f"  Distância: {distancia}")
    print(f"  Caminho: {' -> '.join(caminho)}")

    # Testando outros caminhos
    for dest in ["B", "C", "D", "E"]:
        dist, cam = dijkstra(grafo, "A", dest)
        print(f"\n  A -> {dest}: distância = {dist}, caminho = {' -> '.join(cam)}")
