"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, exetend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou de um índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - estende a lista
    + - Concatena listas

"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(f'{lista_c = }')
print(f'{lista_a = }')