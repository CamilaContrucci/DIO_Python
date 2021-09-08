lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
print(lista)

# Imprime a classe
print(type(lista))

# Para acessar o elemento específico, exemplo o gato, tem que começar a contar a partir do 0. Isto é, cachorro = 0, gato = 1, elefante = 2.
print(lista_animal[1])

# Imprimir todos os itens da lista_animal
for x in lista_animal:
    print(x)

# Imprimir a soma de cada item da lista
soma = 0
for x in  lista:
    print(x)
    soma += x
print(soma)

# Imprimir a soma de todos os elementos
print(sum(lista))

# Buscar o maior valor da lista, independente de posição
print(max(lista))
print(max(lista_animal)) #considera ordem alfabética

# Buscar o menor valor da lista, independente de posição
print(min(lista))
print(min(lista_animal)) #considera ordem alfabética

# Descobrir se existe determinado elemento na lista
if 'gato' in lista_animal:
    print('existe gato na lista')
else: 
    print('não existe gato na lista')

if 'lobo' in lista_animal:
    print('existe lobo na lista')
else: 
    print('não existe lobo na lista. Será incluído')
    lista_animal.append('lobo') # append acrescenta o item na lista
    print(lista_animal)

lista_animal.pop() # remove o último elemento da lista
print(lista_animal)

lista_animal.pop(0) # remove o elemento 0 da lista
print(lista_animal)

lista_animal.remove('elefante')
print(lista_animal)


# Multiplicar lista
nova_lista_animal = lista_animal * 3
print(nova_lista_animal)

print