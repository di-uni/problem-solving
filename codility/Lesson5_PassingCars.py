# First Trial
# 90% (didn't consider the direction)

def solution(A):
    basis_car = A[0]
    basis_cnt = 1
    passing = 0

    for i in range(1, len(A)):
        if A[i] == basis_car:
            basis_cnt += 1
        else:
            passing += basis_cnt

    if passing > 1000000000:
        return -1

    return passing


# Second Trial
# 100%

def solution(A):
    east_cnt = 0
    passing = 0

    for car in A:
        if car == 0:
            east_cnt += 1
        else:
            passing += east_cnt

    if passing > 1000000000:
        return -1

    return passing