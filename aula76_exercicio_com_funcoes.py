def multiplicar(vezes):
    def numero(numero):
        return vezes * numero
    return numero

triplicar = multiplicar(3)
quadriplicar = multiplicar(4)
duplicar = multiplicar(2);
print(triplicar(5))
print(quadriplicar(4))
print(duplicar(16))


# def fatorial(n, y = 0):
#     y = n - 1
#     if y == 1:
#         return n
#     n *= fatorial(y, y - 1)
#     return n
# print(fatorial(4))