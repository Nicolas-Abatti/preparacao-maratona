matriz = []
soma = 0
contador = 0

l = input().upper()

for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

for i in range (12):
    for j in range (12):
        if j > i:
            soma += matriz[i][j]
            contador += 1
        
if l == 'S':
    print(soma)
else:
    print(f'{(soma/contador):.1f}')
    