# def ziper(lista1, lista2):
#     tamanho_menor_lista = len(lista1) if len(lista1) < len(lista2) else len(lista2) 
#     nova_lista = [
#         (lista1[cont], lista2[cont])
#         for cont in range(tamanho_menor_lista)
#     ]
#     return nova_lista
    

# lista1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
# lista2 = ["BA","SP", "MG", "RJ"]

# print(ziper(lista1, lista2))

from itertools import zip_longest # o mesmo que o zip mas usando a maior lista

lista1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
lista2 = ["BA","SP", "MG", "RJ"]
nova_lista = []
for i in zip(lista1, lista2):
    nova_lista.append(i)

print(nova_lista)