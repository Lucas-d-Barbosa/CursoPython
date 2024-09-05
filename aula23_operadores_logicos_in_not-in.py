# Operadores in e not in
# Strings são interáveis
# 0 1 2 3 4 - Positivos
# L u c a s
#-5-4-3-2-1 - Negativos

# nome = 'Lucas'
# print(nome[0], nome[-5])
# print('a' in nome)
# print('z' in nome)
# print('a' not in nome)
# print('z' not in nome)

nome = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
