# 2022.09.27
# First Trial
# Test Passed : ListNode의 val을 변경시킴, 이를 변경시키지 않는 해결방안 찾아보기

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curNode = head
        
        while curNode:
            if curNode.val == 'visited':
                return True
            else:
                curNode.val = 'visited'
            curNode = curNode.next
        
        return False


# =================================================================
# Other's Solution
# Using tortoise and hare algorithm

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        
        while slow != None and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False