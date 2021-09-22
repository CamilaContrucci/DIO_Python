# Aula 9, 13m44s

def escrever_arquivo(texto):
    diretorio = 'C:/Users/contr/Documents/VSCode/DIO_Python/Aulas/aula9p2.txt'
    #gerar num diretório específico >tem que usar a barrinha /
    arquivo = open(diretorio, 'w') 
    arquivo.write(texto)
    arquivo.close()

def atualizar_texto(nome_arquivo):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()

if __name__ == '__main__':
    # aluno = 'Rafael, 10, 10, 5, 5'
    atualizar_texto('notas.txt', texto)
    # ler_arquivo('aula9.txt') # deu ruim
    