import os
try:
    lista = []
    while(True):
        print('O que quer fazer?')
        operacao = input('[I]nserir [A]pagar [L]istar: ')
        os.system('clear')
        if operacao.upper()[0] == 'I':
            item = input('Insira: ')
            lista.append(item)
        if operacao.upper()[0] == 'L':
            print('Lista:')
            for indice, item in enumerate(lista):
                print(f'{indice} - {item}')
            print()
        if operacao.upper()[0] == 'A':
            if len(lista) > 0:
                print('Qual item deseja remover da lista?')
                item_a_remover = input('Digite o índice: ')
                is_num = item_a_remover.isdigit()
                if not is_num:
                    print('Digite um valor númerico!')
                    continue
                if(len(lista) - 1 < int(item_a_remover)) or (int(item_a_remover) < 0):
                    print('Digite um índice válido!')
                    continue
                lista.pop(int(item_a_remover))
            else:
                print('Você finalizou sua lista!')
                break
except __name__:
    print('Exceção:', __name__ )