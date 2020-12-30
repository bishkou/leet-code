# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        h = head.next
        new = Node(head.val)
        nuc = new
        while h:
            n = Node(h.val)
            nuc.next = n
            nuc = nuc.next
            h = h.next

        h = head
        n = new
        i = 0

        while h and n:
            temp = h.random
            k = head
            j = 0

            while k:
                if k == temp:
                    break
                k = k.next
                j += 1

            if j < i:
                m = new
                c = 0
            else:
                m = n
                c = i

            while m:
                if c == j:
                    n.random = m
                    break

                c += 1
                m = m.next

            i += 1
            h = h.next
            n = n.next


        return new
