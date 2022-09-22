# First Trial
# NameError: name 'max_score' is not defined

def solution(n, info):
    answer = []
    target = [x for x in range(10, -1, -1)]
    # visited = [False] * 11
    lion_infos = []
    # lion_info = [0] * 11
    # print(target)
    max_score = 0
    
    def dfs(left_arrows, score, lion_info, visited):
        global max_score
        if left_arrows == 0:
            # lion_infos.append([score, lion_info])
            max_score = max(max_score, score)
            if max_score == score:
                print("hey")
            return score, lion_info
        # global visited
        for i, n in enumerate(info):
            if not visited[i] and left_arrows >= n + 1:
                visited[i] = True
                lion_info[i] += n + 1
                dfs(left_arrows - n - 1, score + target[i], lion_info, visited)
                lion_info[i] = 0
                visited[i] = False
                
    print(dfs(n, 0, [0] * 11, [False] * 11))
        
    return answer


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