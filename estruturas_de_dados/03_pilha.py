"""
3. Pilha (Stack)
Implementação de uma pilha usando uma lista em Python,
com métodos push (empilhar), pop (desempilhar) e is_empty (verificar se está vazia).
"""


class Pilha:
    """Pilha (LIFO - Last In, First Out)."""

    def __init__(self):
        self.itens = []

    def push(self, elemento):
        """Empilha um elemento (adiciona ao topo)."""
        self.itens.append(elemento)

    def pop(self):
        """Desempilha um elemento (remove do topo).
        Retorna o elemento removido ou None se a pilha estiver vazia."""
        if self.is_empty():
            print("Pilha vazia! Não é possível desempilhar.")
            return None
        return self.itens.pop()

    def is_empty(self):
        """Verifica se a pilha está vazia."""
        return len(self.itens) == 0

    def topo(self):
        """Retorna o elemento do topo sem removê-lo."""
        if self.is_empty():
            return None
        return self.itens[-1]

    def tamanho(self):
        """Retorna o tamanho da pilha."""
        return len(self.itens)

    def __str__(self):
        return f"Pilha: {self.itens} <- topo"


# --- Exemplo de uso ---
if __name__ == "__main__":
    pilha = Pilha()

    # Empilhando elementos
    pilha.push(10)
    pilha.push(20)
    pilha.push(30)
    print(pilha)  # Pilha: [10, 20, 30] <- topo

    # Desempilhando elementos
    removido = pilha.pop()
    print(f"Removido: {removido}")  # 30
    print(pilha)  # Pilha: [10, 20] <- topo

    # Verificando o topo
    print(f"Topo: {pilha.topo()}")  # 20

    # Verificando se está vazia
    print(f"Pilha vazia? {pilha.is_empty()}")  # False

    # Tamanho da pilha
    print(f"Tamanho: {pilha.tamanho()}")  # 2
