"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = iter('Lucas') #__iter__()

# for letra in texto
texto = 'Lucas' #iterável
iterador = iter(texto) #iterator

while True:
    try:
        letra = next(iterador)
        print(letra,end="")
    except StopIteration:
        print()
        break

# for letra in texto:
#     print(letra, end="")