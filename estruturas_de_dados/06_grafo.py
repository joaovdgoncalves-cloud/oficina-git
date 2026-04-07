"""
6. Grafo (Graph)
Implementação de um grafo não direcionado utilizando um dicionário
para listas de adjacência, com métodos para adicionar vértices e arestas.
"""


class Grafo:
    """Grafo não direcionado com lista de adjacência."""

    def __init__(self):
        self.adjacencia = {}

    def adicionar_vertice(self, vertice):
        """Adiciona um vértice ao grafo."""
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2, peso=1):
        """Adiciona uma aresta entre dois vértices (não direcionado).
        Cria os vértices automaticamente se não existirem."""
        self.adicionar_vertice(vertice1)
        self.adicionar_vertice(vertice2)
        self.adjacencia[vertice1].append((vertice2, peso))
        self.adjacencia[vertice2].append((vertice1, peso))

    def obter_vizinhos(self, vertice):
        """Retorna os vizinhos de um vértice."""
        return self.adjacencia.get(vertice, [])

    def obter_vertices(self):
        """Retorna todos os vértices do grafo."""
        return list(self.adjacencia.keys())

    def exibir(self):
        """Exibe o grafo."""
        for vertice, vizinhos in self.adjacencia.items():
            vizinhos_str = ", ".join(
                f"{v}(peso={p})" for v, p in vizinhos
            )
            print(f"  {vertice} -> [{vizinhos_str}]")

    def __str__(self):
        linhas = []
        for vertice, vizinhos in self.adjacencia.items():
            vizinhos_str = ", ".join(
                f"{v}(peso={p})" for v, p in vizinhos
            )
            linhas.append(f"  {vertice} -> [{vizinhos_str}]")
        return "Grafo:\n" + "\n".join(linhas)


# --- Exemplo de uso ---
if __name__ == "__main__":
    grafo = Grafo()

    # Adicionando vértices e arestas
    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("A", "C")
    grafo.adicionar_aresta("B", "D")
    grafo.adicionar_aresta("C", "D")
    grafo.adicionar_aresta("D", "E")

    print(grafo)

    # Verificando vizinhos
    print(f"\nVizinhos de 'A': {grafo.obter_vizinhos('A')}")
    print(f"Vizinhos de 'D': {grafo.obter_vizinhos('D')}")
    print(f"Vértices: {grafo.obter_vertices()}")
