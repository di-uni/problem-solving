# First Trial
# Test Passed

def solution(places):
    answer = []
    for place in places:
        room = []
        examinee = []
        for i in range(5):
            temp = []
            for j in range(5):
                temp.append(place[i][j])
                if place[i][j] == "P":
                    examinee.append([i, j])
            room.append(temp)
        if len(examinee) == 0:
            answer.append(1)
            continue
        for p in examinee:
            if [p[0]+1, p[1]] in examinee or [p[0], p[1]+1] in examinee:
                answer.append(0)
                break
            if [p[0]+2, p[1]] in examinee and room[p[0]+1][p[1]] != "X":
                answer.append(0)
                break
            if [p[0], p[1]+2] in examinee and room[p[0]][p[1]+1] != "X":
                answer.append(0)
                break
            if [p[0]+1, p[1]+1] in examinee:
                if not (room[p[0]+1][p[1]] == "X" and room[p[0]][p[1]+1] == "X"):
                    answer.append(0)
                    break
            if [p[0]-1, p[1]+1] in examinee:
                if not (room[p[0]-1][p[1]] == "X" and room[p[0]][p[1]+1] == "X"):
                    answer.append(0)
                    break
        else:
            answer.append(1)
    return answer




# ================================================
# Other's Solution
# Test Passed

from collections import deque

def bfs(p):
    start = []

    for i in range(5):
        for j in range(5):
            if p[i][j] == "P":
                start.append([i, j])

    for s in start:
        queue = deque([s])
        visited = [[0]*5 for _ in range(5)]
        distance = [[0]*5 for _ in range(5)]
        visited[s[0]][s[1]] = 1

        while queue:
            y, x = queue.popleft()

            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))

    return answer