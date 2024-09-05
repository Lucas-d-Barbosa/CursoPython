"""
Calculadora com while
"""
# try:
#     resultado = 0.0
#     while(True):
#         operacao = input("+ - * / C Q:")
#         if operacao.upper() == 'Q':
#             break
#         elif operacao.upper() == 'C':
#             resultado = 0.0
#             continue
#         elif operacao == '+':
#             numero1 = float(input('Digite o primeiro numero: '))
#             numero2 = float(input('Digite o segundo numero: '))
#             resultado += numero1 + numero2

#         elif operacao == '*':
#             numero1 = float(input('Digite o primeiro numero: '))
#             numero2 = float(input('Digite o segundo numero: '))
#             resultado += numero1 * numero2

#         elif operacao == '-':
#             numero1 = float(input('Digite o primeiro numero: '))
#             numero2 = float(input('Digite o segundo numero: '))
#             resultado += numero1 - numero2
        
#         elif operacao == '/':
#             numero1 = float(input('Digite o primeiro numero: '))
#             numero2 = float(input('Digite o segundo numero: '))
#             resultado += numero1 - numero2
#         else:
#             print('Digite uma operação válida!')
#             continue
#         print(resultado)
# except:
#     ...

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0.0
    num_2_float = 0.0
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except Exception as error:
        numeros_validos = None
        print(error)

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos!')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue
    
    print('Realizando sua conta! Confira o resultado abaixo: ')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    elif operador == '-':
         print(f'{num_1_float} - {num_2_float} = {num_1_float - num_2_float}')
    elif operador == '*':
         print(f'{num_1_float} * {num_2_float} = {num_1_float * num_2_float}')
    elif operador == '/':
         print(f'{num_1_float} / {num_2_float} = {num_1_float / num_2_float}')
    else:
        ...
    #########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair:
        break
    