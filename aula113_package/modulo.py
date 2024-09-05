from sys import path

# __all__ = [
#     'variavel',
#     'soma_do_modulo'
# ]
if(__name__ != '__main__'):
    from aula113_package.modulo_b import fala_oi
else:
    from modulo_b import fala_oi
variavel = "Alguma coisa"

def soma_do_modulo(x, y):
    return x + y


nova_variavel = 'OK'
fala_oi()