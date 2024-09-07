"""
List comprehensio em Python
List comprehensio é uma forma rápida para criar listas 
a partir de iteráveis.
"""
# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]

lista = [
    int( numero / 2)
    for numero in lista
]



produtos = [
    {'nome': 'p1', 'preco' : 20},
    {'nome': 'p2', 'preco' : 15},
    {'nome': 'p3', 'preco' : 10}
]

produtos_promocao = [
    {**produto, 'preco' : produto['preco'] * 0.9}
    if produto['preco'] > 10
    else {**produto, 'preco' : produto['preco'] * 1.9}
    for produto in produtos
]
print(*produtos_promocao, sep='\n')