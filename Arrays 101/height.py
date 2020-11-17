from typing import List


def heightChecker(heights: List[int]) -> int:
    x = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i] != x[i]:
            count += 1
    return count


if __name__ == '__main__':
    nums = [1,1,4,2,1,3]
    # moveZeroes(nums)
    print(heightChecker(nums))
    # print(nums)
