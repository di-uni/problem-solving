# 2022.10.12
# First Trial
# Test Passed
# Runtime: faster than 33.61%, Memory Usage: less than 89.90%

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visited = [[False]*n for _ in range(m)]
        stack = [(sr, sc)]
        target_color = image[sr][sc]
        visited[sr][sc] = True
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        while stack:
            x, y = stack.pop()
            image[x][y] = color
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and image[nx][ny] == target_color:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
                    
        return image


# 2022.10.12
# Second Trial
# Test Passed
# Runtime: faster than 87.73%, Memory Usage: less than 89.90%

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visited = [[False]*n for _ in range(m)]
        stack = [(sr, sc)]
        target_color = image[sr][sc]
        
        while stack:
            x, y = stack.pop()
            if 0 <= x < m and 0 <= y < n and not visited[x][y] and image[x][y] == target_color:
                image[x][y] = color
                visited[x][y] = True
                stack += [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                    
        return image



# =================================================================
# Other's Solution
# Using recursive
# Runtime: faster than 94.23%, Memory Usage: less than 80.26%