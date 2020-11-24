from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    length_nums = len(nums)
    all_numbers_set = set(range(1, length_nums + 1))

    for num in nums:
        if num in all_numbers_set:
            all_numbers_set.remove(num)

    return list(all_numbers_set)

if __name__ == '__main__':
    nums = [1,1]
    print(findDisappearedNumbers(nums))
