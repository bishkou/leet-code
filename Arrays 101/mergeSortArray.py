from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1.extend(nums2)
    nums1.sort()
    for i in range(len(nums1) - (m+n)):
        nums1.remove(0)


if __name__ == '__main__':
    nums = [1, 2, 3, 0, 0, 0]
    merge(nums, 3, [2, 5, 6], 3)
    print(nums)
