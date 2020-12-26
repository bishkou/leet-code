# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val <= l2.val:
            tst = l1
            pt = l2
            k = 0
        else:
            tst = l2
            pt = l1
            k = 1

        while tst and pt:
            if tst.next is None:
                tst.next = pt
                break
            elif tst.val <= pt.val <= tst.next.val:
                aux = pt
                if pt:
                    pt = pt.next
                aux.next = tst.next
                tst.next = aux
                tst = tst.next

            else:
                tst = tst.next
        if k == 0:
            return l1
        else:
            return l2





