# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        aux = head
        prev = aux
        while aux:
            if aux.val == val:
                if aux == head:
                    head = head.next
                curr = aux
                prev.next = curr.next
                aux = prev

            prev = aux
            aux = aux.next
        return head