N = int(input())

for i in range(0, N):
    x, y = map(int, input().split())

    a = int((x * y) / 2)

    print(f'{a} cm2')
