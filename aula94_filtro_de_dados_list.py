import pprint

def exibir_lista(lista):
    pprint.pprint(lista, sort_dicts=False, width=50)


produtos = [
    {'nome': 'p1', 'preco' : 20},
    {'nome': 'p2', 'preco' : 15},
    {'nome': 'p3', 'preco' : 10}
]

produtos_promocao = [
    {**produto, 'preco' : produto['preco'] * 0.9}
    if produto['preco'] >= 20 else {**produto}
    for produto in produtos
    if produto['preco'] * 0.9 >= 10
]
# print(*produtos_promocao, sep='\n')
exibir_lista(produtos_promocao)

lista = [
    i ** 2
    if i > 4 else i
    for i in range(10)
    if i % 2 == 0
]
exibir_lista(lista)