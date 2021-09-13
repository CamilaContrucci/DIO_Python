conjunto = {1, 2, 3, 4}
print(type(conjunto)) # imprime a definição da classe (set = conjunto)
conjunto.add(5) # adiciona um elemento
print(conjunto)
conjunto.discard(2) # remove um elemento
print(conjunto)

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}
conjunto_uniao = conjunto1.union(conjunto2)
print('União: {}' . format(conjunto_uniao))

conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Intersecção: {}' . format(conjunto_interseccao))

conjunto_diferenca = conjunto1.difference(conjunto2)
print('Diferença entre 1 e 2: {}' . format(conjunto_diferenca))

conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('Diferença entre 2 e 1: {}' . format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simétrica:{}' . format(conjunto_diff_simetrica))

# Vê se um conjunto é um conjunto é subconjunto / superconjunto de outro.
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_subset = conjunto_a.issubset(conjunto_b) 
print('A é subconjunto de B: {}' .format(conjunto_subset)) # A pertence a B (todos elementos de A também estão em B)

conjunto_subset = conjunto_b.issubset(conjunto_a)
print('B é subconjunto de A: {}' .format(conjunto_subset)) # B não pertence a A (tem mais elementos que A)

conjunto_subset = conjunto_a.issuperset(conjunto_b)
print('A é superconjunto de B: {}' .format(conjunto_subset)) # A não contém B 

conjunto_subset = conjunto_b.issuperset(conjunto_a)
print('B é superconjunto de B: {}' .format(conjunto_subset)) # B contém A

# Converter lista - conjunto; conjunto - lista. 
lista = {'cachorro', 'cachorro', 'gato', 'gato', 'elefante'}
print(lista)
conjunto_animais = set(lista) # converter lista para conjunto, tira a duplicidade da lista
print(conjunto_animais)

lista_animais = list(conjunto_animais) # converte  conjunto para lista
print(lista_animais)