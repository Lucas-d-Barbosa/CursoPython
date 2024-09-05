"""
Encapsulamento (modificadores de acesso: public, protected, private)
Python NÃO TEM modificadores de acesso
Mas podemos seguir as seguintes conveções
    (sem underline) = public
        pode ser usado em qualquer lugar
    (um underline) = protected
        não DEVE ser usado fora da classe
        só na própria classe e suas subclasses.
    (dois underlines)
        "name mangling" (desfiguração de nomes) em Python
        _NomeClasse__nome_attr_ou_method
        só deve ser usado na classe em que foi 
        declarado.

"""

class Foo:
    def __init__(self) -> None:
        self.public = "Isso é público"
        self._protected = "Isso é protected"
        self.__private = "Isso é private"
        
    def metodo_publico(self):
        return self.public
    
    def metodo_protected(self):
        return self._protected 
    
    def metodo_private(self):
        return self.__private

f = Foo()
print(f.public)
# print(f._protected) Funciona mas não use pois vai contra a convenção
# print(f.__private) Isso está de acordo com as outras linguagens e da erro
print(f._Foo__private) # Desa forma consigo acessar o atributo private (o nome dele se modifica fora da classe)
print(f.metodo_publico())
print(f.metodo_protected())
print(f.metodo_private())