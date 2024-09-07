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


caminho_arquivo = '/home/lucas/Documentos/CursoPython/arquivos_extras/'
caminho_arquivo += 'aula132.txt'
print(caminho_arquivo)

# with open(caminho_arquivo, 'w+') as arquivo:
#     print(type(arquivo))
#     print()
#     arquivo.write('Linha 1!\n')
#     arquivo.write('Linha 2!\n')
#     arquivo.write('Linha 3!\n')
#     arquivo.writelines(('Linha 4!\n', 'Linha 5!\n')) # passa uma tupla
#     arquivo.seek(0,0) # Move o cursos para posição 0, 0 (início do arquivo)
#     print(arquivo.read())
#     print('Lendo: ')
#     arquivo.seek(0, 0)
#     print(arquivo.readline().strip()) # Lê apenas linha por linha
#     print(arquivo.readline().strip()) # Lê apenas linha por linha
#     print()
#     print("READLINES")
#     arquivo.seek(0,0)
#     for linha in arquivo.readlines():
#         print(linha.strip())

# print()
# print('#' * 10 + "\n") 

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())
#     print("Fim do arquivo")


# with open(caminho_arquivo, 'a+') as arquivo:
#     arquivo.write('Linha adicionada ao final!\n')
#     for linha in arquivo.readlines():
#         print(linha)

# with open(caminho_arquivo, 'r+') as arquivo:
#     print(arquivo.read())


with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    arquivo.write('Linha 1!\n')
    arquivo.write('Linha 2!\n')
    arquivo.write('Linha 3!\n')
    arquivo.write('Atenção!\n')

# o W abre o arquivo, apaga tudo que há nele e escreve tudo de novo.
# o A abre o arquivo e escreve ao final do arquivo sem apagar o que já tem.