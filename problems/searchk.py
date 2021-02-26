class Solution:
    def search(self, nums: List[int], target: int) -> int:

        try:
            k = nums.index(target)
            return k
        except:
            return -1