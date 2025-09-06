# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        l = 0
        if head is None:
            return 0
        current = head
        while current.next:
            l = l+1
            current = current.next
        return (l+1)

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        size = self.length(head)
        for i in range(size // 2):
            current = current.next
        head = current
        return current 
        
