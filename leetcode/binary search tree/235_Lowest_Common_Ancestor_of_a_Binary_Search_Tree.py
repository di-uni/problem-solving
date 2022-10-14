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
# Other's Solution (1)
# Clean code
# Runtime: faster than 32.43%, Memory Usage: less than 67.74%

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root


# =================================================================
# Other's Solution (2)
# Clean code
# Runtime: faster than 12.91%, Memory Usage: less than 23.05%
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while (root.val - p.val) * (root.val - q.val) > 0:
            if p.val < root.val: root = root.left
            else: root = root.right
            
        return root
        