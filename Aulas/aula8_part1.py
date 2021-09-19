# Módulo são os arquivos .py
# Para importar um módulo tem que entrar terminal ( ctrl + '), navegar na pasta ( cd nomedapasta ) ou (cd ../  para voltar uma pasta), digitar python, import nomedoarquivo.

from aula7_part2 import Televisao
televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)