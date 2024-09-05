"""
Dicionários em python (tipo dict)
Dicionários são estruturas de dados do tipo
par de chave e valor
Chaves podem ser consideradas como o indíce
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc
o valor pode ser de qualquer tipo, incluindo 
outro tipo dicionario
Usamos as chaves - {} ou a classe dict para criar dicionarios
Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list

pessoa = {
    'nome' : 'Francisco Lucas',
    'Sobrenome': 'Barbosa',
    'idade': 22,
    'altura': 1.72,
    'endereco': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'tal tal', 'numero': 123}
    ]
}


""" 

# pessoa = {
#     'nome' : 'Francisco Lucas',
#     'Sobrenome': 'Barbosa',
#     'idade': 22,
#     'altura': 1.72,
#     'endereco': [
#         {'rua': 'João Fechine', 'numero': 123},
#         {'rua': 'tal tal', 'numero': 123}
#     ]
# }

# print(pessoa['endereco'][0]['rua'])

# pessoa = dict(nome='Francisco Lucas', sobrenome='Santos')

pessoa = {
    'nome' : 'Francisco Lucas',
    'sobrenome': 'Barbosa',
    'idade': 22,
    'altura': 1.72,
    'endereco': [
        {'rua': 'João Fechine', 'numero': 123},
        {'rua': 'tal tal', 'numero': 123}
    ]
}

# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])
print()
for chave in pessoa:
    print(chave, pessoa[chave])