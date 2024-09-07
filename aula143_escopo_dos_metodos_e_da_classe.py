"""
Escopo da classe e de métodos da classe
"""

class Animal:
    # nome = "Leão"

    def __init__(self, nome) -> None:
        self.nome = nome
        variavel = 'valor'
        # print(variavel)

    def comendo(self, alimento="algo"):
        # print(variavel) # erro
        # print(nome) # erro
        print(f'{self.nome} está comendo {alimento}!')

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal("Leão")
print(leao.nome)
leao.executar("carne")