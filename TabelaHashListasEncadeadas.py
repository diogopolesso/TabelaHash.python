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
# Criando a tabela hash 
tabela = TabelaHash() 
# Lista de siglas e seus respectivos nomes de estados e distrito federal 
estados = [ 
("SP", "São Paulo"), ("RJ", "Rio de Janeiro"), ("MG", "Minas Gerais"), 
("BA", "Bahia"), ("PR", "Paraná"), ("SC", "Santa Catarina"), 
("RS", "Rio Grande do Sul"), ("GO", "Goiás"), ("ES", "Espírito Santo"), 
("PE", "Pernambuco"), ("DF", "Distrito Federal"), ("AM", "Amazonas"), 
("PA", "Pará"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), 
("CE", "Ceará"), ("MA", "Maranhão"), ("PB", "Paraíba"), ("RN", "Rio Grande 
do Norte"), 
("AL", "Alagoas"), ("SE", "Sergipe"), ("TO", "Tocantins"), ("PI", 
"Piauí"), 
("RO", "Rondônia"), ("AC", "Acre"), ("AP", "Amapá"), ("RR", "Roraima") 
] 
# Inserindo os estados na tabela 
for sigla, nome in estados: 
tabela.inserir(sigla, nome) 
# Inserindo o estado fictício "BK" (Bruno Kostiuk) 
tabela.inserir("BK", "Estado Fictício - Bruno Kostiuk") 
# Imprimir a tabela hash 
tabela.imprimir_tabela()

