# First Trial
# Test Failed

def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zeros = 0
    
    for l in lottos:
        if l in win_nums:
            cnt += 1
        if l == 0:
            zeros += 1
    
    
    if cnt + zeros <= 1:
        answer.append(6)
    else:
        answer.append(6 - (cnt + zeros) + 1)
        
    if cnt <= 1:
        answer.append(6)
    else:
        answer.append(6 - cnt + 1)
        
    return answer



# ==============================
# Other's Solution


def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    zeros = lottos.count(0)
    cnt = len(set(lottos) & set(win_nums))

    return [rank[zeros + cnt], rank[cnt]]
