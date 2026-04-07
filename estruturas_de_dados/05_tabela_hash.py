"""
5. Tabela Hash (Hash Table)
Implementação de uma tabela hash simples com métodos para
insert (inserir), search (buscar) e delete (remover) elementos.
"""


class TabelaHash:
    """Tabela Hash com tratamento de colisões por encadeamento."""

    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        """Função hash: calcula o índice a partir da chave."""
        return hash(chave) % self.tamanho

    def insert(self, chave, valor):
        """Insere um par chave-valor na tabela.
        Se a chave já existir, atualiza o valor."""
        indice = self._hash(chave)
        for i, (c, v) in enumerate(self.tabela[indice]):
            if c == chave:
                self.tabela[indice][i] = (chave, valor)
                return
        self.tabela[indice].append((chave, valor))

    def search(self, chave):
        """Busca um valor pela chave.
        Retorna o valor se encontrado, None caso contrário."""
        indice = self._hash(chave)
        for c, v in self.tabela[indice]:
            if c == chave:
                return v
        return None

    def delete(self, chave):
        """Remove um par chave-valor pela chave.
        Retorna True se removeu, False caso contrário."""
        indice = self._hash(chave)
        for i, (c, v) in enumerate(self.tabela[indice]):
            if c == chave:
                del self.tabela[indice][i]
                return True
        return False

    def exibir(self):
        """Exibe o conteúdo da tabela hash."""
        for i, bucket in enumerate(self.tabela):
            if bucket:
                print(f"  Índice {i}: {bucket}")

    def __str__(self):
        linhas = []
        for i, bucket in enumerate(self.tabela):
            if bucket:
                linhas.append(f"  Índice {i}: {bucket}")
        return "TabelaHash:\n" + "\n".join(linhas)


# --- Exemplo de uso ---
if __name__ == "__main__":
    tabela = TabelaHash()

    # Inserindo elementos
    tabela.insert("nome", "João")
    tabela.insert("idade", 25)
    tabela.insert("cidade", "São Paulo")
    tabela.insert("curso", "Computação")

    print(tabela)

    # Buscando elementos
    print(f"\nBuscar 'nome': {tabela.search('nome')}")      # João
    print(f"Buscar 'idade': {tabela.search('idade')}")      # 25
    print(f"Buscar 'email': {tabela.search('email')}")      # None

    # Removendo elementos
    tabela.delete("idade")
    print(f"\nApós remover 'idade': {tabela.search('idade')}")  # None

    # Atualizando elementos
    tabela.insert("nome", "Maria")
    print(f"Após atualizar 'nome': {tabela.search('nome')}")   # Maria
