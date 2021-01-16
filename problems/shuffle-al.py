class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        aux = []
        for i in range(n):
            aux.append(nums[i])
            aux.append(nums[n + i])
        return aux