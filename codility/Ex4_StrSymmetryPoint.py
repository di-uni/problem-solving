# First Trial 
# 100%

def solution(S):
    if S == "" or len(S) % 2 == 0:
        return -1
    
    if len(S) == 1:
        return 0
    
    for i in range(len(S)//2):
        if S[i] != S[-1-i]:
            return -1
    
    return len(S)//2
