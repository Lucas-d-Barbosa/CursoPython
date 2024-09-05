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

união (|) união (union) - Une

intersecção (&) (intersection) - Itens presentes em ambos

diferença (-) Itens presentes apenas no set da esquerda

diferença simétrica (^) - Itens que não estão em ambos os conjuntos

"""
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # Junta todos e tira repetidos
s3 = s1 & s2 # Pega aqueles que estão em ambos os sets
s3 = s1 - s2 # Retorna o que está presente apenas no da esquerda (1) 
s3 = s2 - s1 # Retorna o que está presente apenas no da esquerda (4) 
s3 = s1 ^ s2 # Retorna aqueles itens que não são comuns aos dois sets (1 e 4)
print(s3)
