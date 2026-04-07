"""
8. Busca em Largura (BFS - Breadth-First Search)
Implementa uma função que realiza a busca em largura no grafo
e retorna a ordem dos vértices visitados.
"""

from collections import deque


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


def bfs(grafo, vertice_inicial):
    """Realiza a busca em largura (BFS) no grafo.

    Args:
        grafo: instância de Grafo
        vertice_inicial: vértice de onde a busca começa

    Returns:
        Lista de vértices visitados na ordem da BFS.
    """
    visitados = []
    fila = deque([vertice_inicial])
    visitados.append(vertice_inicial)

    while fila:
        vertice = fila.popleft()
        for vizinho, _peso in grafo.obter_vizinhos(vertice):
            if vizinho not in visitados:
                visitados.append(vizinho)
                fila.append(vizinho)

    return visitados


# --- Exemplo de uso ---
if __name__ == "__main__":
    grafo = Grafo()
    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("A", "C")
    grafo.adicionar_aresta("B", "D")
    grafo.adicionar_aresta("C", "D")
    grafo.adicionar_aresta("D", "E")

    print(f"BFS a partir de 'A': {bfs(grafo, 'A')}")
    # Esperado: ['A', 'B', 'C', 'D', 'E']
