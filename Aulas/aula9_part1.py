# Criar, copiar, mover, escrever e ler informações de arquivos externos
# \n = pula linha

# arquivo = open('teste.txt', 'w')
# arquivo.write('Meu primeiro arquivo')
# arquivo.close()

diretorio = 'C:/Users/contr/Documents/VSCode/DIO_Python/Aulas/'

def escrever_arquivo(texto):
    diretorio = 'C:/Users/contr/Documents/VSCode/DIO_Python/Aulas/'
    #gerar num diretório específico >tem que usar a barrinha /
    arquivo = open(diretorio, 'w') 
    arquivo.write(texto)
    arquivo.close()

def atualizar_texto(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    # escrever_arquivo('Primeira linha.\n')
    # atualizar_texto('Terceira linha \n')
    ler_arquivo('teste.txt') # para ler em outro diretório, tem que usar a navegação de pastas no terminal como se fosse pelo cmd
    