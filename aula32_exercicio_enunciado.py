# 1º Exercício
# try:
#     num = int(input("Digite um número intero: "))
#     if(num % 2 == 0):
#         print(f'O número {num} é par!')
#     else:
#         print(f'O número {num} é impar!')
# except(ValueError):
#     print(f'{ValueError.__name__}! Você não digitou um número inteiro!')

# 2º Exercício
try:
    horario = int(input("Digite o horário atual: "))
    while(horario > 23 or horario < 0):
        horario = int(input("Digite o horário atual: "))
    if(horario >= 0 and horario <= 11):
        print("Bom dia!")
    elif(horario <= 17):
        print("Boa tarde!")
    else:
        print('Boa noite!')
except:
    print('Digite um número inteiro entre 0-23!')


# 3º Exercício
# nome = input("Digite seu primeiro nome: ")
# if len(nome) <= 4:
#     print(f'Seu nome "{nome}" é curto!')
# elif len(nome) <= 6:
#     print(f'Seu nome "{nome}" é normal!')
# else:
#     print(f'Seu nome "{nome}" é muito grande!')

