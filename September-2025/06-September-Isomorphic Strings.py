from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_t = defaultdict(lambda: None) 
        map_t_s = defaultdict(lambda: None) 

        for a, b in zip(s, t):
            if map_s_t[a] is None and map_t_s[b] is None:
                map_s_t[a] = b
                map_t_s[b] = a
            else:
                if map_s_t[a] != b or map_t_s[b] != a:
                    return False
        return True
