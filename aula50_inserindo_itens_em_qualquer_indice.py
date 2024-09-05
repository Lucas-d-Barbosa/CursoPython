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

lista = [10, 20, 30, 40]
lista.append('Lucas Barbosa')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(200000000,'Pé de Feijão')
print(lista, nome)