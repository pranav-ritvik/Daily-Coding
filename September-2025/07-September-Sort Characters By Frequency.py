from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse = True)
        for k,v in sorted_freq:
            ans += k*v
        return ans
