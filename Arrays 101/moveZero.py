from typing import List


def moveZeroes(nums: List[int]) -> None:
    # redo the whole code
    j = 0
    i = 0
    while i < len(nums):
        while j < len(nums) and nums[j] != 0:
            j += 1

        if i > j and i != 0:
            nums[j] = nums[i]
            nums[i] = 0
            i += 1
        else:
            i += 1

if __name__ == '__main__':
    nums = [1, 0, 1, 0, 3, 12]
    moveZeroes(nums)
    # print(moveZeroes(nums))
    print(nums)
