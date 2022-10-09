# 2022.10.09
# First Trial
# Test Passed
# Runtime: faster than 42.55%, Memory Usage: less than 9.03%

from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = defaultdict(list)
        answer = []
        
        def dfs(node: Optional[TreeNode], num):
            if node == None: return
            level[num].append(node.val)
            if node.left:
                dfs(node.left, num + 1)
            if node.right:
                dfs(node.right, num + 1)
        
        dfs(root, 0)
        # print(level)
        for i in range(len(level)):
            answer.append(level[i])


# =================================================================
# Other's Solution
# Concise
# Runtime: faster than 58.16%, Memory Usage: less than 51.21%

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            tmp = []
            for node in level:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            level = tmp
        
        return ans