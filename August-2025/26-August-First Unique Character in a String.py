from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurance = defaultdict(int)

        for ch in s:
            occurance[ch] += 1

        temp = None
        for key, value in occurance.items():
            if value == 1:
                temp = key
                break

        if temp is None:
            return -1

        for i in range(len(s)):
            if s[i] == temp:
                break
        return i
