import json
from aula147_exercicio_salve_classe_em_json_arquivo1 import Pessoa, CAMINHO_ARQUIVO, fazer_dump

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados_classes = json.load(arquivo)

pessoas = []
for classe in dados_classes:
    pessoas.append(Pessoa(**classe))

for pessoa in pessoas:
    print(pessoa.nome, pessoa.idade, sep=' - ')
