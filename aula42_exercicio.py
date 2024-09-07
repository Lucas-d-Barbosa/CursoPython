def removerCaracter(string, char):
    i = 0
    novaString = ''
    while i < len(string):
        if(string[i] == char):
            i += 1
            continue
        else:
            novaString += string[i]
            i += 1

    return novaString


frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'
frase = removerCaracter(frase, ' ')

i = 0
max = 0
letra_max = ''
while i < len(frase):
    letra_atual =  frase[i].lower()
    max = frase.count(letra_atual) if (frase.count(letra_atual) > max) else max
    letra_max = letra_atual  if (frase.count(letra_atual) >= max) else letra_max
   
    i += 1
print(f'A letra que mais apareceu foi: {letra_max}! '
      f'Ela apareceu {max} vezes.')


    

