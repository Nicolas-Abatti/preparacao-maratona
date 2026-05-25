while True:
    try:
        N = int(input())

        if N == 1:
            print(0)
            continue ##pula todo o restante do programa e volta para o inicio do while
        elif N == 2:
            print(1)
            continue ##pula todo o restante do programa e volta para o inicio do while
        else:
            penultimo = 0
            ultimo = 1

        for i in range(2, N):
            if i % 2 == 0:
                atual = ultimo + penultimo
            else:
                atual = ultimo * penultimo

            penultimo = ultimo
            ultimo = atual

        print(ultimo)

    except EOFError:
        break
