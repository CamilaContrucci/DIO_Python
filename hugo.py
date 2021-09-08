

soma = 2 + 2
soma_2 = 3 + 3

# Diferentes formas de imprimir a soma
print('a soma eh: ', soma)

print('soma:'+str(soma))

print('soma: {}, soma2: {} '.format(soma, soma_2))

print('soma_2: {soma_2_nesse}, soma_1: {soma_1_aqui}'.format(soma_2_nesse=soma_2, soma_1_aqui=soma))

print(f'soma: {soma}, soma2: {soma_2}')


def f(x):
    return x + 2
    

f(10)
f(1)

# Exemplo de uso da função se
media = 7
nota_de_corte = 5

if media > nota_de_corte:
    print('aluno aprovado')
else:
    print('aluno reprovado')

# Imprimir a soma de elementos de um conjunto
lista = [1, 2, 3, 4, 5, 6]

soma = 0

print('soma utilizando o sum:', sum(lista))

for item in lista:
    print(soma)
    soma = soma + item

print('soma por iteracao:', soma)

# Importar csv e imprimir
import csv

with open('./app_Python/hugo.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
