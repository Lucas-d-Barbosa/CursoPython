"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = " lucas barbosa "
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC' ERRO
print(string.upper())
print(string.lstrip())
print(outra_variavel.lstrip())