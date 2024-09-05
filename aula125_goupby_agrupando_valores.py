from itertools import groupby
def ordena(aluno):
    return aluno['nota']
alunos = [
    {'nome': 'Lucas', 'nota' : 'A'},
    {'nome': 'Luiz', 'nota' : 'B'},
    {'nome': 'Eduardo', 'nota' : 'C'},
    {'nome': 'Vitor', 'nota' : 'E'},
    {'nome': 'Ronyel', 'nota' : 'F'},
    {'nome': 'Thormes', 'nota' : 'A'},
    {'nome': 'Hans', 'nota' : 'A'},
    {'nome': 'Natanael', 'nota' : 'A'},
]

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)
for chave, aluno in grupos:
    print(chave)
    print(*list(aluno), sep="\n")