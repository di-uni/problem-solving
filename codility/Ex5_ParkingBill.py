# First Trial 
# 100%

def solution(E, L):
    cost = 2

    h, m = map(int, E.split(":"))
    ent = h * 60 + m
    h, m = map(int, L.split(":"))
    left = h * 60 + m
    diff = left - ent
    
    if diff == 0:
        return cost
    diff -= 60
    cost += 3

    if diff >= 0:
        cost += (diff // 60) * 4
        if diff % 60 > 0:
            cost += 4

    return cost
