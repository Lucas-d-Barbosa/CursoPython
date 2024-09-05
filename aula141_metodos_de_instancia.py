"""
Métodos em instância de classes Python
Hard coded = Algo que foi escrito diretamente no código
"""

class Carro:
    def __init__(self, marca, nome):
        self.marca = marca
        self.nome = nome
    
    def acelerar(self):
        return f'O {self.nome} está acelerando!'

fusca = Carro("Volkswagen", "Fusca")
print(fusca.nome, fusca.marca, sep=" - ")
print(fusca.acelerar())
