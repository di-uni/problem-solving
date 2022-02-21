N = int(input())
num = list(map(int, input().split()))
prime = 0

for n in num:
    if n > 1:
        isPrime = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                isPrime = 0
            i += 1
        if isPrime:
            prime += 1
    
print(prime)
