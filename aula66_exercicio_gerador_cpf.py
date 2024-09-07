import random
import re
import sys

cpf = f'{random.randint(100000000, 999999999)}'
entrada_e_sequencial =  cpf == cpf[0] * len(cpf)
if entrada_e_sequencial:
    print('...')
    sys.exit()

novo_cpf = cpf
cont_1 = 10
cont_2 = 11

resultado = 0
for i in novo_cpf:
    if cont_1 < 2:
        break
    resultado += int(i) * cont_1
    cont_1 -= 1
resultado *= 10
primeiro_digito = resultado % 11 if (resultado % 11) <= 9 else 0
resultado = 0

for i in novo_cpf:
    if cont_2 < 3:
        break
    resultado += int(i) * cont_2
    cont_2 -= 1
resultado += primeiro_digito * 2
resultado *= 10
cont = 1
segundo_digito = resultado % 11 if (resultado % 11) <= 9 else 0
novo_cpf = f'{cpf}{primeiro_digito}{segundo_digito}'
print(novo_cpf)