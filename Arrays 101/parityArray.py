from typing import List


def sortArrayByParity(A: List[int]) -> List[int]:
    if len(A) > 1:
        i = 0
        j = 0
        while i < len(A):
            while j < len(A) - 1 and A[j] % 2 != 0:
                j += 1

            print(j)
            if i < j and A[i] != 0:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                i += 1
            else:
                i += 1
                j += 1

    return A


if __name__ == '__main__':
    nums = [0, 1, 2]
    # moveZeroes(nums)
    print(sortArrayByParity(nums))
    # print(nums)
