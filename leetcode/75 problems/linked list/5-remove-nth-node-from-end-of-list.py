# 2022.09.29
# First Trial
# Test Passed 
# Runtime: faster than 10.69%, Memory Usage: less than 72.33%

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        
        while node:
            node = node.next
            length += 1
            
        buffer = ListNode(0, head)
        node = buffer
        for i in range(length-n):
            node = node.next
        
        node.next = node.next.next
        
        return buffer.next



# =================================================================
# Other's Solution
# Using two linked list
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/1164542/JS-Python-Java-C%2B%2B-or-Easy-Two-Pointer-Solution-w-Explanation

# Runtime: faster than 19.18%, Memory Usage: less than 70.34% 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        for _ in range(n): 
            fast = fast.next
        if not fast: 
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head