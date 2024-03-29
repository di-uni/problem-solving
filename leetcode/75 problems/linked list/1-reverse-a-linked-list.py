# 2022.09.27
# First Trial
# Test Passed

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prevNode = None
        curNode = head
        
        while curNode != None:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
            
        return prevNode

# 2022.10.06
# Second Trial
# Test Passed
# Runtime: faster than 90.23%, Memory Usage: less than 55.07%

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        
        while cur:
            next = cur.next
            cur.next = prev
            prev, cur = cur, next
        
        return prev