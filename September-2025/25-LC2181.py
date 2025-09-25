# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  
        tail = dummy         
        current = head.next   
        total = 0

        while current:
            if current.val == 0:        
                new = ListNode(total)    
                tail.next = new           
                tail = tail.next          
                total = 0                 
            else:
                total += current.val
            current = current.next

        return dummy.next
