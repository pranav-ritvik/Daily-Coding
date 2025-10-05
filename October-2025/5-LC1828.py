class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for x, y, r in queries:
            count = 0
            for a, b in points:
                if (a - x) ** 2 + (b - y) ** 2 <= r ** 2:
                    count += 1
            ans.append(count)
        return ans
