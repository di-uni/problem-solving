N = int(input())
pts = []

for _ in range(N):
    pts.append(list(map(int, input().split())))

# # First Trial
# Solved (메모리 51636 KB, 시간 4444 ms)
pts.sort(key=lambda x: x[0])
pts.sort(key=lambda x: x[1])

# Other's solution
# Solved (메모리 57780 KB, 시간 4520 ms)
pts.sort(key=lambda x: (x[1], x[0]))    
# 해설: 비교할 아이템이 여러 개인 경우, 튜플로 우선순위를 정해줄 수 있음. 여기서는 y좌표가 우선순위
# 추가: -를 붙이면, 내림차순으로 정렬됨
# pts.sort(key=lambda x: (x[1], -x[0]))    

for p in pts:
    print(p[0], p[1])