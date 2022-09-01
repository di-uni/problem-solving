def solution(A, B):
    if len(A) == 0 or len(B) == 0:
        return 0
    
    ans = 1
    idx = 0
    for i in range(A[0], B[-1] + 1):
        if i == B[idx]:
            if A[idx] > B[idx-1]:
                ans += 1
            idx += 1
    return ans