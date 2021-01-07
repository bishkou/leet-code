class Solution:
    def convert(self, s: str, numRows: int) -> str:

        row = 0
        if numRows == 1:
            return s
        down = True
        zzString = [""] * numRows
        for i in range(len(s)):
            zzString[row] = zzString[row] + s[i]
            if down:
                row += 1
                if row == numRows - 1:
                    down = False
            else:
                row -= 1
                if row == 0:
                    down = True

        return "".join(zzString)

