
areas = []

for terreno in range (2):
    pontos = []

    soma1 = 0
    soma2 = 0

    for i in range (4):
        x, y = map(int, input().split())

        pontos.append((x, y))

    for j in range (4):
        x_atual, y_atual = pontos[j]
        x_proximo, y_proximo = pontos[(j + 1) % 4]

        soma1 += x_atual * y_proximo
        soma2 += x_proximo * y_atual

    area = abs(soma1 - soma2) / 2

    areas.append(area)
    
if areas[0] > areas[1]:
    print('terreno A')
else:
    print('terreno B')
