# First Trial
# 100%

import math

def solution(A, B, K):
    if A == B:
        if A % K == 0:
            return 1
        return 0
    max_val = B // K
    min_val = math.ceil(A / K)

    return max_val - min_val + 1


# ====================================
# Other's solution
# 100%

def solution(A, B, K):
    if A == 0:
        return B // K + 1
    else:
        return (B // K + 1) - ((A - 1)// K + 1)