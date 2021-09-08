# Imprimir uma lista de números
for x in range (1, 100):
    print(x)

# Descobrir se o número é primo
a = int(input('Entre com um número: '))

div = 0
for x in range (1, a+1):
    resto = a % x
    if resto == 0: 
        # O div sempre tem que concatenar com um a mais, pode ser div += 1
        div = div + 1

if div == 2:
    print('Número {} é primo' . format(a))
else:
    print('Número {} não é primo' . format(a))

Imprimir uma lista de números primos
for num in range (101):
    div = 0
    for x in range (1, num+1):
        resto = num % x
        # print(x, resto)
        if resto == 0: 
            div += 1
    if div == 2:
        print(num)


