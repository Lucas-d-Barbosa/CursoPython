"""
Aumente os preços dos produtos a seguir em 10%
Gere novos_produtos por deep copy (cópia profunda)

"""
from dados import produtos

novos_produtos = [
    {'nome' : produto['nome'], 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in produtos
]

produtos_ordenador_por_nome = sorted(
    novos_produtos.copy(), 
    reverse = True, 
    key = lambda item : item['nome']
)

produtos_ordenador_por_preco = sorted(
    novos_produtos.copy(), 
    key = lambda item: item['preco']
)


print(*novos_produtos, sep="\n")
print()
print(*produtos_ordenador_por_nome, sep="\n")
print()
print(*produtos_ordenador_por_preco, sep="\n")
print()
print(*produtos, sep="\n")