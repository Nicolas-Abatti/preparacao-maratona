N = int(input())

album = []

for figurinhas in range (0, N):
    fig = int(input())

    album.append(fig)

novo_album = list(set(album))

repetidas =  len(album) - len(novo_album)
unicas = len(novo_album)
    
print(unicas)
print(repetidas)
