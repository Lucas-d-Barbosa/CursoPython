"""
Valores Truthy e Falsy, tipos mutáveis e imutáveis
Mutáveis [] {} set()
Imutáveis () "" 0 0.0 None False range(0, 10)

"""

lista = [0]
dicionario = {'nome' : 'Lucas'}
conjunto = set((1, 2))
tupla = (1, 2)
string = ' '
inteiro = 1
flutuante = 0.1
nada = not None
falso = True
intervalo = range(0, 1)


def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE {falsy("TESTE")}')
print(f'{lista=} {falsy(lista)}')
print(f'{dicionario=} {falsy(dicionario)}')
print(f'{conjunto=} {falsy(conjunto)}')
print(f'{tupla=} {falsy(tupla)}')
print(f'{string=} {falsy(string)}')
print(f'{inteiro=} {falsy(inteiro)}')
print(f'{flutuante=} {falsy(flutuante)}')
print(f'{nada=} {falsy(nada)}')
print(f'{falso=} {falsy(falso)}')
print(f'{intervalo=} {falsy(intervalo)}')