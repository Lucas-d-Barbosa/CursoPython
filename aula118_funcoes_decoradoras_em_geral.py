"""
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python...
... Usar as funções decoradoras em outras funções.
Decoradores são "syntax shugar" (Açucar sintático)

"""
def criar_funcao(func):
    def interna(*args, **kwargs):
        print("Vou te decorar!")
        for arg in args:
            is_string(arg)
        
        resultado = func(*args, **kwargs)
        print("Ok! Foi decorada.")
        return resultado
    
    return interna

@criar_funcao
def inverter_string(string):
    return string[::-1]

def is_string(param):
   if not isinstance(param, str):
       raise TypeError("Param, deve ser uma string")


invertida = inverter_string('12')

print(invertida)