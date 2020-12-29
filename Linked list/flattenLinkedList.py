
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child



class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        if head:
            aux = head

            while aux:
                if aux.child:
                    temp = aux
                    ch = temp.child
                    nx = temp.next
                    while temp.child:
                        temp = temp.child

                    while temp.next:
                        temp = temp.next

                    aux.next = aux.child
                    ch.prev = aux
                    temp.next = nx
                    nx.prev = temp
                    aux.child = None
                aux = aux.next



