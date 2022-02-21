self = [0] * 10001
self[0] = 1

def d(n):
    temp = n    
    while n > 0:
        temp += n % 10
        n //= 10
    if temp <= 10000:
        self[temp] = 1
        d(temp)

for i in range(1, 10001):
    d(i)

for i, s in enumerate(self):
    if s == 0:
        print(i)