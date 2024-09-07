# Yield from

def gen1():
    print('COMEÇOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')
def gen2(gen=None):
    print('COMEÇOU GEN2')
    if gen is not None:
        yield from gen()
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


gen = gen2(gen1)

for numero in gen:
    print(numero)