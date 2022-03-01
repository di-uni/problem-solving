# 값이 같은 원소의 전후관계가 바뀌지 않는 정렬 알고리즘을 안정 정렬(stable sort)이라고 한다.

N = int(input())
judges = []

for _ in range(N):
    judges.append(list(input().split()))

judges.sort(key=lambda x: int(x[0]))

for j in judges:
    print(j[0], j[1])