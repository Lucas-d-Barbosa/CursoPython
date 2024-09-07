"""
@property + @setter - getter e setter no modo Pythônico
- Como getter
- p/ evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo
- Código cliente é o código que usa seu código
"""

"""
method vs @classmethod vs @staticmethod
method - self, método de instância
@classmethod - cls, método da classe
@staticmethod - método estático (sem self, sem cls)

Atributos que começam com um ou dois underlines 
não devem ser usados fora da classe.
"""

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None
    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        if not isinstance(valor, str):
            raise ValueError("Valor inválido!")
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        if not isinstance(valor, str):
            raise ValueError("Valor inválido!")
        self._cor_tampa = valor
# getter  -> Obter Valor

caneta = Caneta("Azul")
caneta.cor = "Rosa"
caneta.cor_tampa = "Colorida"
print(caneta.cor)
print(caneta.cor_tampa)

