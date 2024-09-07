"""
https://docs.python.org/3/py-modindex.html


Módulos padrão do Python (import, from, as e *)
inteiro - import nome_modulo
Vantagens: Você tem o namespace do módulo
Desvantagens: nomes grandes


partes - from nome_modulo import objeto1, objeto2
Vantagens: nomes pequenos
Desvantagens: Sem o namespace do módulo


alias 1 - import nome_modulo as apelido
alias 2 - from nome_modulo import  objeto as apelido
Vantagens: você pode reservar nomes para seu código
Desvantagens: pode ficar fora do padrão da linguagem


má prática - from nome_modulo import *
Vantagens: importa tudo de um módulo
Desvantagens: importa tudo de um módulo

"""

# # Import inteiro
# import sys
# platform = 'A minha'

# print(sys.platform)
# print(platform)


# # Import de partes do módulo
# from sys import platform, exit
# print(platform)
# platform = 'A minha' # substitui o import por 'A minha'
# print("Olá")
# exit()

# # Dando um apelido para o módulo
# import sys as sistemas # o módulo sys foi modificado para sistema
# sys = 'alguma coisa'
# print(sistemas.platform)
# print(sys)

# from sys import platform as pt, exit as fechar # renomeando as partes importadas
# print(pt)
# fechar()
# print('asa')

# from sys import * # Importei tudo do módulo e não preciso mais dos 
# print(platform)#...namespace para usar codigo, mas posso sobrescrever sem querer
# exit()
# print('asa')