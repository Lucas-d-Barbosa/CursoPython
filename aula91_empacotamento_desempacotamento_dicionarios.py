a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome' : 'Lucas',
    'sobrenome' : 'Barbosa'
}

"""
args e kwargs
args (Já vimos)
kwargs - kayword arguments (argumentos nomeados)

"""
# nome, sobrenome = pessoa, pessoa # (Isso me retorna as chaves 'nome'e 'sobrenome')
# nome, sobrenome = pessoa['nome'], pessoa['sobrenome'] traz os valores
# nome, sobrenome = pessoa.values() # traz os valores 
# nome_tupla, sobrenome_tupla = pessoa.items() # cria tuplas composta de chaves e valores 
# (a1, a2), b = pessoa.items() # nome é desempacotado em a1 chave e a2 fica com o valor e b fica com sobrenome chave e o valor
# print(nome, sobrenome)
# print(nome_tupla, sobrenome_tupla)
# print(a1, a2, b)


# for chave, valor in pessoa.items():
#     print(chave, valor, sep=" - ")

pessoa = {
    'nome' : 'Lucas',
    'sobrenome' : 'Barbosa'
}

dados_pessoa = {
    'idade': 22,
    'altura': 1.6
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados: ', args)

    for chave, valor in kwargs.items():
        print(chave.upper(), valor, sep=" - ")
    print()

mostro_argumentos_nomeados(1, 2, pessoa='Lucas Barbosa', animal='Leão')
mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'velocidade' : 4,
    'forca' : 70.4,
    'destreza' : 7
}
mostro_argumentos_nomeados(**configuracoes)