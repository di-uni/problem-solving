# # First Trial
# # Solved (메모리 30840 KB, 시간 1232 ms)

# N = int(input())
# S = []

# for _ in range(N):
#     S.append(list(map(int, input().split())))

# result = float("inf")

# def dfs(i, scoreA, scoreB, teamA, teamB):
#     global result
#     if i == N:
#         # print(result, abs(scoreA - scoreB), teamA, teamB)
#         result = min(abs(scoreA - scoreB), result)
#     else:
#         if len(teamA) < N // 2:
#             teamA.append(i)
#             temp = 0
#             for t in teamA:
#                 temp += S[i][t] + S[t][i]
#             dfs(i + 1, scoreA + temp, scoreB, teamA, teamB)
#             teamA.pop()
#         if len(teamB) < N // 2:
#             teamB.append(i)
#             temp = 0
#             for t in teamB:
#                 temp += S[i][t] + S[t][i]
#             dfs(i + 1, scoreA, scoreB  + temp, teamA, teamB)
#             teamB.pop()

# dfs(0, 0, 0, [], [])

# print(result)



# Second Trial
# 중복되는 case 없애기 (Referred to Other's Solution) -> 근데 더 오래 걸리네..
# Solved (메모리 30840 KB, 시간 1672 ms)

N = int(input())
S = []

for _ in range(N):
    S.append(list(map(int, input().split())))

result = float("inf")

def dfs(i, scoreA, teamA):
    global result
    if len(teamA) == N // 2:
        # print(result, abs(scoreA - scoreB), teamA, teamB)
        scoreB = 0
        teamB = [x for x in range(N) if x not in teamA]
        for i in teamB:
            for j in teamB:
                scoreB += S[i][j]
        result = min(abs(scoreA - scoreB), result)
    else:
        if i == N - 1:
            return
        teamA.append(i)
        temp = 0
        for t in teamA:
            temp += S[i][t] + S[t][i]
        dfs(i + 1, scoreA + temp, teamA)
        teamA.pop()
        dfs(i + 1, scoreA, teamA)

dfs(0, 0, [])

print(result)