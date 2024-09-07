"""
Relações entre classes: associação, agregação e composição
Agregação é uma forma mais especializada de associação
entre dois ou mais objetos. Cada objeto terá seu ciclo
de vida independente.
Geralmente é uma relação de um para muitos, onde um
objeto tem um ou muitos objetos.
Os objetos podem viver separadamente, mas pode se tratar de uma relação[
onde um objeto precisa de outro para fazer 
determinada tarefa
(Existem controvérias sobre a definição de agregação).

"""

class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return f"{sum([
            produto.preco
            for produto in self._produtos
        ]):.2f}"

    def lista_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco, sep=" - ")
        print()

    def inserir_produtos(self, *produtos):
        for p in produtos:
            self._produtos.append(p)

class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    @property
    def preco(self):
        return self._preco
    
    @property
    def nome(self):
        return self._nome
    
carrinho =  Carrinho()

p1, p2 = Produto('Caneta', 1.2), Produto('Camiseta', 24.90)
carrinho.inserir_produtos(p1, p2)
carrinho.lista_produtos()
print(carrinho.total())