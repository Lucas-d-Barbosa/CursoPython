"""
Entendendo self em Python
Classe - Molde (geralmente sem dados)
Instnância da classe (objeto) - Tem os dados
Uma classe pode gerar várias instâncias.
Na classe o self é a própria instâcia.
"""

class Carro:
    def __init__(self, marca, nome):
        self.marca = marca
        self.nome = nome
    
    def acelerar(self):
        return f'O {self.nome} está acelerando!'

fusca = Carro("Volkswagen", "Fusca")
# print(fusca.nome, fusca.marca, sep=" - ")
# print(fusca.acelerar())
print(Carro.acelerar(fusca))