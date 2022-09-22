# First Trial
# Test Passed

def solution(arr):
    answer = [arr[0]]
    prev = arr[0]

    for i in range(1, len(arr)):
        if prev != arr[i]:
            answer.append(arr[i])
        prev = arr[i]
        
    return answer


# ======================================
# Other's solution 
# Test Passed

def solution(arr):
    answer = []
    prev = -1
    
    for a in arr:
        if prev != a:
            answer.append(a)
            prev = a
        
    return answer