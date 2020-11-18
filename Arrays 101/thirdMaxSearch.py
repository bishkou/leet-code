from typing import List


def thirdMax(nums: List[int]) -> int:
    nums.sort()
    maxi = 0
    if len(nums) < 3:
        return max(nums)
    count = 0
    p = 0
    for i in nums:
        if i > maxi:
            if count == 0:
                p = i
            maxi = i
            count += 1
            if count == 3:
                return p
    print("her")
    return maxi


if __name__ == '__main__':
    nums = [1,2,2,5,3,5]
    print(thirdMax(nums))
