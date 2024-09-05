"""
Não existem constantes no python, mas...
... Por convenção, variáveis com letras totalmente...
... Maiúsculas são consideradas constantes
CONSTANTES = "Variáveis" que não vão mudar
Muitas condições if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61 # valocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega 


vel_carro_pass_radar_1 = velocidade > RADAR_1;
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = vel_carro_pass_radar_1 and carro_passou_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade do carro passou do radar 1!') 
    
if carro_passou_radar_1:
    print("O carro passou no radar 1!")

if carro_multado_radar_1:
    print("O carro será multado no radar 1.")