"""
Mantendo estado dentro da classe
"""

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):
        if self.filmando == True:
            print(f'{self.nome} já está filmando!')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = True
    
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar enquanto está filmando!')
            return
        print(f'{self.nome} está fotografando...')

    def parar_de_filmar(self):
        if not self.filmando:
            print(f'{self.nome} está desligada!')
            return
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c2.parar_de_filmar()
c1.parar_de_filmar()
c1.fotografar()
# print(c1.filmando)
# print(c2.filmando)