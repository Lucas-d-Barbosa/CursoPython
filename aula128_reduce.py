# reduce - faz a redução de um iterável em um valor
from functools import reduce
from dados import produtos

def funcao_do_reduce(acumulador, produto):
    return round(acumulador + produto['preco'], 2)


# valor_estoque = reduce(
#     lambda acumulador, produto: produto['preco'] + acumulador,
#     produtos, 
#     0
# )

valor_estoque = reduce(
    funcao_do_reduce,
    produtos, 
    0
)


print(valor_estoque)
