M = int(input())
N = int(input())
prime = []

for i in range(max(M, 2), N + 1):
    j = 2
    isPrime = 1
    while j * j <= i:
        if i % j == 0:
            isPrime = 0
        j += 1
    if isPrime == 1:
        prime.append(i)
if len(prime) == 0:
    print(-1)
else:
    # print(prime)
    print(sum(prime))
    print(min(prime))
