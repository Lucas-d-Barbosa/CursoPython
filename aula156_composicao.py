"""
Relações entre classes: associação, agregação e composição
Composição é uma especialização da agregação.
Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos
também são apagados.

"""

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.endereco = []
    
    def inserir_endereco(self, rua, numero):
        self.endereco.append(Endereco(rua, numero))
       

    def exibir_endereco(self):
        for endereco in self.endereco:
            print(endereco.endereco)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    @property
    def endereco(self):
        return f'Rua: {self.rua} - Nº: {self.numero}'

    def __del__(self):
        print("Apagando,",self.rua, self.numero)
cliente = Cliente("Lucas")
cliente.inserir_endereco("João Fechine", 214)
cliente.inserir_endereco("Três", 1166)
cliente.exibir_endereco()