import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/Users/contr/Documents/VSCode/DIO_Python/Aulas/aula9p2.txt'
    #gerar num diretório específico >tem que usar a barrinha /
    arquivo = open(diretorio, 'w') 
    arquivo.write(texto)
    arquivo.close()

def atualizar_texto(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') #'corta' o texto formando uma lista
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4 #lambda retorna a lista para inteiros, o sum / 4 é o cálculo da média
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
        # print(sum(lista_notas))

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'C:/Users/contr/Documents/VSCode/DIO_Python/Aulas/notas_aluno.txt') #se não colocar nome, ele copia com o mesmo, mas pode dar o nome esccrevendo tbm

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/contr/Documents/VSCode/DIO_Python/')


if __name__ == '__main__':
    move_arquivo('Aula9.txt')
    # copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # aluno = '\nDaiana, 7, 9, 8, 8f'
#     atualizar_texto('notas.txt', aluno)__name__ == '__main__':
    # ler_arquivo('aula9.txt')
    