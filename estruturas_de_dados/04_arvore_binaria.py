"""
4. Árvore Binária (Binary Tree)
Implementação de uma árvore binária de busca com métodos para inserir,
buscar e realizar travessias (in-order, pre-order e post-order).
"""


class NoArvore:
    """Nó da árvore binária."""

    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    """Árvore Binária de Busca (BST)."""

    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        """Insere um valor na árvore."""
        if self.raiz is None:
            self.raiz = NoArvore(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        """Método auxiliar recursivo para inserção."""
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = NoArvore(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = NoArvore(valor)
            else:
                self._inserir_recursivo(no.direita, valor)

    def buscar(self, valor):
        """Busca um valor na árvore.
        Retorna True se encontrado, False caso contrário."""
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, no, valor):
        """Método auxiliar recursivo para busca."""
        if no is None:
            return False
        if valor == no.valor:
            return True
        elif valor < no.valor:
            return self._buscar_recursivo(no.esquerda, valor)
        else:
            return self._buscar_recursivo(no.direita, valor)

    def em_ordem(self):
        """Travessia em ordem (in-order): esquerda -> raiz -> direita."""
        resultado = []
        self._em_ordem_recursivo(self.raiz, resultado)
        return resultado

    def _em_ordem_recursivo(self, no, resultado):
        if no is not None:
            self._em_ordem_recursivo(no.esquerda, resultado)
            resultado.append(no.valor)
            self._em_ordem_recursivo(no.direita, resultado)

    def pre_ordem(self):
        """Travessia pré-ordem (pre-order): raiz -> esquerda -> direita."""
        resultado = []
        self._pre_ordem_recursivo(self.raiz, resultado)
        return resultado

    def _pre_ordem_recursivo(self, no, resultado):
        if no is not None:
            resultado.append(no.valor)
            self._pre_ordem_recursivo(no.esquerda, resultado)
            self._pre_ordem_recursivo(no.direita, resultado)

    def pos_ordem(self):
        """Travessia pós-ordem (post-order): esquerda -> direita -> raiz."""
        resultado = []
        self._pos_ordem_recursivo(self.raiz, resultado)
        return resultado

    def _pos_ordem_recursivo(self, no, resultado):
        if no is not None:
            self._pos_ordem_recursivo(no.esquerda, resultado)
            self._pos_ordem_recursivo(no.direita, resultado)
            resultado.append(no.valor)


# --- Exemplo de uso ---
if __name__ == "__main__":
    arvore = ArvoreBinaria()

    # Inserindo elementos
    valores = [50, 30, 70, 20, 40, 60, 80]
    for v in valores:
        arvore.inserir(v)

    # Buscando elementos
    print(f"Buscar 40: {arvore.buscar(40)}")  # True
    print(f"Buscar 99: {arvore.buscar(99)}")  # False

    # Travessias
    print(f"Em ordem (in-order):   {arvore.em_ordem()}")    # [20, 30, 40, 50, 60, 70, 80]
    print(f"Pré-ordem (pre-order): {arvore.pre_ordem()}")   # [50, 30, 20, 40, 70, 60, 80]
    print(f"Pós-ordem (post-order): {arvore.pos_ordem()}")  # [20, 40, 30, 60, 80, 70, 50]
