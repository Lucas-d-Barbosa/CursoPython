"""
Repetição
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True
nome = ''
while condicao:
    nome = input('Qual o seu nome: ')
    if nome.upper() == 'SAIR':
        break 
    print(f'Seu nome é: {nome}')
    
