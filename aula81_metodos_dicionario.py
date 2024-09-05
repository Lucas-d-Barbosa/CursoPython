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

p1 = {
    'nome' : 'Lucas',
    'sobrenome' : 'Barbosa'

}

# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultimo_item = p1.popitem()
# print(ultimo_item[0],ultimo_item[1], sep=": ")
# print(p1)

# p1.update({
#     'nome' : 'Hiago',
#     'idade' : 22,
# })

# p1.update(nome='Hiago', idade=22)

# atualizacao_dict = (('nome', 'Hiago'),('idade', 22))
atualizacao_dict = [['nome', 'Hiago'],['idade', 22]]
p1.update(atualizacao_dict)


print(p1)