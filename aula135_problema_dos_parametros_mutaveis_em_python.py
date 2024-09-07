def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Lucas')
adiciona_clientes('Claudiane', cliente1)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Viviane')
adiciona_clientes('Gabriel', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)