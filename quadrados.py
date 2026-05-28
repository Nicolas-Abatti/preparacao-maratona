from math import factorial

N = int(input())

while N != 0:

    resultado = 0

    for i in range (N, 0, -1):
        resultado += i * i

    print(resultado)

    N = int(input())
