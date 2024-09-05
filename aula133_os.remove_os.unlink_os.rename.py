"""
Criando arquivos com Python
Usamos a função "open" para abrir um arquivo em Python
(Ele pode ou não existir)

Modos:
r (leitura), w(escrita), x (para criação)
a (escreve ao final), b (binário)
t (modo texto), + (leitura e escrita)
Context manager - with (abre e fecha)
Métodos úteis
write, read (escrever e ler)
writelines(escrever várias linhas)
seek (move o cursor)
readline(ler linha)
readlines(Ler linhas)
Vamos falar mais sobre o módulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo
Vamos falar mais sobre o módulo json, mas:
json.dump = Gera um arquivo json
json.load


"""
from os import unlink, remove,rename

caminho_arquivo = '/home/lucas/Documentos/CursoPython/arquivos_extras/'
caminho_arquivo += 'aula133.txt'

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    arquivo.write('Escrevendo no arquivo 1!\n')
    arquivo.write('Escrevendo no arquivo 2!\n')
    arquivo.write('Escrevendo no arquivo 3!\n')
    arquivo.seek(0,0)
    print(caminho_arquivo + '\n')
    print(arquivo.read())

# unlink(caminho_arquivo) # Apaga o arquivo
# remove(caminho_arquivo) # Faz a mesma coisa

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    arquivo.write('Escrevendo no arquivo novo 1!\n')
    arquivo.write('Escrevendo no arquivo novo 2!\n')
    arquivo.write('Escrevendo no arquivo novo 3!\n')
    arquivo.seek(0,0)
    print(caminho_arquivo + '\n')
    print(arquivo.read())

rename(caminho_arquivo, 'aula133-2.txt')
