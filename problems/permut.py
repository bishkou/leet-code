class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        P = []
        res = []
        for i in range(1, m + 1):
            P.append(i)
        for i in range(len(queries)):
            val = queries[i]
            x = P.index(val)
            res.append(x)
            Y = P.pop(x)
            P.insert(0, Y)

        return res