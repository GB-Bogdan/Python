def exp(a, b):
    if b == 0:
        return 1
    if b < 0:
        return exp(a, b + 1) * 1 / a
    return exp(a, b -1) * a

print(exp(int(input()), int(input())))