from typing import List


def replaceElements(arr: List[int]) -> List[int]:

    max = arr[-1]

    for i in range(len(arr)-2, -1, -1):
        temp = arr[i]
        if arr[i] > max:
            arr[i] = max
            max = temp
        else:
            arr[i] = max
    arr[-1] = -1
    return arr

if __name__ == '__main__':
    nums = [17,18,5,4,6,1]
    print(replaceElements(nums))
    # print(nums)
