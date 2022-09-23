# First Trial
# Test Failed

def solution(n, lost, reserve):
    answer = n - len(lost)
    new_lost = [l for l in lost if l not in reserve]
    new_reserve = [r for r in reserve if r not in lost]
    answer += len(lost) - len(new_lost)
    
    lost.sort()     # new_lost.sort()로 고쳐주니 test pass !!!!
    for l in new_lost:
        if l - 1 in new_reserve:
            new_reserve.remove(l - 1)
            answer += 1
            continue
        if l + 1 in new_reserve:
            new_reserve.remove(l + 1)
            answer += 1
            
    print(answer)
    
    return answer


# Second Trial
# Test Passed

def solution(n, lost, reserve):
    answer = n - len(lost)
    
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    answer += len(lost) - len(new_lost)
    
    for l in new_lost:
        if l - 1 in new_reserve:
            new_reserve.remove(l - 1)
            answer += 1
            continue
        if l + 1 in new_reserve:
            new_reserve.remove(l + 1)
            answer += 1
            
    
    return answer


# Third Trial
# Test Passed 

def solution(n, lost, reserve):
    selfcover = set(lost) & set(reserve)
    for s in selfcover:
        lost.remove(s)
        reserve.remove(s)
    
    answer = n - len(lost)
    
    lost.sort()
    reserve.sort()
    for l in lost:
        if l - 1 in reserve:
            answer += 1
            reserve.remove(l - 1)
        elif l + 1 in reserve:
            answer += 1
            reserve.remove(l + 1)
    
    return answer