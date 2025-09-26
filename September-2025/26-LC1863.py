from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        
        for k in range(1, n+1):
            for subset in combinations(nums, k):
                xor_val = 0
                for num in subset:
                    xor_val ^= num   
                total += xor_val
        
        return total
