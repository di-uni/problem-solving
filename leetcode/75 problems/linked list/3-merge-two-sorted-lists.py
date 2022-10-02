# 2022.09.29
# First Trial
# Test Passed 
# Runtime: faster than 21.83%, Memory Usage: less than 79.35%

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        elif not list1 or not list2:
            return list1 if not list2 else list2
        
        node1 = list1
        node2 = list2
        
        head = node1
        if node2.val < node1.val:
            head = node2
        
        cur_node = head
        while node1 and node2:
            if node1.val <= node2.val:
                next_node = node1
                node1 = node1.next
            else:
                next_node = node2
                node2 = node2.next
            cur_node.next = next_node
            cur_node = next_node
            
        
        # print(head)
        if node1 or node2:
            cur_node.next = node1 if node1 else node2
            
        return head        
        

# =================================================================
# Other's Solution
# Clean code
# Runtime: faster than 35.11%, Memory Usage: less than 32.57%

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
            
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next      
        