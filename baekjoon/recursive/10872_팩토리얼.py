N = int(input())

def fac(x):
    if x == 0 or x == 1:
        return 1
    return x * fac(x - 1)

print(fac(N))