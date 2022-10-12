# 2022.10.11
# First Trial
# Test Passed
# Runtime: faster than 24.74%, Memory Usage: less than 14.03%

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        
        while node:
            # print(node.val, node)
            if node.val > p.val and node.val > q.val:
                node = node.left
                continue
            elif node.val < p.val and node.val < q.val:
                node = node.right
                continue
            else:
                break
        
        return node


# =================================================================
# Other's Solution
# Using recursive
# Runtime: faster than 94.23%, Memory Usage: less than 80.26%