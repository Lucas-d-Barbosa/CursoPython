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
s1 = {1, 2, 3}
print(s1)
print(4  in s1)

for numero in s1:
    print(numero)