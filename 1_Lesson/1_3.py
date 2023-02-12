n = input('Введите шестизначный номер билета: ')

a = int(n[0])
b = int(n[1])
c = int(n[2])
a1 = int(n[3])
b1 = int(n[4])
c1 = int(n[5])

if (a+b+c) == (a1+b1+c1):
    print('Билет счастливый')
else:
    print('Билет не счастливый')