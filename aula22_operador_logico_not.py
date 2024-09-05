"""
Operador lógico "not"
usado para inverter expressões
not True == False
not False == True

"""

senha = input("Senha: ")

if not senha:
    print("Você não digitou a sua senha")

print(not 1)
print(not 0)
print(not True)
print(not False)