from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  # key: sorted string, value: list of words

        for s in strs:
            key = "".join(sorted(s))   # e.g., "eat" -> "aet", "tea" -> "aet"
            groups[key].append(s)

        return list(groups.values())
