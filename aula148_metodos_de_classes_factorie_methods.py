"""
Métodos de classe
São métodos onde o "self" será "cls", ou seja, ao invés 
de receber a própria instância no primeiro parâmetro
recebemos a própria classe
"""

class Pessoa:
    ano = 2024 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print("Hey")

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls("Anônimo", idade)

p1 = Pessoa("Lucas",22)
p2 = Pessoa.criar_com_50_anos("Luiz")
p3 = Pessoa.criar_sem_nome(33)
p1.metodo_de_classe()
Pessoa.metodo_de_classe() # sem o @classmethod daria erro
# Pessoa.metodo_de_classe(p1)

print(p2.nome)
print(p3.nome)