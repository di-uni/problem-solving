import math

def solution(N):
    for i in range(int(math.log2(N)) + 1):
        if N % (2 ** i) != 0:
            return i - 1
    return int(math.log2(N))