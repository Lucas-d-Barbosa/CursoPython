"""
Formatação básica de Strings
s - string
d e i - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(Quantidade)
> - Esquerda
< - Direita
^ - Centro

Sinal -> + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a

"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:$^10}')
print(f'{1999.4848:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')

