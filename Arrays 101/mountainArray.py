
from typing import List


def validMountainArray(A: List[int]) -> bool:
    if len(A) < 3:
        return False
    else:
        i = 0
        j = len(A) - 1
        k = 0
        m = 0

        while i < j:
            if (A[i] < A[i + 1]):
                if k > 0:
                    return False
                else:
                    i += 1
                    m += 1

            elif (A[i] == A[i + 1] and m > 0):
                i += 1

            elif (A[i] > A[i + 1]):
                print(m)
                print(A[i])
                if m > 0:
                    k += 1
                    i += 1
                else:
                    return False
            else:
                return False

        if (k > 0):
            return True
        else:
            return False


if __name__ == '__main__':
    nums = [4,4,3,2,1]
    print(validMountainArray(nums))
    # print(nums)
