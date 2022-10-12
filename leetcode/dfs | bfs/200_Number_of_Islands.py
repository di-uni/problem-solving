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
# Other's Solution
# Using recursive
# Runtime: faster than 94.23%, Memory Usage: less than 80.26%