from itertools import combinations
from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        big = 0
        for a, b, c in combinations(points, 3):
            area = abs(
                a[0] * (b[1] - c[1]) +
                b[0] * (c[1] - a[1]) +
                c[0] * (a[1] - b[1])
            ) / 2
            big = max(big, area)
        return big
