"""
Introdução às funções (def) em Python
Funções são trechos de código usado para replicar
determinada ação ao longo do código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam none (nada).

"""

# def Print(a, b, c):
#     print("Várias1")
#     print("Várias2")
#     print("Várias3")


# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)
# imprimir(7, 8, 9)

def saudacao(nome="Amigo"):
    print(f'Olá, {nome}!')

saudacao('Lucas Barbosa')
saudacao('Luiz Fernando')
saudacao()