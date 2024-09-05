# if / elif  ----/ else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if(entrada.lower() == "entrar"):
    print("Bem-vindo(a)!")
elif(entrada.lower() == "sair"):
    print("Tenha um ótimo dia!")
else:
    print("Sinto muito, não consigo compreender!")

print("Fora dos blocos!")