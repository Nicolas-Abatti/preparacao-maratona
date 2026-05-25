class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inserir(no, valor):
    if valor < no.valor:
        if no.esquerda is None:
            no.esquerda = Node(valor)
        else:
            inserir(no.esquerda, valor)   
    elif valor > no.valor:
        if no.direita is None:
            no.direita = Node(valor)
        else:
            inserir(no.direita, valor)

def pre_ordem(no, prordem):
    if no is None:
        return

    prordem.append(no.valor)
    pre_ordem(no.esquerda, prordem)
    pre_ordem(no.direita, prordem)

def pos_ordem(no, posordem):
    if no is None:
        return
    else:
        pos_ordem(no.esquerda, posordem)
        pos_ordem(no.direita, posordem)
        posordem.append(no.valor)
    
def em_ordem(no, emordem):
    if no is None:
        return
    else:
        em_ordem(no.esquerda, emordem)
        emordem.append(no.valor)
        em_ordem(no.direita, emordem)
    
if __name__ == "__main__":

    C = int(input()) 
    
    for tests in range (1, C + 1):

        prordem = []
        emordem = []
        posordem = []

        N = int(input())
        ''' Esse N = int(input()) é inútil
        Originalmente o problema pede que a quantidade de números contida na árvore seja inserida 
        Porém, com este método ele sabe a hora de parar sem precisar usar essa variável N'''
    
        numeros = list(map(int, input().split()))

        raiz = Node(numeros[0])

        for numero in numeros[1:]:
            inserir(raiz, numero)

        pre_ordem(raiz, prordem)
        resprordem = ' '.join(map(str, prordem))

        pos_ordem(raiz, posordem)
        resposordem = ' '.join(map(str, posordem))

        em_ordem(raiz, emordem)
        resemordem = ' '.join(map(str, emordem))

        print(f'Case {tests}')
        print(f'Pre.: {resprordem}')
        print(f'In..: {resemordem}')
        print(f'Post: {resposordem}')
