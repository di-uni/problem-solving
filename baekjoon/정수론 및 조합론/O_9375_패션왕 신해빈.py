# First Trial
# Solved (메모리 32412 KB, 시간 108 ms)

from collections import defaultdict
T = int(input())

for _ in range(T):
    n = int(input())
    clothes = defaultdict(int)
    for _ in range(n):
        cloth, type = input().split()
        clothes[type] += 1
    result = 1
    for i in clothes.values():
        result *= (i + 1)
    print(result - 1)



# ===================================
# Other's solution 
# Counter 사용
# Solved (메모리 32420 KB, 시간 116 ms)

from collections import Counter
T = int(input())

for _ in range(T):
    n = int(input())
    clothes = []
    for _ in range(n):
        cloth, type = input().split()
        clothes.append(type)
    
    type_Counter = Counter(clothes)
    result = 1
    for key in type_Counter:
        result *= type_Counter[key] + 1

    print(result - 1)