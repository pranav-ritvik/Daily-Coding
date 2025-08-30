class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        size = len(words[-1])
        return size
