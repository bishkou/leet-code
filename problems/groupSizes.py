class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        ret = []
        dirs = {}
        for index, groupSize in enumerate(groupSizes):
            if groupSize == 1:
                ret.append([index])
            else:
                if groupSize not in dirs:
                    dirs[groupSize] = [index]
                else:
                    dirs[groupSize].append(index)
        for num in dirs:
            temp = 0
            while (temp < len(dirs[num])):
                ret.append(dirs[num][temp: temp + num])
                temp += num
        return ret