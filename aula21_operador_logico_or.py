"""
and (e) or (ou) not (não)
Or - Somente uma condição precisa ser verdadeiras
Se qualquer valor for considerado verdadeiro, 
a expresão inteira seŕa avaliada naquele valor
São considerados falsy (que vc já viu)
0 0.0 '' False
Também existe o tipo None que é
Usado para representar um não valor

"""

# entrada = input("[E]ntrar [S]air: ")
# senha_digitada = input("Senha: ")

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print("Entrar")
# else:
#     print("Sair")

#Avaliação de curto circuito

senha = input('Senha: ') or 'Sem senha'
print(senha)