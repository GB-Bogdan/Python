def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)

n = int(input())
m = int(input())
print(sum(n,m))