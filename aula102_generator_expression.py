import sys

# Generator expression, Iterables e Itarators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__

lista = [n for n in range(10000)]

generator = (
    i
    for i in range(10000)
)

print(sys.getsizeof(generator))
print(sys.getsizeof(lista))
print(next(generator))
print(next(generator))
print(next(generator))
# print(len(generator)) #erro, não se sabe o tamanho até executar um a um
