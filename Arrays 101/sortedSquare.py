from typing import List


def sortedSquares(A: List[int]) -> List[int]:
    return sorted(x * x for x in A)


if __name__ == '__main__':
    nums = [0, 1, 2]
    # moveZeroes(nums)
    print(sortedSquares(nums))
    # print(nums)
