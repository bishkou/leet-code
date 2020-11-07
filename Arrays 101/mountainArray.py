
from typing import List


def validMountainArray(A: List[int]) -> bool:
    i, j, n = 0, len(A) - 1, len(A)
    while i + 1 < n and A[i] < A[i + 1]:
        i += 1
    while j > 0 and A[j - 1] > A[j]:
        j -= 1
    return 0 < i == j < n - 1


if __name__ == '__main__':
    nums = [4,4,3,2,1]
    print(validMountainArray(nums))
    # print(nums)
