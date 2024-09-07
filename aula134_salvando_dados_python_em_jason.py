# from dados import pessoa
import json

# with open('/home/lucas/Documentos/CursoPython/arquivos_extras/aula134.json', 'w+', encoding='utf-8') as arquivo:
#     json.dump(
#         pessoa, 
#         arquivo, 
#         ensure_ascii=False, 
#         indent=True)
#     arquivo.seek(0,0)

with open('/home/lucas/Documentos/CursoPython/arquivos_extras/aula134.json', 'r+', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])