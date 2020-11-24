from typing import List


def thirdMax(nums: List[int]) -> int:
    nums.sort()
    if len(nums) < 3:
        return max(nums)
    count = 1
    maxi = nums[-1]
    for i in range(len(nums)-1, -1, -1):
        if nums[i] < maxi:
            maxi = nums[i]
            count += 1
            if count == 3:

                return nums[i]

    return nums[-1]



if __name__ == '__main__':
    nums = [3,2,1]
    print(thirdMax(nums))
