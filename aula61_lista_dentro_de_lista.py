"""
Lista de listas e seus índices
"""

salas = [
    #  0         1
    ['Maria', 'Helena'], # 0
    #  0
    ['Luísa'], # 1
    
    #   0       1        2
    ['Lucas', 'Luiz', 'Eduardo'] #2

]

# print(salas[0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    for item in sala:
        print(item, end="  ")
    print()