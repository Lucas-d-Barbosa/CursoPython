import json
CAMINHO_ARQUIVO = 'aula147_classes_salvas.json'
class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("Lucas Barbosa", 22)
p2 = Pessoa("Luiz Fernando", 19)
p3 = Pessoa("João Eduardo", 20)

bd = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO,'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    fazer_dump()