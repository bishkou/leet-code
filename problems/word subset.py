class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        s = ''
        for el in B:
            for e in s:
                if e in el:
                    el = el.replace(e, '', 1)
            s += el

        new = []
        temp = A
        j = 0
        for el in temp:
            i = 0
            for e in s:
                if e in el:
                    el = el.replace(e, '', 1)
                    i += 1
                    if i == k:
                        new.append(A[j])
                        break
            j += 1

        return new