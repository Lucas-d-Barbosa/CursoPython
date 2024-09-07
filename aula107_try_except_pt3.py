
try:
    print("ABRIR ARQUIVO")
    # 8/0
    # import a
except ZeroDivisionError:
    print("DIVISÃO POR ZERO")
except IndexError:
    print("INDEX FORA DO RANGE")
except (NameError, ImportError) as e:
    print(e)
else:
    print('NÃO DEU ERRO')
finally:
    print("FECHAR ARQUIVO")
