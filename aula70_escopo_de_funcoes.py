"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo local e o global.
O escopo global é o escopo onde todo código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
Não temos acesso anomes de escopos internos nos escopos exeternos
A palvra global faz uma variável do escopo externo 
ser a mesma do escopo interno.
"""
x = 1
def escopo():
    # global x # manipular a variável global
    x = 10
    def outra_funcao():
        # global x # manipular a variável global
        x = 11
        y = 3
        print(x, y)
    # print(y) erro

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)