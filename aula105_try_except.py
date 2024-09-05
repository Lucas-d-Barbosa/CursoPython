# Try, Except, else e finally

"""
Não silencie um erro! 
"""
try:
    n = int(input())
    divisao = n / 0
except ValueError as e:
    print("Digite um número!", e)
except ZeroDivisionError as e:
    print("Impossível dividir um número por 0!", e)
except TypeError:
    print('TypeError!')
except Exception:
    print('ERROR DESCONHECIDO!')