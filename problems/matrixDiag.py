class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        table = defaultdict(list)
        for i in range(m):
            for j in range(n):
                table[j-i].append(mat[i][j])
        for k in table:
            table[k].sort()
        for i in range(m):
            for j in range(n):
                mat[i][j] = table[j-i].pop(0)
        return mat