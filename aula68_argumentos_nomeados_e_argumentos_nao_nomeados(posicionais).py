"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados recebe apenas o argumentos (valor)
"""

# Definição
def soma(x, y, z):
    print(f'{x = } y = {y} z = {z}| ', 'x + y + z =', x + y + z)

soma(1, 2, 1)
soma(1, y = 2, z = 5)
soma(y = 2, x = 1,z = 1)
