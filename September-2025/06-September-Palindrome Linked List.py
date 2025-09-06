# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        num1 = []
        current = head
        if current.next == None:
            return True
        while current:
            num1.append(current.val)
            current = current.next
        num2 = num1[::-1]
        return num1 == num2
