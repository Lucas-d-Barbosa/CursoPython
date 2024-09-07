"""
Introdução às Generator functions em Python
generator = (n for n in range(1000))
"""

def generator(start = 0, stop = 0, stap = 1):
    while True:
        yield start
        start += stap
        if start == stop:
            return
    return print("Acabou")
gen = generator(0,10, 2)

for i in gen:
    print(i)