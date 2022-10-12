# 2022.09.30
# First Trial
# Time Limit Exceeded (135/138)

from heapq import heappush, heappop
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 1
        rows = len(matrix)
        cols = len(matrix[0])
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        heap = []
        for i in range(rows):
            for j in range(cols):
                heappush(heap, (-1, i, j, matrix[i][j]))
        
        while heap:
            cnt, x, y, val = heappop(heap)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < rows and 0 <= ny < cols:
                    if val < matrix[nx][ny]:
                        heappush(heap, (cnt - 1, nx, ny, matrix[nx][ny]))
                        ans = max(-cnt + 1, ans)
                
        
        return ans



# =================================================================
# Other's Solution
# Using dfs
# Runtime: faster than 51.58%, Memory Usage: less than 74.62%

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i-1, j) if i and val > matrix[i-1][j] else 0,
                    dfs(i+1, j) if i < M-1 and val > matrix[i+1][j] else 0,
                    dfs(i, j-1) if j and val > matrix[i][j-1] else 0,
                    dfs(i, j+1) if j < N-1 and val > matrix[i][j+1] else 0
                )
            return dp[i][j]
        
        M, N = len(matrix), len(matrix[0])
        dp = [[0]*N for _ in range(M)]
        
        return max(dfs(x, y) for x in range(M) for y in range(N))