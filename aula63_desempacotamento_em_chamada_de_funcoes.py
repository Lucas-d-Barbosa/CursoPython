"""
Desempacotamento em chamada
...de funções.
"""

string = 'ABC'
lista = ['Maria', 'Helena',1, 2, 3, 'Eduarda' ]
tupla = 'Python', 'é', 'legal'

# p, s,*_ , u  = lista
# print(p, u)

# print('Maria', 'Helena',1, 2, 3, 'Eduarda' )
# print(*lista)
# print(*string)
# print(*tupla)


salas = [
    #  0         1
    ['Maria', 'Helena'], # 0
    #  0
    ['Luísa'], # 1
    
    #   0       1        2
    ['Lucas', 'Luiz', 'Eduardo'] #2

]

print(*salas, sep="\n")