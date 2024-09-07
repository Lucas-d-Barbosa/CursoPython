"""
A função lambda é uma função como qualquer outra
em python. Porém, são funções anônimas que contêm apenas
uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.

lista = [
    {'nome': 'Lucas', 'sobrenome': 'Barbosa'},
    {'nome': 'Luiz', 'sobrenome': 'Dantas'},
    {'nome': 'Eduardo', 'sobrenome': 'Batista'},

]

"""

# lista = [4, 32, 1, 34, 5, 6]

# lista.sort(reverse=True) # Modifica a lista original e ordenada
# # sorted(lista) # cria uma nova lista modificada e ordenada

lista = [
    {'nome': 'Lucas', 'sobrenome': 'Barbosa'},
    {'nome': 'Luiz', 'sobrenome': 'Dantas'},
    {'nome': 'Eduardo', 'sobrenome': 'Batista'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

# lista.sort(key = lambda item: item['sobrenome'])

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)