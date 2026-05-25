while True:
    try:
        expressao = input()
        
        contador = 0
        correto = True

        for c in expressao:
            if c == '(':
                contador += 1
            elif c == ')':
                contador -= 1

                if contador < 0:
                    correto = False
                    break

        if contador != 0:
            correto = False

        print('correct' if correto else 'incorrect')

    except EOFError:
        break