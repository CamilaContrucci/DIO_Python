a = 10
b = 6
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto) 

#str faz a conversão
print('soma: {}'.format(soma))
print('soma: ' + str(soma))
print('Soma: {} . \nSubtração: {}'.format(soma, subtracao))

print('Soma: {soma}. \nSubtração: {subtracao}.'
    '\nMultiplicação: {multiplicacao}. \nDivisão: {divisao}'
    '\nResto: {resto}'. frmat(soma=soma, subtracao=subtracao, divisao=divisao, multiplicacao=multiplicacao, resto=resto))

#int faz o arredondamento
print(int(divisao))


x = '1'
soma2 = int(x) + 1
print(soma2)

c = int (input('Entre com o primeiro valor: '))
d = int (input('Entre com o segundo valor: '))
soma = c + d
subtracao = c - d
multiplicacao = c * d
divisao = c / d
resto = c % d
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto) 

print('Soma: {soma}. \nSubtração: {subtracao}.'
    '\nMultiplicação: {multiplicacao}. \nDivisão: {divisao}'
    '\nResto: {resto}'. format(soma=soma, subtracao=subtracao, divisao=divisao, multiplicacao=multiplicacao, resto=resto))
