# ======================================
# Other's solution 
# Test Passed

def solution(n, times):
    left = min(times)
    right = max(times) * n
    
    while left < right:
        mid = (left + right) // 2
        checked = sum([mid//i for i in times])
        if checked >= n:
            right = mid
        elif checked < n:
            left = mid + 1
            
    return left