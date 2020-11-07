
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    one = 0
    maxi = 0
    for i in range(0, len(nums)):
        if nums[i] == 1:
            one += 1
            if one > maxi:
                maxi = one
        else:
            one = 0

    return maxi


if __name__ == '__main__':
    nums = [1, 0, 1, 1, 0, 1]
    print(findMaxConsecutiveOnes(nums))
