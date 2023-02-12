n = int(input('Введите количество монеток: '))

a1 = a0 = 0

for i in range(n):
    coin = int(input())
    if coin:
        a1 += 1
    else:
        a0 += 1

if a1 > a0:
    print(a0)
else:
    print(a1)