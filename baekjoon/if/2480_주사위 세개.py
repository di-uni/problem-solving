a, b, c = map(int, input().split())

if a == b and b == c:
    print(10000 + a * 1000)
    exit(0)
elif a == b:
    print(1000 + a * 100)
    exit(0)
elif b == c:
    print(1000 + b * 100)
    exit(0)
elif c == a:
    print(1000 + c * 100)
    exit(0)
else:
    print(max(a, b, c) * 100)
    exit(0)
