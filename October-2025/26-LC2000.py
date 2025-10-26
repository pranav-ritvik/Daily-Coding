class Solution:
    def reversePrefix(self, word: str, target: str) -> str:
        for i,ch in enumerate(word):
            if ch == target:
                part1 = word[:i+1]
                part1 = part1[::-1]
                part2 = word[i+1:]
                return part1+part2
        return word
