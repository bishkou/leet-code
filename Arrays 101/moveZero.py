
from typing import List


def moveZeroes(nums: List[int]) -> None:

    j = 0
    i = 0
    while i < len(nums):
        while j < len(nums) and nums[j] == 0:
            j += 1
        if len(nums) > j != i:
            temp = nums[j]
            if nums[i] == 0 and j > i:
                nums[i] = temp
                nums[j] = 0
                j += 1
            i += 1
        else:
            i += 1
            pass

if __name__ == '__main__':
    nums = [1,0,1,0,3,12]
    moveZeroes(nums)
    # print(moveZeroes(nums))
    print(nums)
