from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    aux = []
    for i in range(1,len(nums)+1):
        if i not in nums:
            aux.append(i)

    return aux

if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(nums))
