"""
1. Lista Encadeada (Linked List)
Implementação de uma lista encadeada simples com métodos para
inserir, remover e buscar elementos.
"""


class No:
    """Nó da lista encadeada."""

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    """Lista encadeada simples."""

    def __init__(self):
        self.cabeca = None

    def inserir_no_inicio(self, dado):
        """Insere um elemento no início da lista."""
        novo_no = No(dado)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def inserir_no_final(self, dado):
        """Insere um elemento no final da lista."""
        novo_no = No(dado)
        if self.cabeca is None:
            self.cabeca = novo_no
            return
        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo_no

    def remover(self, dado):
        """Remove a primeira ocorrência do elemento na lista.
        Retorna True se removeu, False caso contrário."""
        if self.cabeca is None:
            return False

        if self.cabeca.dado == dado:
            self.cabeca = self.cabeca.proximo
            return True

        atual = self.cabeca
        while atual.proximo is not None:
            if atual.proximo.dado == dado:
                atual.proximo = atual.proximo.proximo
                return True
            atual = atual.proximo
        return False

    def buscar(self, dado):
        """Busca um elemento na lista.
        Retorna True se encontrado, False caso contrário."""
        atual = self.cabeca
        while atual is not None:
            if atual.dado == dado:
                return True
            atual = atual.proximo
        return False

    def exibir(self):
        """Retorna uma representação em string da lista."""
        elementos = []
        atual = self.cabeca
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return " -> ".join(elementos)

    def __str__(self):
        return self.exibir()


# --- Exemplo de uso ---
if __name__ == "__main__":
    lista = ListaEncadeada()

    # Inserindo elementos
    lista.inserir_no_final(10)
    lista.inserir_no_final(20)
    lista.inserir_no_final(30)
    lista.inserir_no_inicio(5)
    print(f"Lista: {lista}")  # 5 -> 10 -> 20 -> 30

    # Buscando elementos
    print(f"Buscar 20: {lista.buscar(20)}")  # True
    print(f"Buscar 99: {lista.buscar(99)}")  # False

    # Removendo elementos
    lista.remover(20)
    print(f"Após remover 20: {lista}")  # 5 -> 10 -> 30

    lista.remover(5)
    print(f"Após remover 5: {lista}")  # 10 -> 30
