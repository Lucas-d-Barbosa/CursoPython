pessoa = {}


chave = 'nome'
pessoa[chave] = 'Lucas Santos'
pessoa['sobrenome'] = 'Barbosa'

print(pessoa['nome'])

pessoa[chave] = 'Hiago Barbosa'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa['sobrenome'])
# if not pessoa.get('sobrenome', None) is None:
if not pessoa.get('sobrenome'):
    print('A chave sobrenome não existe!')

print('ISSO NÃO VAI EXECUTAR!')