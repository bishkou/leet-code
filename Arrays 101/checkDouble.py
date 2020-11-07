
from typing import List


def checkIfExist(arr: List[int]) -> bool:
    for i in range(len(arr)):
        if (arr[i] * 2) in arr[i+1:len(arr)]:
            print(i)
            return True
        elif (arr[i] * 2) in arr[0:i]:
            print(i)
            return True

    return False

if __name__ == '__main__':
    nums = [-2,0,10,-19,4,6,-8]
    print(checkIfExist(nums))
    # print(nums)
