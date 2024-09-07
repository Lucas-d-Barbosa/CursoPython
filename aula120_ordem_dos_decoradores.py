def parametros_decorador(nome = "Lucas"):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):

            resultado = func(*args, **kwargs)
            final = f'{resultado} {nome}'
            return final
        
        return sua_nova_funcao
    
    return decorador

@parametros_decorador("5")
@parametros_decorador("4")
@parametros_decorador("3")
@parametros_decorador("2")
@parametros_decorador("1")
def soma(x, y):
    return x + y

somando = soma(10, 5)
print(somando)