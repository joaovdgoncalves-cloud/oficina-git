"""
2. Fila (Queue)
Implementação de uma fila utilizando uma lista em Python,
com métodos enqueue (enfileirar) e dequeue (desenfileirar).
"""


class Fila:
    """Fila (FIFO - First In, First Out)."""

    def __init__(self):
        self.itens = []

    def enqueue(self, elemento):
        """Enfileira um elemento (adiciona ao final da fila)."""
        self.itens.append(elemento)

    def dequeue(self):
        """Desenfileira um elemento (remove do início da fila).
        Retorna o elemento removido ou None se a fila estiver vazia."""
        if self.esta_vazia():
            print("Fila vazia! Não é possível desenfileirar.")
            return None
        return self.itens.pop(0)

    def frente(self):
        """Retorna o elemento da frente sem removê-lo."""
        if self.esta_vazia():
            return None
        return self.itens[0]

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.itens) == 0

    def tamanho(self):
        """Retorna o tamanho da fila."""
        return len(self.itens)

    def __str__(self):
        return f"Fila: {self.itens}"


# --- Exemplo de uso ---
if __name__ == "__main__":
    fila = Fila()

    # Enfileirando elementos
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)
    print(fila)  # Fila: [10, 20, 30]

    # Desenfileirando elementos
    removido = fila.dequeue()
    print(f"Removido: {removido}")  # 10
    print(fila)  # Fila: [20, 30]

    # Verificando a frente da fila
    print(f"Frente da fila: {fila.frente()}")  # 20

    # Verificando se está vazia
    print(f"Fila vazia? {fila.esta_vazia()}")  # False

    # Tamanho da fila
    print(f"Tamanho: {fila.tamanho()}")  # 2
