"""
Filter é um filtro funcional
"""
from dados import produtos

def print_iter(iterador):
    print(*list(iterador), sep="\n")
    print()

novos_produtos = list(filter(
    lambda produto: produto['preco'] <= 25,
    produtos
))

print_iter(novos_produtos)