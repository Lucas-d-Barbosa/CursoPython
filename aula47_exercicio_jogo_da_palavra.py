import os
# def mudar_char(palavra):
#     nova_string = ''
#     for i in range(len(palavra)):
#         nova_string += '*'
#     return nova_string

# def mudar_letra(palavra, letra, pos):
#     nova_string = ''
#     for i in range(len(palavra)):
#         if i == pos:
#             nova_string += letra
#         else:
#             nova_string += palavra[i] 
#     return nova_string

# palavra = 'Lucas'
# palavra_secreta = mudar_char(palavra)
# palvra_meio = ''
# i = 0
# chaces = 5
# while i < len(palavra) :
#     letra = input('Digite uma letra: ')
#     letra = letra[0]
#     if palavra.count(letra.upper()) or palavra.count(letra.lower()):
#         for j in range(len(palavra)):
#             if letra.upper() == palavra[j].upper():
#                 palavra_secreta = mudar_letra(palavra_secreta, palavra[j], j)
#                 i += 1
#     else:
#         chaces -= 1
#         print(f'Você errou! Número de chances restantes: '\
#               f'{chaces}')

#     if(chaces == 0):
#         break
#     print(f'{palavra_secreta}')
# else:
#     print('Parabéns! Você acertou a palavra!')

# if(chaces == 0):
#     print('Você perdeu!')

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0
while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    os.system('clear')
    print(f'Palavra formada: {palavra_formada}')
    if palavra_formada == palavra_secreta:
        print("VOCÊ GANHOU!! PARABÉNS!!")
        print(f"A palvra era: {palavra_formada}")
        print(f'Tentativas: {numero_tentativas}')
        palavra_secreta = 'perfume'
        letras_acertadas = ''
        numero_tentativas = 0