class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        x = start
        for i in range(n):
            if i > 0:
                x = x ^ start + 2 * i

        return x