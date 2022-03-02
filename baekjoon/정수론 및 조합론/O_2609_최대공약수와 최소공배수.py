# First Trial
# Solved (메모리 30864 KB, 시간 72 ms)

a, b = map(int, input().split())
alis_a = []
alis_b = []

for i in range(1, max(int(a ** 0.5) + 1, int(b ** 0.5) + 1)):
    if a % i == 0:
        alis_a.append(i)
        alis_a.append(a // i)
    if b % i == 0:
        alis_b.append(i)
        alis_b.append(b // i)

# Handling prime number 
alis_a.append(a)
alis_b.append(b)

alis_a = set(alis_a)
alis_b = set(alis_b)
# print(alis_a, alis_b)

if len(alis_a & alis_b) == 0:
    GCD = 1
else:
    GCD = max(alis_a & alis_b)
LCM = int(a * b // GCD)
print(GCD)
print(LCM)


# ===================================
# Other's solution (1)
# 유클리드 호제법 이용 (https://ko.wikipedia.org/wiki/유클리드_호제법)
# Solved (메모리 30864 KB, 시간 72 ms)

a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    # 유클리드 호제법에는 a > b 라는 조건이 붙지만 
    # a < b 일 때 a, b = b, a % b 연산을 해주면 a, b가 swap하므로 위 조건을 따로 고려해주지 않아도 된다.
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))


# Other's solution (2)
# 파이썬 math 모듈 함수 이용
# Solved (메모리 32976 KB, 시간 80 ms)
import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))
