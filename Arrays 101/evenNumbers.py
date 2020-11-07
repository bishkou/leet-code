
from typing import List


def findNumbers(nums: List[int]) -> int:
    num = 0
    for i in nums:
        if (len(str(i)) % 2 == 0):
            num += 1
    return num


if __name__ == '__main__':
    nums = [12,345,2,6,7896]
    print(findNumbers(nums))
