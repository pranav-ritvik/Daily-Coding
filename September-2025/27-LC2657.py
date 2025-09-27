from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        dict_1, dict_2 = {}, {}
        n = len(A)
        ans = []
        common = 0
        
        for i in range(n):
            dict_1[A[i]] = dict_1.get(A[i], 0) + 1
            dict_2[B[i]] = dict_2.get(B[i], 0) + 1

            if A[i] in dict_2:
                common += 1
            if B[i] in dict_1 and B[i] != A[i]:
                common += 1

            ans.append(common)
        
        return ans
