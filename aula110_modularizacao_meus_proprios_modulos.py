"""
Entendendo os seus próprios módulos Python
O primeiro módulo executado chama-se __main__
Você pode importar outro módulo inteiro ou partes dele
O python conhece a pasta onde o __main__ está e abaixo dele
Ele não reconhece pastas e módulos acima do __main__ por padrão
O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path



"""
import sys
sys.path.append('/home/lucas/Documentos/TestePython')
print(*sys.path, sep="\n")
print('\n\n')
import aula110_m_modularizacao_meus_proprios_modulos as aula_110
# import teste as t # type: ignore

print('Este módulo se chama:', __name__)