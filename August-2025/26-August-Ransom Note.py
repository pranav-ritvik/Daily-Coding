from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = defaultdict(int)        
        for ch in magazine:            
            cnt[ch] += 1
        for ch in ransomNote:
            if cnt[ch] == 0:
                return False
            cnt[ch] -= 1
        return True
