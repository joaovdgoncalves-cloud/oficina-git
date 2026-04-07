"""
7. Busca em Profundidade (DFS - Depth-First Search)
Utiliza a estrutura de grafo (do exercício 6) para realizar a busca em
profundidade e retorna uma lista de vértices visitados.
"""


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


def dfs(grafo, vertice_inicial):
    """Realiza a busca em profundidade (DFS) no grafo de forma iterativa.

    Args:
        grafo: instância de Grafo
        vertice_inicial: vértice de onde a busca começa

    Returns:
        Lista de vértices visitados na ordem da DFS.
    """
    visitados = []
    pilha = [vertice_inicial]

    while pilha:
        vertice = pilha.pop()
        if vertice not in visitados:
            visitados.append(vertice)
            vizinhos = grafo.obter_vizinhos(vertice)
            for vizinho, _peso in reversed(vizinhos):
                if vizinho not in visitados:
                    pilha.append(vizinho)

    return visitados


def dfs_recursivo(grafo, vertice, visitados=None):
    """Realiza a busca em profundidade (DFS) de forma recursiva.

    Args:
        grafo: instância de Grafo
        vertice: vértice atual
        visitados: lista de vértices já visitados

    Returns:
        Lista de vértices visitados na ordem da DFS.
    """
    if visitados is None:
        visitados = []

    visitados.append(vertice)
    for vizinho, _peso in grafo.obter_vizinhos(vertice):
        if vizinho not in visitados:
            dfs_recursivo(grafo, vizinho, visitados)

    return visitados


# --- Exemplo de uso ---
if __name__ == "__main__":
    grafo = Grafo()
    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("A", "C")
    grafo.adicionar_aresta("B", "D")
    grafo.adicionar_aresta("C", "D")
    grafo.adicionar_aresta("D", "E")

    print(f"DFS iterativa a partir de 'A': {dfs(grafo, 'A')}")
    print(f"DFS recursiva a partir de 'A': {dfs_recursivo(grafo, 'A')}")
