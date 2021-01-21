class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums)):
            s += nums[i + 1:].count(nums[i])

        return s