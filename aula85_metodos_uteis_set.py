"""
Sets - COnjuntos em Python (Tipo set)
Conjuntos são ensinados na matemática
representados graficamente pelo diagrama de Venn
Sets em python são mutáveis, porém aceitam apenas tipos imutáveis
como valor interno.

Criando um set 
set(iterável) ou {1, 2, 3}


Set são eficientes para remover valores duplicados
de iteváveis.

-- Eles não tem índexes;
-- Eles não garantem ordem;
-- Eles são iteráveis (For, in, not in)

# métodos úteis:
add, update, clear, discard


#Operadores úteis:

união | união (union) - Une

intersecção & (intersection) - Itens presentes em ambos

diferença - Itens presentes apenas no set da esquerda

diferença simétrica - Itens que não estão em ambos os conjuntos

"""


# l1 = [1, 2, 3, 3, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)

# l2 = list(s1)
# s1 = {1, 2, 3, 3, 3, 3, 3, 1} # Valores duplicados são eliminados 
# s1 = {1, 2, 3, {1, 2, 3}}  Erro pois estou passando um valor mutável
# s1 = {1, 2, 3, (1, 2, 3)} aceito pois tupla é imutável

s1 = set()
s1.add("Lucas")
s1.add(1)
# s1.add(1, 2) Isso da erro
# s1.update("Olá, mundo") Vai ser passado como iterável
s1.update(("Olá, mundo",)) #Aqui manda como se fosse uma tupla para pegar o elemento de forma única
# s1.clear() Limpa o set
print(s1)
s1.discard('Olá, mundo') # Descarta um valor, já que cada valor é único
print(s1)