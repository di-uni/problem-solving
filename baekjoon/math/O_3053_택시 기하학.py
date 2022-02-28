# 택시 기하학에서의 원: |x| + |y| = r
# 유클리드 기하학에서의 원: x^2 + y^2 = r^2

import math

R = int(input())

print(round(R * R * math.pi, 6))
print(round(R * R * 2, 6))

# 예시처럼 .000000까지 정확하게 포맷을 맞추기 위해서는
print(f'{R * R * math.pi: .6f}')
print(f'{R * R * 2: .6f}')