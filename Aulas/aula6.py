# conjunto = {1, 2, 3, 4}
# print(type(conjunto)) # imprime a definição da classe (set = conjunto)
# conjunto.add(5) # adiciona um elemento
# print(conjunto)
# conjunto.discard(2) # remove um elemento
# print(conjunto)

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
