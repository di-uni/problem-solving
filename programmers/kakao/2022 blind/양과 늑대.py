from collections import defaultdict
def solution(info, edges):
    answer = 0
    
    next_nodes = defaultdict(list)
    for i, j in edges:
        next_nodes[i].append(j)

    def dfs(sheep, wolf, current, path):
        if info[current]:
            wolf += 1
        else:
            sheep += 1
            
        if sheep <= wolf:
            return 0
        
        maxSheep = sheep
        
        for p in path:
            for n in next_nodes[p]:
                if n not in path:
                    path.append(n)
                    maxSheep = max(maxSheep, dfs(sheep, wolf, n, path))
                    path.pop()
        # print(maxSheep)
        return maxSheep
    
    answer = dfs(0, 0, 0, [0])
    return answer