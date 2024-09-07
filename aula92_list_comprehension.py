"""
List comprehensio em Python
List comprehensio é uma forma rápida para criar listas 
a partir de iteráveis.
"""
# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero 
    for numero in range(10) if numero % 2 == 0]
print(lista)