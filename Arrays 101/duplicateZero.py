from typing import List



def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    aux = []
    for i in arr:
        aux.append(i)
        if i == 0:
            aux.append(i)
    for i in range(len(arr)):
        arr[i] = aux[i]


    # return arr

if __name__ == '__main__':
    nums = [1,0,2,3,0,4,5,0]
    duplicateZeros(nums)
    print(nums)