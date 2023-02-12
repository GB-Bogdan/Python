s = int(input('Сумма = '))
p = int(input('Произведение = '))
a1 = 1

while a1 < p:
    a2 = s - a1
    if s == a1 + a2 and p == a1 * a2:
        print(a1, a2)
        break
    a1 += 1