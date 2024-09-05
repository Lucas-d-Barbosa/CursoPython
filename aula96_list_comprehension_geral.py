def divisao(x, y):
    return x / y

def multiplicacao(x, y):
    return x * y

def potenciacao(x, y):
    return x ** y

numeros = [1, 2, 3, 4, 5]
quadrado = [potenciacao(numero, 2) for numero in numeros]
dividido = [divisao(numero, 2) for numero in numeros]
multiplicado = [multiplicacao(numero, 2) for numero in numeros]

print(quadrado)
print(multiplicado)
print(dividido)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novos_numeros = [numero for numero in numeros if numero > 5]
outro_if = [numero * 100 if numero == 6 else numero for numero in numeros if numero % 2 == 0]
print(novos_numeros)
print(outro_if)

print(end="\n\n")

# for x in range(10):
#     for y in range(5):
#         print(x, y, sep=" - ")

linhas_e_colunas = [
    (x, y)
    if y != 2 else (x, y * 1000)
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2
]

print(linhas_e_colunas)

print(end="\n\n")


string = 'Lucas Barbosa'
nova_string = ''.join([letra if (letra != 'a' and letra != 'A')else '@' for letra in string])
numeros_de_letras = 1
nova_string = '.'.join([
    string[indice:indice + numeros_de_letras]
    for indice in range(0, len(string), numeros_de_letras)
])
print(nova_string)

nomes = ['Lucas', 'Luiz', 'Eduardo', 'Vinícius', 'Hans']

novos_nomes = [
    nome.lower()
    for nome in nomes
]

novos_nomes = [
    nome[0:len(nome) - 1].lower() + nome[len(nome) - 1].upper()
    for nome in nomes
]
print(novos_nomes)


print(end="\n\n")


numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x]
print(numeros)
print(flat)