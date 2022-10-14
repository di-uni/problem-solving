# 2022.10.07
# First Trial
# Test Passed
# Runtime: faster than 95.41%, Memory Usage: less than 91.23%

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]
        
        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                
                if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] == "1":
                    stack += [(x-1, y),(x+1, y),(x, y-1),(x, y+1)]
                    visited[x][y] = True
                    
            # print(visited)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    # print("dfs(", i, j,")")
                    dfs(i, j)
                    ans += 1
                        
        return ans


# =================================================================
# Other's Solution (1)
# visited 필요 없음!
# Runtime: faster than 15.92%, Memory Usage: less than 64.22%

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        
        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                    grid[x][y] = "0"
                    stack += [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        
        return ans


# =================================================================
# Other's Solution (2)
# Concise
# Runtime: faster than 67.68%, Memory Usage: less than 48.14%

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

