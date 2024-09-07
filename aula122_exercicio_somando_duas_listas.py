def somar_listas(lista_a, lista_b):
    tamanho = min(len(lista_a), len(lista_b))
    nova_lista = [
        lista_a[i] + lista_b[i]
        for i in range(tamanho)
    ]

    return nova_lista
    
        

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [2, 4, 7, 8, 9]
print("(", end="")
print(*somar_listas(lista_a, lista_b), sep=", ",end=")\n")