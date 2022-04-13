def solution(n, edges, k, a, b):
    visited = [False] * n
    s = []
    s.append(a)
    used = []

    def dfs(node):
        if len(s) <= k + 1 and s[-1] == b:
            for i in range(len(s)-1):
                if [s[i],s[i+1]] in edges:
                    if [s[i],s[i+1]] not in used:
                        used.append([s[i],s[i+1]])
                if [s[i+1],s[i]] in edges:
                    if [s[i+1],s[i]] not in used:
                        used.append([s[i+1],s[i]])

        for e in edges:
            if e[0] == node and not visited[e[1]]:
                s.append(e[1])
                visited[e[1]] = True
                dfs(e[1])
                visited[e[1]] = False
                s.pop()
            if e[1] == node and not visited[e[0]]:
                s.append(e[0])
                visited[e[0]] = True
                dfs(e[0])
                visited[e[0]] = False
                s.pop()

    dfs(a)
    return len(used)

solution(8, [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]], 4, 0, 3)
solution(2, [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]], 4, 0, 3)