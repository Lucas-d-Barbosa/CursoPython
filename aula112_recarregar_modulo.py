import importlib

import aula112_m_recarregar_modulo

print(aula112_m_recarregar_modulo.variavel)

for i in range(10):
    importlib.reload(aula112_m_recarregar_modulo)
    print(i)

print("FIM")