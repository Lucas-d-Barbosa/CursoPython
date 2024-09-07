perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções' : ['1', '2', '4', '5'],
        'Resposta' : '4'
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções' : ['25', '55', '10', '51'],
        'Resposta' : '25'
    },

    {
        'Pergunta': 'Quanto é 10 / 5?',
        'Opções' : ['4', '5', '2', '1'],
        'Resposta' : '2'
    },
]

quantidade_acertos = 0

for dict in perguntas:
    print(f'Pergunta:', dict['Pergunta'])

    print('Opções:')
    cont = 0 
    
    for indice, opcao in enumerate(dict.get('Opções')):
        print(f'{indice + 1}) {opcao}')
    
    resposta = int(input('Escolha uma opção: ')) - 1
    
    if dict['Resposta'] == dict['Opções'][resposta]:
        print('Você acertou!')
        print()
        quantidade_acertos += 1
    
    else:
        print('Você errou!')
        print()

print(f'Você acertou {quantidade_acertos} de {len(perguntas)} questões.')