from collections import defaultdict
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = defaultdict(int)

        while n != 1:
            if seen[n] > 0:
                return False
            seen[n] += 1
            n = sum(int(d)**2 for d in str(n))
        return True
