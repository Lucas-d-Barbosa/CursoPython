"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

"""
nome = 'Lucas'
preco = 1000.9580
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (15, 15))