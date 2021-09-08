# Exercício para identificar o maior valor
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Condicional (if, else) e operador (and)
if a > b and a > c:
    print('O maior número é: {}' . format(a))
elif b > a and b > c:
    print('O maior número é: {}' . format (b))
else:
    print('O maior número é: {}' . format (c))

# Exercício para identificar se o número é par
a = int(input('Entre com um valor: '))
resto = a % 2
if resto == 0:
    print('número é par')
else:
    print ('número é ímpar')

# Para saber se um número par foi digitado
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or resto_b == 0:
    print('foi digitado um número par')
else:
    print ('nenhum número par foi digitado')
    
# Também pode usar or not para frase falsa
