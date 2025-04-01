```python
class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        # A tabela começa com 10 posições, todas com valor None
        self.tabela = [None] * 10

    def funcao_hash(self, sigla):
        # A função hash segue as regras descritas:
        if sigla == "DF":
            return 7
        return (ord(sigla[0]) + ord(sigla[1])) % 10
    
    def inserir(self, sigla, nomeEstado):
        # Insere o estado no início da lista encadeada
        indice = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla, nomeEstado)
        
        # Inserir no início da lista
        novo_nodo.proximo = self.tabela[indice]
        self.tabela[indice] = novo_nodo

    def imprimir_tabela(self):
        # Imprime os estados em cada posição da tabela hash
        for i in range(10):
            print(f"Posição {i}: ", end="")
            atual = self.tabela[i]
            if atual is None:
                print("Vazio")
            else:
                estados = []
                while atual:
                    estados.append(atual.sigla)
                    atual = atual.proximo
                print(" -> ".join(estados))
