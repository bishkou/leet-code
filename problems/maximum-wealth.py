class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        maxi = 0
        for acc in accounts:
            s = 0
            for k in acc:
                s += k
            if s >= maxi:
                maxi = s

        return maxi