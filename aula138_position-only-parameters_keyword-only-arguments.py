"""
Controlando a quantidade de argumentos posicionais e nomeados em funções
*args (ilimitado de argumetnos posicionais)
**kwargs (ilimitado de argumetnos nomeados)
Position-only Parameters (/) - Tudo antes da barra deve ser APENAS posicional.
PEP 570 - Python positional only parameters
https://peps.python.org/pep-0570/

Keyword-only arguments (*) - sozinho NÃO SUGA valores.
PEP 3102 - Keyword only arguments 
https://peps.python.org/pep-3102/

"""

def soma(a, b, /,*, c, **kwargs):
    print(kwargs)
    print(a + b)


soma(1, 2, c=3, nome='Teste', idade=21)
