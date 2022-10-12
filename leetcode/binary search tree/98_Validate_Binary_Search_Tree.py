# 2022.10.11
# First Trial
# Test Passed
# Runtime: faster than 24.74%, Memory Usage: less than 14.03%

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(array: List[int], root: Optional[TreeNode]):
            if root.left:
                inorder(array, root.left)
            array.append(root.val)
            # print(root.val)
            if root.right:
                inorder(array, root.right)
            
        inorderlist = []
        inorder(inorderlist, root)
        # print(inorderlist)
        
        return inorderlist == sorted(list(set(inorderlist)))



# =================================================================
# Other's Solution
# Using recursive
# Runtime: faster than 94.23%, Memory Usage: less than 80.26%

class Solution:
    def isValidBST(self, root: Optional[TreeNode], floor=float("-inf"), ceiling=float("inf")) -> bool:
        if not root:
            return True
        if not floor < root.val < ceiling:
            return False
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)