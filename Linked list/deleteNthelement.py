# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        aux = head
        j = 0
        prev = aux
        while aux:
            curr = aux
            j += 1
            for i in range(n):
                curr = curr.next
                if i == n - 1:
                    if curr == None:
                        print("found it", aux.val)
                        if aux.next:
                            aux.val = aux.next.val
                            aux.next = aux.next.next
                        elif j == 1:
                            head = None
                        else:
                            prev.next = None

                        return head
            prev = aux
            aux = aux.next