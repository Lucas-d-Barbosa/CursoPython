"""
Crie uma função que encontra o primeiro duplicado considerando 
 o segundo número como a duplicação. Retorne a duplicação considerada.

Requisito:
    A ordem do número duplicado é considerada a partir da ocorrência
    da segunda ocorrência do número, ou seja, o número duplicado em si.

    Exemplo:
    [1, 2, 3, 3, 2, 1] -> 1, 2,e 3 são duplicados (retorne o 3)
    [1, 2, 3, 4, 5, 6] - Retorne -1 (Não tem duplicados)
    se não encontrar duplicados na lista retorne -1

"""

def retornar_duplicados(lista):
    list_inteiros_duplicados = []

    for i in lista:

        tamanho_lista = len(list_inteiros_duplicados)
        numeros_duplicados = set()

        for j in i:
            teste = set((j,))
            if numeros_duplicados.intersection(teste):
                list_inteiros_duplicados.append(j)
                break
            
            numeros_duplicados.add(j)
        if tamanho_lista == len(list_inteiros_duplicados):
            list_inteiros_duplicados.append(-1)
    return list_inteiros_duplicados    


lista_de_lista_de_inteiros = \
    [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
        [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
        [1, 4, 9, 8, 9, 4, 8],
        [1, 2, 3, 3, 2, 1],
        [1, 2, 3, 4, 5, 6]
    ]

print(retornar_duplicados(lista_de_lista_de_inteiros))
