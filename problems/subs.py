class Solution:
    from collections import defaultdict
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0

        substr_len_map = defaultdict(int)

        prepend = ' '
        p = prepend + p

        l = 1
        for i in range(1, len(p)):
            # 1. vanilla consecutive or 2. wraparound consecutive
            if ord(p[i]) - ord(p[i - 1]) == 1 or ord(p[i]) - ord(p[i - 1]) == -25:
                l += 1
            else:
                l = 1
            substr_len_map[p[i]] = max(l, substr_len_map[p[i]])

        return sum(substr_len_map.values())