class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        canGreatest = []
        greatest = max(candies)
        for n in candies:
            if n + extraCandies >= greatest:
                canGreatest.append(True)
            else:
                canGreatest.append(False)
        return canGreatest

