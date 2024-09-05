"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)

#Lembre-se de desempacotamento

"""

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

# def soma(*args):
#     soma = 0
#     for i in args:
#           soma += i
#     return soma
          
def soma(*args, cont = 0):
    total = 0
    for numero in args:
        total += numero + cont
    return total
numeros = 1, 2, 3, 4, 5, 6, 7
soma_resultado = soma(*numeros)
print(soma_resultado)
print(sum((1, 2, 3, 4, 5, 6, 7)))
