from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = defaultdict(int)

        for ch in s:
            x[ch] += 1
        for ch in t:
            x[ch] -= 1
        for k,v in x.items():
            if v == -1:
                temp = k
                break
        return temp  
            
