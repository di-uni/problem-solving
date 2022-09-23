# # First Trial
# # NameError: name 'max_score' is not defined

# def solution(n, info):
#     answer = []
#     target = [x for x in range(10, -1, -1)]
#     # visited = [False] * 11
#     lion_infos = []
#     # lion_info = [0] * 11
#     # print(target)
#     max_score = 0
    
#     def dfs(left_arrows, score, lion_info, visited):
#         global max_score
#         if left_arrows == 0:
#             # lion_infos.append([score, lion_info])
#             max_score = max(max_score, score)
#             if max_score == score:
#                 print("hey")
#             return score, lion_info
#         # global visited
#         for i, n in enumerate(info):
#             if not visited[i] and left_arrows >= n + 1:
#                 visited[i] = True
#                 lion_info[i] += n + 1
#                 dfs(left_arrows - n - 1, score + target[i], lion_info, visited)
#                 lion_info[i] = 0
#                 visited[i] = False
                
#     print(dfs(n, 0, [0] * 11, [False] * 11))
        
#     return answer




# Second Trial
# Test Passed
# using dfs

def solution(n, info):
    answer = []
    max_gap = -1

    def getScore(apeach, lion):
        apeachScore, lionScore = 0, 0
        
        for i in range(0, 10):
            if apeach[i] == 0 and lion[i] == 0:
                continue
            if apeach[i] >= lion[i]:
                apeachScore += 10 - i
            else:
                lionScore += 10 - i
        return lionScore - apeachScore
    
    res = [0] * 11
    stack = [(res, 0)]
    while stack:
        lion, k = stack.pop()
        
        if k == 10:
            lion[k] = n - sum(lion)
            
        if sum(lion) == n:
            gap = getScore(info, lion)
            if gap > 0:
                if gap > max_gap:
                    max_gap = gap
                    answer = [lion]
                elif gap == max_gap:
                    answer.append(lion)
            continue
        
        # print(lion, k)
        if sum(lion) + info[k] + 1 <= n:
            lion2 = lion.copy()
            lion2[k] = info[k] + 1
            stack.append((lion2, k + 1))
        stack.append((lion, k + 1))
        # print(stack, answer, max_gap)
        
    if answer:
        # print(answer)
        # 가장 낮은 점수를 더 많이 맞힌 경우 찾기
        answer = sorted(list(map(list, map(reversed, answer))))
        return list(reversed(answer[-1]))
    return [-1]



# ==========================================
# Other's Solution
# using bfs

from collections import deque

def bfs(n, info):
    res = []
    q = deque([(0, [0]*11)])
    maxGap = 0

    while q:
        focus, arrow = q.popleft()

        if sum(arrow) == n:     # 종료조건 1) 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            
            if apeach < lion:
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap
                    res.clear()
                res.append(arrow)

        # elif sum(arrow) > n:    # 종료조건 2) 화살 더 쏜 경우
        #     continue
            
        elif focus == 10:   # 종료조건 3) 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)   # 마지막 과녁에 다 쏴준다
            q.append((-1, tmp))         # focus는 이제 필요없어서 아무값이나 넣어주기

        else:   # 화살 쏘기
            tmp = arrow.copy()
            if sum(arrow) + info[focus] + 1 <= n:   # 화살을 n개보다 많이 쏘지 않을 때만
                tmp[focus] = info[focus] + 1
                q.append((focus+1, tmp))
                tmp[focus] = 0
            q.append((focus+1, tmp))

    return res

def solution(n, info):
    winList = bfs(n, info)

    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]


# ==========================================
# Other's Solution
# using 중복조합

from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_gap = -1

    def getScore(apeach, lion):
        apeachScore, lionScore = 0, 0
        
        for i in range(0, 10):
            if apeach[i] == 0 and lion[i] == 0:
                continue
            if apeach[i] >= lion[i]:
                apeachScore += 10 - i
            else:
                lionScore += 10 - i
            # print(apeachScore, lionScore)
        if lionScore > apeachScore:
            return lionScore - apeachScore
        else:
            return -1
    
    for combi in combinations_with_replacement(range(11), n):
        lion = [0] * 11

        for i in combi:
            lion[10 - i] += 1

        if getScore(info, lion) > 0:
            gap = getScore(info, lion)
            if gap > max_gap:
                max_gap = gap
                answer = lion
            # elif gap == max_gap:
            #     answer.append(lion)
            
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))