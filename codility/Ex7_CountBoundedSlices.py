# First Trial 
# 60% (Timeout error with O(N^2))

def solution(K, A):
    cnt = len(A)
    
    for i in range(len(A)-1):
        temp_min = min(A[i], A[i+1])
        temp_max = max(A[i], A[i+1])
        if temp_max - temp_min > K:
            continue
        cnt += 1
        for j in range(i + 2, len(A)):
            temp_min = min(temp_min, A[j])
            temp_max = max(temp_max, A[j])
            if temp_max - temp_min <= K:
                cnt += 1
            else:
                break
    return cnt