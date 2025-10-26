class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        for i in order[:]:
            if i in friends:
                continue
            else:
                order.remove(i)
        return order   
