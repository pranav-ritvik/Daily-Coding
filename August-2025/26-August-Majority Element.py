from collections import defaultdict
import numpy as np

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = defaultdict(int)
        for i in nums:
            frequency[i] += 1
        sorted_frequency = sorted(frequency.items(), key=lambda x:x[1], reverse=True)
        return sorted_frequency[0][0]
