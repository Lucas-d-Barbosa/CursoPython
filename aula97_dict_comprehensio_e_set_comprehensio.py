produto = {
    'nome' : 'Caneta Preta',
    'preco' : 2.5,
    'categoria' : 'Escritório'
}


print(produto.items())

dc = {
    chave: valor * 1.1
    if chave == 'preco'
    else valor 
    for chave, valor in produto.items()
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
]

dc = {
    chave: valor
    for chave, valor in lista
}


s1 = {i for i in range(10)}
print(dc)
print(s1)