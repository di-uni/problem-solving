# # 유클리드 알고리즘으로 소수 구하기
# # 구한 소수 중 약수 찾기 -> 틀림 !
# # 최대공약수 구하기

# # First Trial
# # Wrong Answer

# import sys

# max_num = 45000
# T = int(sys.stdin.readline().rstrip())

# prime = [True] * (max_num + 1)
# prime[1] = False
# for even in range(2 * 2, max_num + 1, 2):
#     prime[even] = False
# for odd in range(3, int((max_num + 1) ** 0.5) + 1, 2):
#     for j in range(odd * 2, max_num + 1, odd):
#         prime[j] = False

# for _ in range(T):
#     A, B = map(int, sys.stdin.readline().rstrip().split())
#     alis_a = []
#     alis_b = []

#     alis_a.append(1)
#     alis_a.append(A)

#     alis_b.append(1)
#     alis_b.append(B)

#     if ~prime[A]:
#         print(int(A ** 0.5) + 1)
#         for i in range(2, int(A ** 0.5) + 1):
#             if prime[i] and A % i == 0:
#                 alis_a.append(i)
#                 alis_a.append(A // i)
        
#     if ~prime[B]:
#         for i in range(2, int(B ** 0.5) + 1):
#             if prime[i] and B % i == 0:
#                 alis_b.append(i)
#                 alis_b.append(B // i)

#     print(alis_a, alis_b)
#     GCD = max(set(alis_a) & set(alis_b))
#     print(GCD)
#     print(A * B // GCD)


# Second Trial
# 유클리드 호제법 이용
# Solved (메모리 30864 KB, 시간 72 ms)

import sys

T = int(sys.stdin.readline().rstrip())

def GCD(A, B):
    while B != 0:
        A, B = B, A % B
    return A

for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    # while B != 0:
    #     A, B = B, A % B
    #     GCD = A
    # 함수로 구현하지 않으면 A, B 값이 바뀌게 되므로 
    # GCD라는 함수를 정의해서 최대공약수를 계산하였다

    print(A * B // GCD(A, B))


# =========================
# Other's solution
# Solved (메모리 30860 KB, 시간 68 ms)

import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    a, b = A, B
    
    while b != 0:
        a, b = b, a % b

    print(A * B // a)