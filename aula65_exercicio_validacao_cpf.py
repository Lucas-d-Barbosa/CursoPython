"""
CPF: 746.824.890-70
Coleta a soma dos 9 primeiros digitos do cpf
multiplicando cada um dos valores 
por uma contagem regressiva começando por 10

Ex.: 746.824.890-70 (74682489070)
10 9 8 7 6 5 4 3 2 
7  4 6 8 2 4 8 9 0

Somar todos os resultado:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão por 11
3010 % 11 = 7
Se for maior que 10 == 0



"""
import re
import sys

cpf = input('Digite seu CPF Ex.(XXX.XXX.XXX-XX): ')
cpf = re.sub(
    r'[^0-9]',
    '',
    cpf
)

entrada_e_sequencial =  cpf == cpf[0] * len(cpf)
if(entrada_e_sequencial):
    print('CPF inválido!')
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

segundo_digito = resultado % 11 if (resultado % 11) <= 9 else 0
digitos_confirmacao = f'{primeiro_digito}{segundo_digito}'
if(digitos_confirmacao == novo_cpf[len(novo_cpf)- 2:]):
    print('CPF válido!')
    print(digitos_confirmacao)
else:
    print('CPF inválido!')