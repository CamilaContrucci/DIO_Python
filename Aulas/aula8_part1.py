# Módulo são os arquivos .py
# Para importar um módulo tem que entrar terminal ( ctrl + '), navegar na pasta ( cd nomedapasta ) ou (cd ../  para voltar uma pasta), digitar python, import nomedoarquivo.

from aula7_part2 import Televisao
from aula7_part1 import Calculadora
from aula8_part2 import contador_letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('total de letras por palavra da lista: {}' .format(total_letras))