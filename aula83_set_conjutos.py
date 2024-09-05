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


"""


# s1 = set() # Vazio use esse se não vira um dict
s1 = {'Lucas', 'Luiz', 'Eduardo'} # com dados
print(s1, type(s1))