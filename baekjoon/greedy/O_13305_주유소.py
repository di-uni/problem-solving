# First Trial
# Solved (메모리 45396 KB, 시간 148 ms)

N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_val = costs[0]
for i, c in enumerate(costs):
    if c < min_val:
        min_val = c
    costs[i] = min_val

# costs.pop()
ans = 0
for road, cost in zip(roads, costs):
    ans += road * cost

print(ans)


# ===================================
# Other's solution 
# for loop 하나만 사용
# Solved (메모리 45388 KB, 시간 144 ms)

N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))
ans = 0

min_val = costs[0]
for i in range(N - 1):
    if costs[i] < min_val:
        min_val = costs[i]
    ans += min_val * roads[i]

print(ans)