import os
import json

caminho = 'aula137_aula138_lista_de_tarefas.json'

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

def adicionar(tarefa, tarefas):
    tarefas.append(tarefa)
    print('TAREFAS:')
    print(*lista_de_tarefas, sep="\n")

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='UTF-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError as e:
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w+', encoding="UTF-8") as arquivo: 
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)

CAMINHO_ARQUIVO = 'aula137_aula138_lista_de_tarefas.json'
lista_de_tarefas = ler([],CAMINHO_ARQUIVO)
tarefas_desfeitas = []

while True:
    print()
    print('Comandos: listar, desfazer, refazer')
    tarefa_ou_comando = input('Digite uma tarefa ou comando: ')
    print()
    if tarefa_ou_comando.lower() == '\quit':
        break
    comandos = {
        'listar' : lambda: listar(lista_de_tarefas),
        'desfazer' : lambda: desfazer(lista_de_tarefas, tarefas_desfeitas),
        'refazer' : lambda: refazer(lista_de_tarefas, tarefas_desfeitas),
        '\clear' : lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa_ou_comando, lista_de_tarefas)
    }

    comando = comandos.get(tarefa_ou_comando) if comandos.get(tarefa_ou_comando) is not None else \
        comandos['adicionar']
    comando()
    salvar(lista_de_tarefas, CAMINHO_ARQUIVO)


    # if tarefa_ou_comando.lower() == 'listar':
    #     listar(lista_de_tarefas)
    # elif tarefa_ou_comando.lower() == 'desfazer':
    #     desfazer(lista_de_tarefas, tarefas_desfeitas)
    # elif tarefa_ou_comando.lower() == 'refazer':
    #     refazer(lista_de_tarefas, tarefas_desfeitas)
    # elif tarefa_ou_comando.lower() == '\quit':
    #     break
    # elif tarefa_ou_comando.lower() == '\clear':
    #     os.system('cls' if os.name == 'nt' else 'clear')
    #     continue
    # else:
    #     lista_de_tarefas.append(tarefa_ou_comando)
    #     print('TAREFAS:')
    #     print(*lista_de_tarefas, sep="\n")


