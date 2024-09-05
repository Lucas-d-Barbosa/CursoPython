"""
Introdução ao try/except (try/catch)
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input(
    'Vou dobrar o número que você digitar: '
    )

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_float} é {numero_float * 2}')
# else:
#     ...

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except(ValueError):
    print(f"{ValueError.__name__}: This not a number!")
