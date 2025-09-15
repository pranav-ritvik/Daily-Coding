from collections import defaultdict
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = []
        count = 0
        for ch in brokenLetters:
            broken.append(ch)
        words = text.split()
        for word in words:
            for ch in word:
                if ch in broken:
                    break
            else:
                count = count + 1    
        return count 
