"""
map para mapear dados

"""
from functools import partial
from dados import produtos
from types import GeneratorType

def print_iter(iterador):
    print(*list(iterador), sep="\n")
    print()

def aumentar_procentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(
    aumentar_procentagem,
    porcentagem = 1.1
)

def muda_preco_produto(produto):
    return {
        **produto, 'preco' : aumentar_dez_porcento(
            produto['preco']
        )
    }

# novos_produtos = map(
#     lambda produto: produto['preco'] * 1.5, produtos
# )

novos_produtos = list(map(
    muda_preco_produto, produtos
))
print_iter(novos_produtos) # vira um map object
novos_produtos = list(novos_produtos)
print(type(novos_produtos))
print(isinstance(novos_produtos, GeneratorType))

for i in novos_produtos:
    print(i)

