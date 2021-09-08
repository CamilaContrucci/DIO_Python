# # Fazer a média do bimestre
# a = int(input('Primeiro bimestre: '))
# b = int(input('Segundo bimestre: '))
# c = int(input('Terceiro bimestre: '))
# d = int(input('Quarto bimestre: '))
# media = (a + b + c + d) / 4

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}' . format(media))
# else:
#     print('foi informado alguma nota errada')

# # Modo especificando o bimestre com a nota errada
# a = int(input('Primeiro bimestre: '))
# if a > 10:
#     a = int(input('Você digitou errado. Primeiro bimestre: '))

# b = int(input('Segundo bimestre: '))
# if b > 10:
#     b = int(input('Você digitou errado. Segundo bimestre: '))

# c = int(input('Terceiro bimestre: '))
# if a > 10:
#     c = int(input('Você digitou errado. Terceiro bimestre: '))

# d = int(input('Quarto bimestre: '))
# if a > 10:
#     d = int(input('Você digitou errado. Quarto bimestre: '))

# media = (a + b + c + d) / 4
# print('Média: {}'. format(media))

# # Pessoa fica digitando forever até a nota ser menor que 10
# nota = int(input('Entre com um valor: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com o valor correto: '))

# Especificar a nota errada e corrigir usando while
a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))

b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))

c = int(input('Terceiro bimestre: '))
while a > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))

d = int(input('Quarto bimestre: '))
while a > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))

media = (a + b + c + d) / 4
print('Média: {}'. format(media))