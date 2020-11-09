
from typing import List


def removeDuplicates(nums: List[int]) -> int:

    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i += 1
    return len(nums)

if __name__ == '__main__':
    nums = [1,1,2,2,2,2,2,5,5]
    print(removeDuplicates(nums))
    print(nums)
