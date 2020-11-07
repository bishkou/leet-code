from typing import List


def sortedSquares(A: List[int]) -> List[int]:
    return sorted(x * x for x in A)


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(sortedSquares(nums))
