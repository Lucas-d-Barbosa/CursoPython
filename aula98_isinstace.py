# isinstace - para saber se o objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], 
    (1, 2), {0, 1}, {'nome' : 'Lucas'}
]


for item in lista:
    if isinstance(item, set):
        print("SET")
        item.add(5)
        print(item)

    elif isinstance(item, str):
        print("STR")
        print(item.upper())

    elif isinstance(item, (float, int)):
        print("NUM")
        print(item)
        
    else:
        print('OUTRO')
        print(item)