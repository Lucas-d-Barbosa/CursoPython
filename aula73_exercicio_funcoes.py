def multiplica_valores(*args):
    total = 1
    for i in args:
        total *= i
    return total
def par_ou_impar(num):
    if num % 2 == 0:
        return f'O número {num} é par!'
    return f'O número {num} é impar!'

valores_multiplicados = multiplica_valores(2, 6, 3)
resultado_par_impar = par_ou_impar(4)

print(valores_multiplicados)
print(resultado_par_impar)