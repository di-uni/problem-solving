N = int(input())
meetings = []

for _ in range(N):
    item = list(map(int, input().split()))
    # print(meetings, item)
    if len(meetings) == 0:
        meetings.append(item)
        continue
    isAdded = False
    for m in meetings:
        if item[0] >= m[0] and item[1] <= m[1]:
            m = item
            isAdded = True
            break
        elif item[0] <= m[0] and item[1] >= m[1]:
            isAdded = True
            break
    if not isAdded: meetings.append(item)

print(meetings)

sub = []
visited = [False] * len(meetings)
max_cnt = float("-inf")

for i, m in enumerate(meetings):
    isAdded = True
    for s in sub:
        if (m[0] < s[0] and m[1] > s[0]) or (m[0] < s[1] and m[1] > s[1]):
            isAdded = False
    if isAdded:
        visited[i] = True
        sub.append(m)

print(sub)
max_cnt = max(max_cnt, len(sub))


if False in visited:
    falses = []
    for i in range(len(visited)):
        if visited[i] == False:
            falses.append([meetings[i], i])
    for f in falses:
        sub = []
        visited = [False] * len(meetings)
        sub.append(f[0])
        visited[f[1]] = True
        for i, m in enumerate(meetings):
            if visited[i]: continue
            isAdded = True
            for s in sub:
                if (m[0] < s[0] and m[1] > s[0]) or (m[0] < s[1] and m[1] > s[1]):
                    isAdded = False
            if isAdded:
                visited[i] = True
                sub.append(m)
        max_cnt = max(max_cnt, len(sub))
        print(sub)

print(max_cnt)