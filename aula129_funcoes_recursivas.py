"""
Funções recursivas e recursividade
Funções que podem se chamar de volta
Úteis p/ dividir problemas grandes em partes menores
Toda função recursiva dever ter:
  -  Um problema que possa ser dividido em partes menores
  -  Um caso recursivo que resolve o pequeno problema
  -  Um caso base que para a recursão
  -  fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120

"""
# import sys
# sys.setrecursionlimit(1005) # aumenta o limite de chamadas recursivas

def fatorial(inicio = 5):
    # Caso recursivo
    # Contar até chegar ao final
    if inicio == 1:
        return inicio
    inicio *= fatorial(inicio - 1)
    return inicio

print(fatorial(100))