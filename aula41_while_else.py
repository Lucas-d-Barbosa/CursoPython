"""while/else"""

string = 'Valor qualquer'

i = 0


while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else:
    print('O else foi executado!')

print('Fora do while!')

"""
O else do while é executado após o final do laço while
Entretanto, se um break for executado para sair do laço
o else não é executado

"""