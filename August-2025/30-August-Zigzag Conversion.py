class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return s
        if numRows == 1:
            return s
        if len(s) == 1:
            return s
        if numRows >= len(s):
            return s

        rows = ["" for _ in range(numRows)]
        row = 0
        going_down = True

        for ch in s:
            rows[row] += ch
            if row == 0:
                going_down = True
            elif row == numRows - 1:
                going_down = False
            if going_down:
                row += 1
            else:
                row -= 1

        return "".join(rows)
