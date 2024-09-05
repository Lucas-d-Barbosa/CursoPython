"""
Cuidados com dados mutáveis
= - Copiado o valor (imutáveis)
= - Aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Lucas'
# outra_variavel = nome
# nome = "Barbosa"
# print(nome)
# print(outra_variavel)

lista_a = ['Lucas','Barbosa', [1, 2, 3]] 
lista_b = lista_a.copy()
lista_a[0] = 'Qualquer coisa'
lista_a[2][1] = 4
print(lista_a)
print(lista_b)