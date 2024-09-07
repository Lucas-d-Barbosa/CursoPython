# __dict__ e vars para atributos de instncia
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
        

dados = {'nome': 'Luiz', 'idade': 19}
p2 = Pessoa(**dados) #desempacotei um dicionario para criar minha classe
print(vars(p2))
p1 = Pessoa('Lucas', 22)

# p1.nome = 'EITA'
# del p1.nome # apaga o atributo referenciado
print(p1.__dict__) # Mostra os atributos e seus valores CUIDADO!!
# __dict__ não é só leitura p1.__dict__['nome'] = 'eita' altera o atributo nome
print(vars(p1)) # Mostra os atributos e seus valores
