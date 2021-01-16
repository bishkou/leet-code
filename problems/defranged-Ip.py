class Solution:
    def defangIPaddr(self, address: str) -> str:

        new = ''
        for l in address:
            if l == '.':
                new += '[.]'
            else:
                new += l

        return new
