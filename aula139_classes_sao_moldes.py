"""
class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que 
podem ter seus próprios atributos e métodos.
Os objetos gerados pela classe podem usar seus dados
internos para realizar várias ações.
Por convenção, usamos  PascalCase para nomes de classes.

"""

# string = 'Lucas' # str
# print(string.upper())  # método da classes str
# print(isinstance(string, str)) # verificando se essa variável é uma instância de str

class Pessoa:
    ...

p1 = Pessoa()
p1.sobrenome = "Barbosa"
p1.nome ="Lucas"

p2 = Pessoa()
p2.sobrenome = "Fernando"
p2.nome ="Luiz"

print(p1.nome, p1.sobrenome)

print(p2.nome, p2.sobrenome)
