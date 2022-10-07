# 2022.10.07
# First Trial
# Test Passed
# Runtime: faster than 74.62%, Memory Usage: less than 55.19%

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        cur = head
        
        while cur:
            n += 1
            cur = cur.next
        
        ans = head
        for i in range(n // 2):
            ans = ans.next
            
        return ans



# =================================================================
# Other's Solution
# Using slow and fast pointers
# Runtime: faster than 28.79%, Memory Usage: less than 55.19%

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow