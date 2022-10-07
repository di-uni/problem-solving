# 2022.10.05
# First Trial
# Test Passed 
# Runtime: faster than 28.59%, Memory Usage: less than 43.03%

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        head = ListNode()
        prev, cur = head, head
        
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val + c
                l1, l2 = l1.next, l2.next
            elif not l1:
                val = l2.val + c
                l2 = l2.next
            elif not l2:
                val = l1.val + c
                l1 = l1.next
                
            if val >= 10:
                c = 1
                val -= 10
            else:
                c = 0
            cur.val = val
            cur.next = ListNode()
            prev, cur = cur, cur.next
        
        if c == 1:
            cur.val = c
        if cur.val == 0:
            prev.next = None
        
        return head



# =================================================================
# Other's Solution
# Concise
# Runtime: faster than 87.07%, Memory Usage: less than 43.03%

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = curNode = ListNode()
        
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            curNode.next = ListNode(val)
            curNode = curNode.next
            
        return root.next