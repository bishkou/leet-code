
from typing import List


def removeElement(nums: List[int], val: int) -> int:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    j = 0
    for i in nums:
        if i == val:
            j += 1
    for i in range(j):
        nums.remove(val)
    print(nums)
    return len(nums)



if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    print(removeElement(nums, 2))
    # print(nums)
