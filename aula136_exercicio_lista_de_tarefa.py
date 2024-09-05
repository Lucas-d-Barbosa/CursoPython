import os

lista_de_tarefas = []
tarefas_desfeitas = []

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar!')
        return
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    
def desfazer(tarefas, terefas_desfazer):
    if not tarefas:
        print('Nada a desfazer!')
        return
    terefas_desfazer.append(tarefas.pop())
    print('TAREFAS:')
    print(*tarefas, sep="\n")

def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print('Nenhuma tarefa a refazer!') 
        return
    tarefas.append(tarefas_refazer.pop())
    print('TAREFAS:')
    print(*lista_de_tarefas, sep="\n")

while True:
    print()
    print('Comandos: listar, desfazer, refazer')
    tarefa_ou_comando = input('Digite uma tarefa ou comando: ')
    print()
    if tarefa_ou_comando.lower() == 'listar':
        listar(lista_de_tarefas)
    elif tarefa_ou_comando.lower() == 'desfazer':
        desfazer(lista_de_tarefas, tarefas_desfeitas)
    elif tarefa_ou_comando.lower() == 'refazer':
        refazer(lista_de_tarefas, tarefas_desfeitas)
    elif tarefa_ou_comando.lower() == '\quit':
        break
    elif tarefa_ou_comando.lower() == '\clear':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        lista_de_tarefas.append(tarefa_ou_comando)
        print('TAREFAS:')
        print(*lista_de_tarefas, sep="\n")


