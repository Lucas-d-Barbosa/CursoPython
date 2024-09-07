"""
Iterando strings com while
"""
nome = 'Lucas Barbosa' # Iteráveis

tamanho_nome = len(nome)
novo_nome = ''
cont = 0
while cont < tamanho_nome:
    novo_nome += f'*{nome[cont]}'
    cont += 1
print(novo_nome)