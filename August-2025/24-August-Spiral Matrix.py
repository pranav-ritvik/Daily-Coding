class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # go right
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # go down
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # go left (if there is a remaining row)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # go up (if there is a remaining column)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res
