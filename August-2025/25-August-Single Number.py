from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        for key, val in count.items():
            if val == 1:
                return key
