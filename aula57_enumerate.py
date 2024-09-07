"""
enumerate para enumerar valores
 ...iteráveis (índices)
"""

lista = ['Lucas', 'Francisco', 'Barbosa']
lista.append('João')

for indice,nome in enumerate(lista):
    print(indice,nome, sep=" - ")

print()

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice,nome, sep=" - ")
