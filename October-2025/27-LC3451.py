from collections import defaultdict
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a','e','i','o','u']
        freq = defaultdict(int)

        for ch in s:
            freq[ch]+=1
        
        max_c = 0
        max_v = 0

        for k,v in freq.items():
            if k in vowels:
                max_v = max(max_v,v)
            else:
                max_c = max(max_c,v)
        return max_c + max_v
