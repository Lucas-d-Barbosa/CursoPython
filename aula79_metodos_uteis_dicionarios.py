"""
Métodos úteis dos dicionários em Python 
len - quantas chaves (Não é um método)
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave 
pop - apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro

"""

pessoa = {
    'nome' : 'Francisco Lucas',
    'sobrenome': 'Barbosa',
    # 'idade': 900,

}

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

print(pessoa.setdefault('idade', 18))
print(pessoa['idade'])


for chave in pessoa.keys():
    print(pessoa[chave])


for valor in pessoa.values():
    print(valor)

for chave, valor in list(pessoa.items()):
    print(chave, valor, sep=": ")