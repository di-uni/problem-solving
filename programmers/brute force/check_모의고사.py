# First Trial
# Test Passed

def solution(answers):
    answer = []
    method1 = [1,2,3,4,5]
    method2 = [2,1,2,3,2,4,2,5]
    method3 = [3,3,1,1,2,2,4,4,5,5]
    
    solve1 = 0
    solve2 = 0
    solve3 = 0
    
    for i in range(len(answers)):
        if method1[i % len(method1)] == answers[i]:
            solve1 += 1
        if method2[i % len(method2)] == answers[i]:
            solve2 += 1
        if method3[i % len(method3)] == answers[i]:
            solve3 += 1
    
    max_solve = max(solve1, solve2, solve3)
    if max_solve == solve1:
        answer.append(1)
    if max_solve == solve2:
        answer.append(2)
    if max_solve == solve3:
        answer.append(3)
        
    return answer

# Second Trial
# more concisely

def solution(answers):
    answer = []
    method = [[1,2,3,4,5],
             [2,1,2,3,2,4,2,5],
             [3,3,1,1,2,2,4,4,5,5]]
    solve = [0] * len(method)
    
    for i in range(len(answers)):
        for j in range(len(method)):
            if method[j][i % len(method[j])] == answers[i]:
                solve[j] += 1
    
    max_solve = max(solve)
    
    for i, sol in enumerate(solve):
        if max_solve == sol:
            answer.append(i + 1)
        
    return answer

# ==============================
# Other's Solution (1)

from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]