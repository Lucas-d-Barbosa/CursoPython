# Exemplo de uso de sets
letras_digitadas = set()
letras_acertadas = set()
palavra_secreta = set("Pão")
while True:
    letra = input('Digite: ')

    letras_digitadas.add(letra)
    letras_acertadas = letras_digitadas & palavra_secreta
    for i in letras_acertadas:
        print(i)

    if letras_acertadas == palavra_secreta:
        break
    
print(letras_acertadas)