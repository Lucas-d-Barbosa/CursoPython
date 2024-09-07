# Try, Except, else e finally

"""
Não silencie um erro! 
"""
try:
    n = int(input())
    # print(n[0])
    divisao = n / 0
except ValueError as e:
    print("Digite um número!", e)
except ZeroDivisionError as e:
    print("Impossível dividir um número por 0!", e)
except (TypeError, IndexError) as e:
    print('ERROR:', e.__class__.__name__)
except Exception:
    print('ERROR DESCONHECIDO!')