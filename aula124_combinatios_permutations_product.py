"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa - iterável + tamanho do grupo
Permutação - Ordem importa
Produto - Ordem importa e repete valores únicos

"""
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*iterator, sep="\n")

pessoas = [
    'João', 'Joana', 'Lucas', 'Letícia'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g', 'gg'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster'],
]

# print_iter(list(combinations(pessoas, 3)))
# print()
# print()
# print_iter(list(permutations(pessoas, 3)))
print_iter(list(product(*camisetas)))