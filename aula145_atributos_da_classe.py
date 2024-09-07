# Atributos da classe

class Pessoa:
    ano_atual = 2024
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
        

p1 = Pessoa('Lucas', 22)
p2 = Pessoa('Luiz', 19)

# Pessoa.ano_atual = 1 
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print()
print(Pessoa.ano_atual)