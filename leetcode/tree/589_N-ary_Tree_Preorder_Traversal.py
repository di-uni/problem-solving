# 2022.10.09
# First Trial
# Test Passed
# Runtime: faster than 29.61%, Memory Usage: less than 50.76%

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer = []
        
        if root == None:
            return answer
        
        def recur(node: 'Node'):
            answer.append(node.val)
            for i in node.children:
                recur(i)
                
        recur(root)
        return answer


# =================================================================
# Other's Solution
# Efficient
# Runtime: faster than 94.94%, Memory Usage: less than 50.76%

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output =[]
        self.dfs(root, output)
        return output
    
    def dfs(self, root, output):
        if root is None:
            return
        output.append(root.val)
        for child in root.children:
            self.dfs(child, output)