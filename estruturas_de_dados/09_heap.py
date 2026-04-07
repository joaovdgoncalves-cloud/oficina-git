"""
9. Heap (Min-Heap)
Implementação de uma estrutura de heap (min-heap) em Python,
com métodos para insert (inserir) e extract (extrair o mínimo).
"""


class MinHeap:
    """Min-Heap: o menor elemento está sempre na raiz."""

    def __init__(self):
        self.heap = []

    def _pai(self, indice):
        """Retorna o índice do pai."""
        return (indice - 1) // 2

    def _filho_esquerdo(self, indice):
        """Retorna o índice do filho esquerdo."""
        return 2 * indice + 1

    def _filho_direito(self, indice):
        """Retorna o índice do filho direito."""
        return 2 * indice + 2

    def _trocar(self, i, j):
        """Troca dois elementos no heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _subir(self, indice):
        """Move o elemento para cima até restaurar a propriedade do heap."""
        while indice > 0:
            pai = self._pai(indice)
            if self.heap[indice] < self.heap[pai]:
                self._trocar(indice, pai)
                indice = pai
            else:
                break

    def _descer(self, indice):
        """Move o elemento para baixo até restaurar a propriedade do heap."""
        tamanho = len(self.heap)
        while True:
            menor = indice
            esquerdo = self._filho_esquerdo(indice)
            direito = self._filho_direito(indice)

            if esquerdo < tamanho and self.heap[esquerdo] < self.heap[menor]:
                menor = esquerdo
            if direito < tamanho and self.heap[direito] < self.heap[menor]:
                menor = direito

            if menor != indice:
                self._trocar(indice, menor)
                indice = menor
            else:
                break

    def insert(self, valor):
        """Insere um valor no heap."""
        self.heap.append(valor)
        self._subir(len(self.heap) - 1)

    def extract(self):
        """Extrai e retorna o menor elemento (raiz) do heap.
        Retorna None se o heap estiver vazio."""
        if len(self.heap) == 0:
            print("Heap vazio! Não é possível extrair.")
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimo = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer(0)
        return minimo

    def espiar(self):
        """Retorna o menor elemento sem removê-lo."""
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def tamanho(self):
        """Retorna o número de elementos no heap."""
        return len(self.heap)

    def esta_vazio(self):
        """Verifica se o heap está vazio."""
        return len(self.heap) == 0

    def __str__(self):
        return f"MinHeap: {self.heap}"


# --- Exemplo de uso ---
if __name__ == "__main__":
    heap = MinHeap()

    # Inserindo elementos
    valores = [35, 10, 25, 5, 15, 30, 20]
    for v in valores:
        heap.insert(v)
        print(f"Inserido {v}: {heap}")

    print(f"\nMenor elemento (espiar): {heap.espiar()}")  # 5

    # Extraindo elementos (sempre o menor)
    print("\nExtraindo elementos:")
    while not heap.esta_vazio():
        print(f"  Extraído: {heap.extract()} | Restante: {heap}")
