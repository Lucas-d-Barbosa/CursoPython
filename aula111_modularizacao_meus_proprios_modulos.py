import aula110_m_modularizacao_meus_proprios_modulos as aula110_m
from aula110_m_modularizacao_meus_proprios_modulos import variavel_modulo, soma

# print('Este módulo se chama', __name__)
print("COM NAMESPACE DO MÓDULO")
print(aula110_m.variavel_modulo)
print(aula110_m.soma(10, 5))

print()

print("SEM NAMESPACE DO MÓDULO")
print(variavel_modulo)
print(soma(10, 5))